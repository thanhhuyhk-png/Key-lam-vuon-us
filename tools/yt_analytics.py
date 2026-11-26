#!/usr/bin/env python3
"""
yt_analytics.py — Phase 4 OAuth Analytics tự động cho Garden US.

Lệnh:
  python tools/yt_analytics.py sync            # baseline 28d + top videos + vùng chết retention
                                               #   -> ghi references/yt-analytics-latest.json
                                               #   -> cập nhật block DATA_TRUTH trong channel-truth.md
  python tools/yt_analytics.py retro <videoId> # AVD + retention curve 1 video -> block ACTUAL cho retro.md
  python tools/yt_analytics.py update-truth [json] # cap nhat channel-truth tu JSON benchmark CO SAN (khong fetch)
                                               #   default json = references/channel-stats-garden-us-60k.json
                                               #   -> dung boi routine garden-us-60k-weekly-benchmark (gop A)
  python tools/yt_analytics.py health [weeks]  # SELF-BASELINE health metrics (default 8 tuan)
                                               #   xu huong AVD/views theo tuan + traffic mix ky nay vs ky truoc
                                               #   + outlier ratio + duration band + early velocity 5 ngay dau
                                               #   -> ghi references/channel-health-latest.json
                                               #   -> doc boi skill yt-channel-health-audit (skill CHI dien giai)

Chỉ đọc (scopes: youtube.readonly + yt-analytics.readonly). KHÔNG ghi gì lên YouTube.
CTR thumbnail KHÔNG có trong Analytics API -> vẫn nhập tay từ Studio.
"""
import json, sys, os, datetime, statistics, urllib.request, urllib.parse, urllib.error, re

try:
    sys.stdout.reconfigure(encoding="utf-8")  # Windows console cp1252 -> cho phép emoji
except Exception:
    pass

UTC = datetime.timezone.utc


def _utcnow():
    return datetime.datetime.now(UTC)


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load_config():
    """Đọc channel.config.json ở gốc workspace → mọi path/slug suy ra từ đây (đa kênh)."""
    try:
        return json.load(open(os.path.join(ROOT, "channel.config.json"), encoding="utf-8"))
    except Exception:
        return {}


CONFIG = _load_config()
SLUG = CONFIG.get("youtube_channel_slug", "garden-us-60k")
ENV_FILE = os.path.join(ROOT, ".env")
TOKEN_FILE = os.path.join(ROOT, ".secrets", "youtube-token-%s.json" % SLUG)
DIGEST_FILE = os.path.join(ROOT, "references", "yt-analytics-latest.json")
STATS_JSON = os.path.join(ROOT, "references", "channel-stats-%s.json" % SLUG)
TRUTH_FILE = os.path.join(ROOT, CONFIG.get("brand_voice_file", "references/channel-truth.md").replace("/", os.sep))

ANALYTICS = "https://youtubeanalytics.googleapis.com/v2/reports"
DATA = "https://www.googleapis.com/youtube/v3"


