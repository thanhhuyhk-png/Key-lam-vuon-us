---
file: feedback-loop.md
role: Quy trình Phase 2 — vòng lặp tự học script→đăng→retention→audit
status: AUTO (Phase 4 OAuth Analytics đã wired — tools/yt_analytics.py)
created: 2026-06-10
---

# Feedback Loop — Garden US (Phase 2)

Biến pipeline **một chiều** (ý tưởng→script→đăng) thành **vòng lặp tự học**. Mỗi video mới
được audit dựa trên điều **thật sự đã thắng/thua**, không phải lý thuyết.

```
[GATE Script ─ Bước 3]
   └─► prediction.md         (ghi "cược": title pattern, open loop 40-55s, tension 4-6, AVD dự đoán)
          │  đăng video → chờ 7–14 ngày
          ▼
[Post-publish ─ Bước 6]
   └─► retro.md              (kéo AVD/CTR/retention từ Studio + comments → DIFF cược → LESSONS)
          │
          ├─► lessons-learned.md   (rollup 1 file → audit script kế tiếp ĐỌC)
          └─► channel-truth.md     (cập nhật DATA TRUTH + Reconciliation Log nếu rule đổi)
```

## Khi nào chạy bước nào

| Khi | Hành động | File | Ai làm |
|-----|-----------|------|--------|
| GATE Script approve | Tạo `prediction.md` từ template, điền cược | `scripts/{slug}/prediction.md` | orchestrator/user |
| 7–14 ngày sau publish | `python tools/yt_analytics.py retro <videoId>` → auto block ACTUAL (AVD + drop second) vào `retro.md`, rồi DIFF cược | `scripts/{slug}/retro.md` | tool + Claude diff |
| Ngay sau retro | Copy block LESSONS → rollup; update DATA TRUTH nếu cần | `lessons-learned.md`, `channel-truth.md` | Claude |
| Mỗi lần audit script MỚI | Đọc `lessons-learned.md` ACTIVE RULES, check script chống lặp sai lầm | — | `mkt-youtube-script-audit` |
| Hàng tuần (hoặc trước khi viết) | `python tools/yt_analytics.py sync` → refresh baseline + top videos vào `channel-truth.md` DATA TRUTH | `channel-truth.md`, `yt-analytics-latest.json` | tool |

## Token discipline
- Audit chỉ đọc block `## ✅ ACTIVE RULES` (~15 dòng), KHÔNG đọc từng retro.
- retro.md nặng (số liệu) nằm trong folder video, không nạp vào pipeline trừ khi đào sâu 1 video.
- Phần "pull" retention curve nặng → khi lên Phase 4, chạy trong sub-agent isolated, chỉ trả digest.

## Ranh giới manual vs auto (Phase 4 đã wired)
- ✅ **AUTO qua `tools/yt_analytics.py`** (OAuth, scopes youtube.readonly + yt-analytics.readonly): views, AVD, avg view duration, subs gained/lost, top videos, **retention curve giây-theo-giây** (biggest drop second auto-detect), titles.
- ⚠️ **Vẫn paste tay từ Studio:** **CTR thumbnail** — YouTube Analytics API KHÔNG expose. Nhập ở DATA TRUTH `[USER FILL]`.
- 🔑 **Token:** `.secrets/youtube-token-garden-us-60k.json` (gitignored). Tool tự refresh access token. Nếu refresh fail → liên kết lại kênh.

## Định nghĩa "diff thành công"
Một retro tốt trả lời được: **cược nào thắng (giữ làm rule), cược nào thua (thành lesson cấm)**.
Lesson lặp ở 2+ video → promote lên `channel-truth.md` thành luật kênh.
