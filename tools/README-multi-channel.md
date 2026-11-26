# Onboard kênh mới — Checklist (Channel-Linked Pro)

> Hướng dẫn dựng pipeline tự động cho **một kênh YouTube mới** (vd US Team1, Japan).
> Thiết kế: **1 workspace = 1 kênh = 1 `channel.config.json`**. Tools đã config-driven nên
> phần lớn là plug-and-play; chỉ token OAuth + scheduled-task là per-kênh thật sự.

---

## TL;DR — 5 bước

| # | Bước | Plug-and-play? |
|---|------|----------------|
| 1 | Copy `tools/` vào workspace mới | ✅ |
| 2 | Tạo `channel.config.json` đúng slug | ✅ |
| 3 | Đặt token OAuth `.secrets/youtube-token-{slug}.json` | ⚙️ per-kênh |
| 4 | Tạo brand-voice file có markers `DATA_TRUTH` | ✅ |
| 5 | Clone scheduled-task benchmark weekly | ⚙️ per-kênh |

Sau đó: `python tools/yt_analytics.py sync` → nếu ra số là xong.

---

## Bước 1 — Copy tools

Copy nguyên thư mục `tools/` (gồm `yt_analytics.py`, `run-sync.cmd`, `notify-ctr.ps1`, file này) sang workspace kênh mới. Không cần sửa code — tự suy đường dẫn từ vị trí file.

## Bước 2 — channel.config.json

Đặt ở **gốc workspace**. Tối thiểu cần:

```json
{
  "channel_name": "US Team1",
  "youtube_channel_slug": "us-team1",
  "brand_voice_file": "references/channel-truth.md",
  "script_language": "English",
  "translate_es": false,
  "model_routing": {
    "default": "haiku",
    "steps": { "hook": "sonnet", "script": "sonnet", "script_audit": "sonnet" }
  }
}
```

> `youtube_channel_slug` quyết định tên file token + stats. `brand_voice_file` là nơi block
> DATA TRUTH được ghi đè. Tool đọc các giá trị này, **không** còn hardcode `garden-us-60k`.

## Bước 3 — Token OAuth (per-kênh)

Mỗi kênh là một tài khoản YouTube khác → cần token riêng:
`.secrets/youtube-token-{slug}.json` (vd `.secrets/youtube-token-us-team1.json`).

Scopes bắt buộc: `youtube.readonly` + `yt-analytics.readonly`.
Cấu trúc file (giống Garden US): `token`, `refresh_token`, `client_id`, `client_secret`, `token_uri`, `scopes`, `expiry`.

**Lấy token:** chạy OAuth flow của skill benchmark (gõ `benchmark {slug}` trong Claude Code, hoặc dùng script `fetch_channel_data.py` lần đầu — nó mở browser login). Token được cache lại, các lần sau tự refresh.

> ⚠️ `.secrets/` và `.env` PHẢI nằm trong `.gitignore`. KHÔNG commit / push Notion / sync ra ngoài.

## Bước 4 — Brand-voice file + markers

File mà `brand_voice_file` trỏ tới (vd `references/channel-truth.md`) phải chứa block:

```
<!-- DATA_TRUTH_START -->
... (tool sẽ ghi đè vùng này) ...
<!-- DATA_TRUTH_END -->
```

Nếu chưa có markers, `update-truth`/`sync` sẽ không chèn được số liệu. Copy `channel-truth.md`
của Garden US làm khung rồi sửa phần Voice cho đúng kênh mới.

## Bước 5 — Clone scheduled-task (per-kênh)

Routine weekly là 1 task/kênh với absolute path. Clone từ `garden-us-60k-weekly-benchmark`:
- Tên mới: vd `us-team1-weekly-benchmark`
- Sửa mọi `D:\...\<workspace Garden US>` → đường dẫn workspace kênh mới
- Sửa `--channel-slug` và path token sang slug mới
- Giữ nguyên Bước 3.5 (update-truth + toast) — đã config-driven nên chỉ cần đúng workspace path

---

## Kiểm tra (verification)

```bash
# Từ gốc workspace kênh mới:
python tools/yt_analytics.py sync          # ra baseline -> OK
python tools/yt_analytics.py retro <videoId>   # ra retention curve -> OK
tools\run-sync.cmd                         # sync + toast -> kiểm tra sync.log + balloon
```

Mở brand-voice file → block DATA TRUTH phải có số mới + dòng CTR.

---

## Vận hành hàng tuần (mọi kênh giống nhau)

1. Routine CN chạy → fetch + cập nhật channel-truth + **toast nhắc CTR**
2. Bạn: Studio → Reach → CTR (28d) → sửa `manual_ctr_pct` trong `references/channel-stats-{slug}.json` → `python tools/yt_analytics.py update-truth`

> CTR là thứ DUY NHẤT phải nhập tay — YouTube Analytics API không expose (đã verify).
> `sync` và `update-truth` đều giữ `manual_ctr_pct` đã nhập, không ghi đè mất.

---

## Troubleshooting

| Triệu chứng | Nguyên nhân | Cách xử |
|-------------|-------------|---------|
| `Refresh token FAILED` | token bị thu hồi/hết hạn vĩnh viễn | re-OAuth: gõ `benchmark {slug}` login lại |
| `Unknown identifier (impressions)` | (bình thường) API không có CTR | bỏ qua — nhập CTR tay |
| update-truth không đổi gì | thiếu markers `DATA_TRUTH` trong brand-voice file | thêm markers (Bước 4) |
| toast không hiện | session không tương tác (task chạy lúc không đăng nhập) | reminder vẫn nằm trong channel-truth + sync.log |
| `python` not found (scheduled task) | PATH context | dùng absolute python path trong task, hoặc thêm Python vào PATH hệ thống |

---

*Cập nhật: 2026-06-10 · Pipeline Channel-Linked Pro (Phase 1–4).*