# ---------- auth ----------
def _get(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    try:
        return json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e:
        sys.exit("API error %s: %s" % (e.code, e.read().decode()[:500]))


def get_access_token():
    """Trả access token còn hạn; tự refresh + cache lại nếu hết hạn."""
    tok = json.load(open(TOKEN_FILE, encoding="utf-8"))
    exp = tok.get("expiry")
    if exp:
        try:
            if datetime.datetime.strptime(exp, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=UTC) > _utcnow() + datetime.timedelta(minutes=2):
                return tok["token"]
        except ValueError:
            pass
    data = urllib.parse.urlencode({
        "client_id": tok["client_id"], "client_secret": tok["client_secret"],
        "refresh_token": tok["refresh_token"], "grant_type": "refresh_token",
    }).encode()
    try:
        j = json.load(urllib.request.urlopen(urllib.request.Request(tok["token_uri"], data=data)))
    except urllib.error.HTTPError as e:
        sys.exit("Refresh token FAILED %s: %s\n-> Token có thể bị thu hồi. Liên kết lại kênh." % (e.code, e.read().decode()[:300]))
    tok["token"] = j["access_token"]
    tok["expiry"] = (_utcnow() + datetime.timedelta(seconds=int(j.get("expires_in", 3600)))).strftime("%Y-%m-%dT%H:%M:%SZ")
    json.dump(tok, open(TOKEN_FILE, "w", encoding="utf-8"))
    return tok["token"]


def api_key():
    for line in open(ENV_FILE, encoding="utf-8"):
        if line.startswith("YOUTUBE_API_KEY="):
            return line.split("=", 1)[1].strip()
    return None


def analytics(access, **params):
    url = ANALYTICS + "?" + urllib.parse.urlencode(params)
    return _get(url, {"Authorization": "Bearer " + access})


# ---------- helpers ----------
def iso8601_to_sec(d):
    m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", d or "")
    if not m:
        return 0
    h, mi, s = (int(x) if x else 0 for x in m.groups())
    return h * 3600 + mi * 60 + s


def video_meta(access, ids):
    """title + duration (giây) + ngày đăng + privacy cho list videoId.

    Hỏi bằng OAuth của CHỦ KÊNH, không phải API key công khai: key công khai không thấy
    video private, nên video bị ẩn sẽ bị nhầm thành đã xoá. Chỉ video xoá hẳn mới vắng mặt.
    """
    out = {}
    for i in range(0, len(ids), 50):
        chunk = ids[i:i + 50]
        j = _get(DATA + "/videos?" + urllib.parse.urlencode(
            {"part": "snippet,contentDetails,status", "id": ",".join(chunk)}),
            {"Authorization": "Bearer " + access})
        for it in j.get("items", []):
            out[it["id"]] = {"title": it["snippet"]["title"],
                             "dur": iso8601_to_sec(it["contentDetails"]["duration"]),
                             "published": it["snippet"]["publishedAt"][:10],
                             "privacy": it["status"].get("privacyStatus", "public")}
    return out


def fmt_mmss(s):
    return "%d:%02d" % (s // 60, s % 60)


# ---------- commands ----------
def cmd_sync():
    access = get_access_token()
    end = datetime.date.today()
    start = end - datetime.timedelta(days=28)
    ds, de = str(start), str(end)

    base = analytics(access, ids="channel==MINE", startDate=ds, endDate=de,
                     metrics="views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained,subscribersLost")
    bc = [c["name"] for c in base["columnHeaders"]]
    br = dict(zip(bc, base["rows"][0])) if base.get("rows") else {}

    top = analytics(access, ids="channel==MINE", startDate=ds, endDate=de,
                    dimensions="video", metrics="views,averageViewPercentage,averageViewDuration",
                    sort="-views", maxResults=10)
    tcols = [c["name"] for c in top["columnHeaders"]]
    trows = top.get("rows", [])
    vids = [r[tcols.index("video")] for r in trows]
    meta = video_meta(access, vids) if vids else {}
    top_videos = []
    for r in trows:
        d = dict(zip(tcols, r))
        vid = d["video"]
        top_videos.append({
            "videoId": vid, "title": meta.get(vid, {}).get("title", vid),
            "views": int(d["views"]), "avd_pct": round(d["averageViewPercentage"], 1),
            "url": "https://youtu.be/" + vid,
        })

    manual_ctr = None  # API không expose CTR -> giữ giá trị nhập tay gần nhất từ channel-stats JSON
    try:
        manual_ctr = json.load(open(STATS_JSON, encoding="utf-8")).get("manual_ctr_pct")
    except Exception:
        pass

    digest = {
        "fetched_at": _utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "date_range": {"start": ds, "end": de},
        "baseline": {
            "views_28d": int(br.get("views", 0)),
            "watch_minutes_28d": int(br.get("estimatedMinutesWatched", 0)),
            "avg_view_duration_s": int(br.get("averageViewDuration", 0)),
            "avd_pct": round(br.get("averageViewPercentage", 0), 2),
            "subs_gained": int(br.get("subscribersGained", 0)),
            "subs_lost": int(br.get("subscribersLost", 0)),
            "subs_net": int(br.get("subscribersGained", 0)) - int(br.get("subscribersLost", 0)),
            "ctr_pct": manual_ctr,
        },
        "top_videos": top_videos,
    }
    json.dump(digest, open(DIGEST_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    update_truth(digest)

    b = digest["baseline"]
    avd_flag = "🔴" if b["avd_pct"] < 40 else "✅"
    print("SYNC OK  %s -> %s" % (ds, de))
    print("  Views %s | AVD %s%% %s | AvgDur %ss | Net subs +%d" % (
        f"{b['views_28d']:,}", b["avd_pct"], avd_flag, b["avg_view_duration_s"], b["subs_net"]))
    print("  Top video: %s (%s views, AVD %s%%)" % (
        top_videos[0]["title"][:50], f"{top_videos[0]['views']:,}", top_videos[0]["avd_pct"]) if top_videos else "  (no videos)")
    print("  -> %s" % os.path.relpath(DIGEST_FILE, ROOT))
    print("  -> channel-truth.md DATA_TRUTH block cập nhật")
    print("  ⚠️ NHẮC: nhập CTR tay từ YouTube Studio (Reach > CTR 28d) — API không có.")


def cmd_retro(video_id):
    access = get_access_token()
    end = datetime.date.today()
    start = end - datetime.timedelta(days=90)
    meta = video_meta(access, [video_id]).get(video_id, {"title": video_id, "dur": 0})
    dur = meta["dur"]

    base = analytics(access, ids="channel==MINE", startDate=str(start), endDate=str(end),
                     dimensions="video", filters="video==" + video_id,
                     metrics="views,averageViewPercentage,averageViewDuration")
    bc = [c["name"] for c in base["columnHeaders"]]
    br = dict(zip(bc, base["rows"][0])) if base.get("rows") else {}

    # retention curve
    ret = analytics(access, ids="channel==MINE", startDate=str(start), endDate=str(end),
                    dimensions="elapsedVideoTimeRatio", filters="video==" + video_id,
                    metrics="audienceWatchRatio")
    rrows = ret.get("rows", [])
    curve = [(float(r[0]), float(r[1])) for r in rrows]  # (ratio 0..1, watchRatio)

    biggest_drop = None
    if len(curve) > 1 and dur:
        for i in range(1, len(curve)):
            delta = curve[i][1] - curve[i - 1][1]
            sec = curve[i][0] * dur
            if biggest_drop is None or delta < biggest_drop[2]:
                biggest_drop = (curve[i - 1][0] * dur, sec, delta)

    avd = round(br.get("averageViewPercentage", 0), 1)
    print("# ACTUAL — %s" % meta["title"])
    print("Video: https://youtu.be/%s  | duration %s" % (video_id, fmt_mmss(dur)))
    print("| Chỉ số | THẬT |")
    print("|--------|------|")
    print("| Views | %s |" % f"{int(br.get('views',0)):,}")
    print("| AVD %% | %s%% %s |" % (avd, "🔴" if avd < 40 else "✅"))
    print("| Avg view duration | %ss |" % int(br.get("averageViewDuration", 0)))
    if biggest_drop:
        print("| Hook/biggest drop | giây %d→%d = %.1f%% |" % (
            biggest_drop[0], biggest_drop[1], biggest_drop[2] * 100))
    print("| CTR | [Studio — API không có] |")
    print("\n(retention curve %d điểm — paste vào retro.md, classify comment riêng)" % len(curve))


def update_truth(digest):
    if not os.path.exists(TRUTH_FILE):
        return
    txt = open(TRUTH_FILE, encoding="utf-8").read()
    b = digest["baseline"]
    iso = datetime.date.fromisoformat(digest["date_range"]["end"]).isocalendar()
    week = "%d-W%02d" % (iso[0], iso[1])
    avd_flag = "🔴 Dưới target 40% — vấn đề #1" if b["avd_pct"] < 40 else "✅"
    ctr = b.get("ctr_pct")
    ctr_cell = ("**%s%%**" % ctr) if ctr is not None else "`[NHẬP TAY — Studio · tuần %s]`" % week
    ctr_status = "✅ nhập tay" if ctr is not None else "⚠️ API không expose CTR"
    tv = digest["top_videos"][0] if digest["top_videos"] else None
    block = (
        "<!-- DATA_TRUTH_START -->\n"
        "| Chỉ số | Giá trị | Trạng thái |\n"
        "|--------|---------|-----------|\n"
        "| AVD trung bình | **%s%%** | %s |\n"
        "| Avg view duration | %ss | — |\n"
        "| Views (28d) | %s | — |\n"
        "| Net subs (28d) | +%d (%d/-%d) | — |\n"
        "| CTR (28d) | %s | %s |\n\n"
        "**Top video:** %s — %s views, AVD %s%%\n\n"
        "**Date range:** %s → %s · **Fetched:** %s (auto sync).\n"
        "<!-- DATA_TRUTH_END -->"
    ) % (
        b["avd_pct"], avd_flag, b["avg_view_duration_s"], f"{b['views_28d']:,}",
        b["subs_net"], b["subs_gained"], b["subs_lost"], ctr_cell, ctr_status,
        (tv["title"][:55] if tv else "—"), (f"{tv['views']:,}" if tv else "—"), (tv["avd_pct"] if tv else "—"),
        digest["date_range"]["start"], digest["date_range"]["end"], digest["fetched_at"][:10],
    )
    new = re.sub(r"<!-- DATA_TRUTH_START -->.*?<!-- DATA_TRUTH_END -->", lambda m: block, txt, flags=re.DOTALL)
    open(TRUTH_FILE, "w", encoding="utf-8").write(new)


def cmd_update_truth(json_path):
    """Cập nhật channel-truth DATA TRUTH từ JSON benchmark có sẵn (không fetch lại).
    Dùng bởi routine garden-us-60k-weekly-benchmark sau khi nó đã fetch."""
    if not os.path.isabs(json_path):
        json_path = os.path.join(ROOT, json_path)
    j = json.load(open(json_path, encoding="utf-8"))
    ca = j.get("channel_analytics", {})
    tv = [{"title": v.get("title", v.get("video", "")),
           "views": int(v.get("views", 0)),
           "avd_pct": round(v.get("averageViewPercentage", 0), 1)}
          for v in j.get("top_5_ctr_videos", [])]
    digest = {
        "fetched_at": j.get("fetched_at", str(datetime.date.today())),
        "date_range": {"start": j["date_range"]["start"], "end": j["date_range"]["end"]},
        "baseline": {
            "views_28d": int(ca.get("views", 0)),
            "avg_view_duration_s": int(ca.get("averageViewDuration", 0)),
            "avd_pct": round(ca.get("averageViewPercentage", 0), 2),
            "subs_gained": int(ca.get("subscribersGained", 0)),
            "subs_lost": int(ca.get("subscribersLost", 0)),
            "subs_net": int(ca.get("subscribersGained", 0)) - int(ca.get("subscribersLost", 0)),
            "ctr_pct": j.get("manual_ctr_pct"),
        },
        "top_videos": tv,
    }
    update_truth(digest)
    b = digest["baseline"]
    print("UPDATE-TRUTH OK từ %s" % os.path.relpath(json_path, ROOT))
    print("  AVD %s%% | Views %s | Net subs +%d | CTR %s" % (
        b["avd_pct"], f"{b['views_28d']:,}", b["subs_net"],
        (str(b["ctr_pct"]) + "%") if b["ctr_pct"] is not None else "chưa nhập (Studio)"))


# ---------- health ----------
HEALTH_FILE = os.path.join(ROOT, "references", "channel-health-latest.json")

# Gộp insightTrafficSourceType thô của API về nhóm người đọc hiểu được.
TRAFFIC_GROUPS = {
    "browse": ("SUBSCRIBER", "YT_OTHER_PAGE"),
    "suggested": ("RELATED_VIDEO", "END_SCREEN"),
    "search": ("YT_SEARCH", "HASHTAGS"),
    "shorts": ("SHORTS",),
    "external": ("EXT_URL", "NO_LINK_EMBEDDED", "NO_LINK_OTHER"),
    "playlist": ("PLAYLIST", "YT_PLAYLIST_PAGE"),
    "notification": ("NOTIFICATION",),
}
DURATION_BANDS = ((180, 300, "3-5′"), (300, 480, "5-8′"), (480, 720, "8-12′"),
                  (720, 1200, "12-20′"), (1200, 2400, "20-40′"), (2400, 10 ** 9, "40′+"))

# Shorts tối đa 3 phút. Chúng loop nên averageViewPercentage vượt 100% và view không so
# được với long-form → phải tách, nếu trộn chung thì mọi thống kê độ dài đều sai lệch.
SHORT_MAX_S = 180


def _analytics_safe(access, **params):
    """Như analytics() nhưng trả None thay vì thoát — dùng cho vòng lặp per-video."""
    try:
        return analytics(access, **params)
    except (SystemExit, Exception):
        return None


def _traffic_shares(access, ds, de):
    """{nhóm: % view} cho khoảng ngày. None nếu API không trả dữ liệu."""
    j = _analytics_safe(access, ids="channel==MINE", startDate=ds, endDate=de,
                        dimensions="insightTrafficSourceType", metrics="views")
    if not j or not j.get("rows"):
        return None
    raw = {r[0]: int(r[1]) for r in j["rows"]}
    total = sum(raw.values()) or 1
    out = {}
    for group, keys in TRAFFIC_GROUPS.items():
        out[group] = round(100.0 * sum(raw.get(k, 0) for k in keys) / total, 1)
    known = sum(sum(raw.get(k, 0) for k in keys) for keys in TRAFFIC_GROUPS.values())
    out["other"] = round(100.0 * (total - known) / total, 1)
    return out


def cmd_health(weeks=8):
    access = get_access_token()
    end = datetime.date.today()
    days = weeks * 7
    start = end - datetime.timedelta(days=days)
    ds, de = str(start), str(end)

    # --- A. Xu hướng theo tuần (bucket ISO week) ---
    daily = _analytics_safe(access, ids="channel==MINE", startDate=ds, endDate=de,
                            dimensions="day", metrics="views,averageViewPercentage,averageViewDuration")
    buckets = {}
    for r in (daily or {}).get("rows", []):
        d = datetime.date.fromisoformat(r[0])
        iso = d.isocalendar()
        key = "%d-W%02d" % (iso[0], iso[1])
        b = buckets.setdefault(key, {"views": 0, "avp": [], "dur": []})
        b["views"] += int(r[1])
        b["avp"].append(float(r[2]))
        b["dur"].append(float(r[3]))
    weekly = [{"week": k, "views": v["views"],
               "avd_pct": round(statistics.mean(v["avp"]), 1) if v["avp"] else None,
               "avg_dur_s": int(statistics.mean(v["dur"])) if v["dur"] else None}
              for k, v in sorted(buckets.items())]

    avd_series = [w["avd_pct"] for w in weekly if w["avd_pct"] is not None]
    avd_trend = None
    if len(avd_series) >= 3:
        cur = avd_series[-1]
        med = round(statistics.median(avd_series[:-1]), 1)
        delta = round(cur - med, 1)
        avd_trend = {"current": cur, "median_prior_weeks": med, "delta_pts": delta,
                     "direction": "down" if delta <= -1 else ("up" if delta >= 1 else "flat")}

    # --- B. Traffic mix: 28 ngày gần nhất vs 28 ngày trước đó ---
    cur_end, cur_start = end, end - datetime.timedelta(days=28)
    prv_end, prv_start = cur_start - datetime.timedelta(days=1), cur_start - datetime.timedelta(days=29)
    cur_mix = _traffic_shares(access, str(cur_start), str(cur_end))
    prv_mix = _traffic_shares(access, str(prv_start), str(prv_end))
    mix_delta = None
    if cur_mix and prv_mix:
        mix_delta = {k: round(cur_mix[k] - prv_mix.get(k, 0), 1) for k in cur_mix}

    # --- C. Bảng video trong cửa sổ ---
    vj = _analytics_safe(access, ids="channel==MINE", startDate=ds, endDate=de,
                         dimensions="video", metrics="views,averageViewPercentage,averageViewDuration",
                         sort="-views", maxResults=50)
    vcols = [c["name"] for c in vj["columnHeaders"]] if vj else []
    vrows = (vj or {}).get("rows", [])
    ids = [r[vcols.index("video")] for r in vrows]
    meta = video_meta(access, ids) if ids else {}
    videos = []
    for r in vrows:
        d = dict(zip(vcols, r))
        vid = d["video"]
        m = meta.get(vid, {})
        dur = m.get("dur", 0)
        avd = round(d["averageViewPercentage"], 1)
        avg_dur = int(d["averageViewDuration"])
        # Hỏi bằng OAuth chủ kênh (xem video_meta) nên video private VẪN trả metadata.
        # Vắng mặt = đã xoá hẳn, không còn khôi phục được thông tin gì ngoài số Analytics.
        privacy = m.get("privacy", "deleted") if m else "deleted"
        # AVD >100% chỉ xảy ra khi người xem lặp lại => chữ ký Shorts. Với video đã xoá
        # (không có duration), dùng avg_dur làm proxy: xem trung bình <=60s gần như chắc là Shorts.
        is_short = (0 < dur <= SHORT_MAX_S) or avd > 100 or (not m and avg_dur <= 60)
        videos.append({
            "videoId": vid, "title": m.get("title", vid), "published": m.get("published"),
            "duration_s": dur, "is_short": is_short, "privacy": privacy,
            "available": privacy == "public",
            "views": int(d["views"]), "avd_pct": avd, "avg_dur_s": avg_dur,
        })

    # Tách Shorts + video không còn công khai khỏi long-form TRƯỚC mọi thống kê. Trộn chung thì
    # band độ dài và outlier ratio đều vô nghĩa (Shorts loop => AVD >100%, view khác thang đo;
    # video đã ẩn/xoá thì không rút được bài học nào cho video sắp làm).
    longform = [v for v in videos if not v["is_short"] and v["available"]]
    shorts = [v for v in videos if v["is_short"]]
    private = [v for v in videos if v["privacy"] == "private"]
    deleted = [v for v in videos if v["privacy"] == "deleted"]

    # --- D. Outlier ratio (bao nhiêu % video LONG-FORM đạt >=3x median view của CHÍNH kênh) ---
    outliers = None
    if len(longform) >= 3:
        med_views = statistics.median(v["views"] for v in longform)
        hits = [v for v in longform if med_views and v["views"] >= 3 * med_views]
        outliers = {
            "scope": "long-form only",
            "median_views": int(med_views),
            "count_3x": len(hits), "total": len(longform),
            "ratio_3x_pct": round(100.0 * len(hits) / len(longform), 1),
            "top": [{"title": v["title"][:60], "views": v["views"], "avd_pct": v["avd_pct"],
                     "duration_s": v["duration_s"],
                     "multiple": round(v["views"] / med_views, 1) if med_views else None}
                    for v in longform[:5]],
        }

    # --- E. Duration band: độ dài nào thực sự ăn view trên CHÍNH kênh này (long-form) ---
    bands = []
    for lo, hi, label in DURATION_BANDS:
        grp = [v for v in longform if lo <= v["duration_s"] < hi]
        if grp:
            bands.append({"band": label, "n": len(grp),
                          "median_views": int(statistics.median(v["views"] for v in grp)),
                          "median_avd_pct": round(statistics.median(v["avd_pct"] for v in grp), 1)})

    shorts_summary = None
    if shorts:
        shorts_summary = {"n": len(shorts),
                          "median_views": int(statistics.median(v["views"] for v in shorts)),
                          "_note": "avd_pct cua Shorts co the >100% do loop — khong so voi long-form."}
    excluded = {"shorts": len(shorts), "private": len(private), "deleted": len(deleted),
                "counted_longform": len(longform), "total_from_api": len(videos),
                "views_lost_to_removed": sum(v["views"] for v in private + deleted)}

    # Catalog cũ vs video mới. Mọi chỉ số TRUNG BÌNH CẤP KÊNH (CTR, AVD tổng) là trung bình CÓ
    # TRỌNG SỐ — nếu catalog cũ chiếm phần lớn view thì các số đó mô tả catalog cũ, KHÔNG mô tả
    # video mới đăng. Bỏ qua điều này sẽ chấm "khỏe" cho một trục đang hỏng.
    old = [v for v in longform if v["published"] and v["published"] < ds]
    new = [v for v in longform if v["published"] and v["published"] >= ds]
    vo, vn = sum(v["views"] for v in old), sum(v["views"] for v in new)
    catalog_split = {
        "old_videos": len(old), "old_views": vo,
        "new_videos": len(new), "new_views": vn,
        "old_share_pct": round(100.0 * vo / (vo + vn), 1) if (vo + vn) else None,
        "channel_avg_represents": "catalog cũ" if (vo + vn) and vo / (vo + vn) > 0.7 else "hỗn hợp",
        "_warn": "old_share_pct cao => CTR/AVD trung binh cap kenh KHONG mo ta video moi. "
                 "Phai lay CTR tung video tu Studio truoc khi cham truc Dong goi.",
    }

    # --- F. Early velocity: view 5 ngày đầu của các video long-form mới nhất ---
    recent = sorted([v for v in longform if v["published"]], key=lambda v: v["published"], reverse=True)[:8]
    early = []
    for v in recent:
        pub = datetime.date.fromisoformat(v["published"])
        win_end = pub + datetime.timedelta(days=4)
        partial = win_end > end
        j = _analytics_safe(access, ids="channel==MINE", startDate=str(pub),
                            endDate=str(min(win_end, end)), dimensions="day",
                            filters="video==" + v["videoId"], metrics="views")
        if j is None:
            continue
        early.append({"videoId": v["videoId"], "title": v["title"][:60], "published": v["published"],
                      "views_5d": sum(int(r[1]) for r in j.get("rows", [])), "partial": partial})
    complete = [e["views_5d"] for e in early if not e["partial"]]

    digest = {
        "fetched_at": _utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "channel_slug": SLUG,
        "window": {"start": ds, "end": de, "weeks": weeks},
        "weekly_trend": weekly,
        "avd_trend": avd_trend,
        "watch_budget_s": int(statistics.median(w["avg_dur_s"] for w in weekly if w["avg_dur_s"])) if weekly else None,
        "traffic_mix": {"current_28d": cur_mix, "previous_28d": prv_mix, "delta_pts": mix_delta},
        "outliers": outliers,
        "duration_bands": bands,
        "shorts": shorts_summary,
        "excluded": excluded,
        "catalog_split": catalog_split,
        "early_velocity": {"scope": "long-form only", "videos": early,
                           "median_5d_views": int(statistics.median(complete)) if complete else None},
        "videos": videos,
        "_note": "SELF-BASELINE. Moc so sanh la chinh kenh ky truoc, KHONG phai nguong pho quat. "
                 "Shorts (<=180s) da tach khoi outliers/duration_bands/early_velocity. CTR khong co trong API.",
    }
    json.dump(digest, open(HEALTH_FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    print("HEALTH OK  %s -> %s (%d tuần)" % (ds, de, weeks))
    if avd_trend:
        arrow = {"down": "🔴 ↓", "up": "✅ ↑", "flat": "→"}[avd_trend["direction"]]
        print("  AVD tuần mới nhất %.1f%% vs median %d tuần trước %.1f%%  %s (%+.1f điểm)" % (
            avd_trend["current"], len(avd_series) - 1, avd_trend["median_prior_weeks"],
            arrow, avd_trend["delta_pts"]))
    if outliers:
        print("  Outlier ≥3× median: %d/%d video long-form (%.1f%%) | median view/video %s" % (
            outliers["count_3x"], outliers["total"], outliers["ratio_3x_pct"],
            f"{outliers['median_views']:,}"))
    if shorts or private or deleted:
        print("  (loại khỏi long-form: %d Shorts, trong đó %d private + %d đã xoá — còn %d/%d)" % (
            len(shorts), len(private), len(deleted), len(longform), len(videos)))
    if private or deleted:
        print("  ⚠️ %d video không còn công khai, mất %s view khỏi cửa sổ — kiểm tra xem có chủ ý không" % (
            len(private) + len(deleted), f"{excluded['views_lost_to_removed']:,}"))
    if cur_mix and mix_delta:
        print("  Traffic 28d: " + " · ".join(
            "%s %.1f%% (%+.1f)" % (k, cur_mix[k], mix_delta[k])
            for k in ("browse", "suggested", "search", "shorts") if cur_mix.get(k)))
    if bands:
        best = max(bands, key=lambda b: b["median_views"])
        print("  Band ăn view nhất: %s (n=%d, median %s view, AVD %.1f%%)" % (
            best["band"], best["n"], f"{best['median_views']:,}", best["median_avd_pct"]))
    ev = digest["early_velocity"]["median_5d_views"]
    print("  Median view 5 ngày đầu: %s" % (f"{ev:,}" if ev else "[chưa đủ video hoàn tất 5 ngày]"))
    cs = catalog_split
    if cs["old_share_pct"] is not None:
        print("  Catalog: %d video cũ giữ %.1f%% view · %d video mới trong cửa sổ chỉ %.1f%%" % (
            cs["old_videos"], cs["old_share_pct"], cs["new_videos"], 100 - cs["old_share_pct"]))
        if cs["old_share_pct"] > 70:
            print("  🔴 CTR/AVD trung bình cấp kênh đang mô tả CATALOG CŨ, không phải video mới.")
            print("     Muốn chấm trục Đóng gói phải lấy CTR TỪNG VIDEO mới từ Studio.")
    print("  -> %s" % os.path.relpath(HEALTH_FILE, ROOT))
    print("  ⚠️ CTR vẫn phải nhập tay từ Studio — API không expose.")


if __name__ == "__main__":
    cmds = ("sync", "retro", "update-truth", "health")
    if len(sys.argv) < 2 or sys.argv[1] not in cmds:
        sys.exit(__doc__)
    if sys.argv[1] == "sync":
        cmd_sync()
    elif sys.argv[1] == "health":
        cmd_health(int(sys.argv[2]) if len(sys.argv) > 2 else 8)
    elif sys.argv[1] == "update-truth":
        path = sys.argv[2] if len(sys.argv) > 2 else STATS_JSON
        cmd_update_truth(path)
    else:
        if len(sys.argv) < 3:
            sys.exit("Cần videoId: python tools/yt_analytics.py retro <videoId>")
        cmd_retro(sys.argv[2])
