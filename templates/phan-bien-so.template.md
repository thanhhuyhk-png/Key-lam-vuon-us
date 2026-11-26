# Sổ phản biện — <big-idea-NNN-slug> · vòng <N>

> Bước 3R (thêm 2026-11-08). Orchestrator điền sau khi nhận 2 bản phản biện. Lưu tại `scripts/<tập>/phan-bien-vN.md`.
> Nguyên tắc: **nhận** lỗi có dẫn chứng (dòng C.. trong Claim Ledger, luật ACTIVE, số đo của `gate.py`);
> **bác** lỗi mà ledger / số đo chứng minh sai. Không nhận vì "nghe có lý", không bác vì "đã self-audit rồi".

## Nguồn
| Người phản biện | Model | Thư mục cách ly | Kết luận | Hook /35 |
|---|---|---|---|---|
| R1 Agy | <model> `--sandbox` | phan-bien-vN/agy/ | ĐẠT / ĐẠT CÓ SỬA / KHÔNG ĐẠT | |
| R2 Opus ngữ cảnh mới | opus | phan-bien-vN/opus/ | | |

Bản gốc: `phan-bien-vN/agy/agy-phan-bien.txt` · `phan-bien-vN/opus/opus-phan-bien.md`

## ✅ Đã nhận → danh sách quyết định biên tập
| # | Mức | Từ (R1/R2/cả hai) | Câu gốc @mm:ss | Quyết định sửa (câu mới hoặc hướng) | Căn cứ (C.. / L.. / gate) |
|---|---|---|---|---|---|
| D1 | CHẶN | | | | |

## ❌ Đã bác (kèm lý do)
| # | Từ | Lỗi người phản biện nêu | Vì sao bác (bằng chứng) | Báo nhầm lặp lại? |
|---|---|---|---|---|
| B1 | | | | có → ghi vào lessons-learned § Báo nhầm đã biết |

## Hai bên bắt gì khác nhau (ghi để chỉnh brief lần sau)
- R1 bắt mà R2 không: …
- R2 bắt mà R1 không: …

## Sau khi sửa
- Người biên tập: <model> · sửa theo D1…Dn, **chỉ sửa câu trong danh sách**, không viết lại đoạn khác.
- `gate.py` sau sửa: PASS / FAIL (dán dòng tổng kết).
- Vùng đã sửa (để vòng 2 soi): `phan-bien-v<N+1>/vung-da-sua.md`.
