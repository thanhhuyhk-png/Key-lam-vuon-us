# Prediction — big-idea-094-root-9-free-plants-water

> Ghi tại GATE Script (08/11/2026). 7–14 ngày sau khi đăng, so với số thật trong `retro.md`.
> **Chấm chính:** views_5d so với trung vị 597 (`channel.config.json` → `scoring`) + giây xem/lượt + CTR Studio. ⛔ Không chấm bằng AVD% đơn lẻ.

| Trường | Giá trị |
|--------|---------|
| Video | big-idea-094-root-9-free-plants-water |
| **Hạng** | **CÚ ĐÁNH LỚN** (`hang` = cu-danh-lon) |
| Ngày scripted | 2026-11-08 |
| Target publish | trước ~22/11/2026 (đợt sương giá lớn ở vùng 5–7; nhóm A mất tính "làm ngay" nếu đăng muộn) |
| Compliance score (lúc GATE) | 10/10 (R2 Opus, vòng 2) — gate.py tts-clean PASS |
| Độ dài | 1.781 từ ≈ 10,8′ @165 wpm (khung big_hit 10–14′) |

## Title bet
- **Title chốt:** `You're Throwing Away Free Plants: Root These 9 in a Glass of Water` (vidIQ 92)
- Specific quantity? **Y** ("9", "a glass of water")
- Leading number? **N**. Mở bằng "You're Throwing Away" (DNA "thứ đang vứt đi" ×2,1). Số đứng giữa title.
- Độ dài: **13 từ / 66 ký tự**
- Thumbnail test: A `BEFORE THE FROST` vs B `$0 BY SPRING` (Test & Compare). C `JUST 1 LEAF` để dự phòng.

## Retention bets
- **Topic familiarity:** **Y**. 9 cây phổ biến ở Mỹ, nối hit 985K (cây trong nước) và 182K (giâm cành).
- **Giây 40–55:** Loop #1 "one sign you can see through the glass" (mở ~0:38) → đóng ở đoạn chuyển sang đất (~9:00). Nhắc lại ở 3:10 và 6:40.
- **Phút 4–6:** Loop #2 "the last plant… turns one single leaf into a whole new plant" mở ~4:45 → đóng ~8:10. Cảnh viewer-POV sau đêm sương giá (mục 4). Chuyển nhóm porch → trong nhà ở ~5:40 có re-hook "if you don't have a garden to clean up… this next part is for you". Jenga: **ON** (2 loop chồng nhau).

## Engagement bets
- Themes: ☐ Nostalgia · ☑ Pet safety (ASPCA: coleus/begonia/arrowhead độc; 5 cây không độc) · ☑ USDA zone/frost
- Câu kích theme: "What zone are you gardening in, and when does your first frost usually hit?" · "Glass up high, where paws and curious noses can't reach."

## Dự đoán số (so baseline kênh)
| Chỉ số | Baseline kênh | DỰ ĐOÁN video này |
|--------|---------------|-------------------|
| views_5d | trung vị 597 · an toàn ≥896 · bứt ≥2.982 | **P50 ~1.200 · P25 ~600 · P75 ~3.000**. Cược: qua mức an toàn; xác suất chạm mức bứt ~25% |
| AVD % | 25,6% (video 7–9′: 27–35%; ≥16′: 12–15%) | **~30%** (10,8′, listicle có 2 loop) |
| CTR % (giờ 48) | 28d 5,5% · video mới 10/10–07/11 1,3–1,6% | **≥3,5%** (gói "đồ đang vứt" + thumbnail biến đổi) |
| Giây xem/lượt | watch-budget kênh ~195 s | **≥190 s** |

> Các số P25/P50/P75 là phán đoán, không do mô hình tính. Phiếu san-y-tuong vòng B (C1) chưa chạy (còn 30 credit trần) → chưa có dòng p_thang trong `research/du-bao.csv`.

## TEST (ghi rõ để retro trả lời)
1. **TEST ĐỘ DÀI:** big_hit 10–14′ thay cho 20–24′. Câu hỏi retro: giây xem/lượt và tổng giờ xem có hơn 093 (16:57) không?
2. **TEST KHUNG "thứ đang vứt đi" (DNA ×2,1):** CTR giờ 48 có thoát mức 1,3–1,6% của 8 video mới không?
3. **TEST LISTICLE ĐẾM XUÔI + 2 LOOP:** đường cong có rơi mạnh ở ranh giới giữa các mục, hay ở 4–6′?
4. **TEST THUMBNAIL A/B:** `BEFORE THE FROST` (thời gian) vs `$0 BY SPRING` (tiền).

## Quy tắc dừng
- views_5d < 500 **hoặc** CTR giờ 48 < 3% → gói hỏng: đổi thumbnail sang C `JUST 1 LEAF` trước, rồi mới đổi title.
- views_5d ≥ 2.982 → làm phần tiếp ngay (giâm lá / cây cảnh trong nhà mùa đông), giữ nguyên khung gói.
