# Prediction — big-idea-098-amish-no-till-fall

> Ghi tại GATE Script (18/11/2026). 7–14 ngày sau khi đăng, so với số thật trong `retro.md`.
> **Chấm chính:** views_5d so với trung vị 597 (`channel.config.json` → `scoring`) + giây xem/lượt + CTR Studio. ⛔ Không chấm bằng AVD% đơn lẻ.

| Trường | Giá trị |
|--------|---------|
| Video | big-idea-098-amish-no-till-fall |
| **Hạng** | **AN TOÀN** (Topic Gate 2/3 · GO-TEST · không phải cú đánh lớn) · **TEST** (xem dưới) |
| Ngày scripted | 2026-11-18 (user duyệt script + hook A′) |
| Target publish | **~12–19/12/2026** (user chọn «chen giữa tháng 12»). Ràng buộc: cách 096 (~30/11–07/12) ≥ 5 ngày · trước 097 (12–16/01). Mùa: lá rụng xong, dọn vườn thu; đăng muộn hơn 20/12 thì phần «phân trước cuối tháng 11» đã trễ cho xà lách tháng 4 — script nói theo cách đếm lùi nên vẫn dùng được, nhưng giảm tính «làm ngay» |
| Compliance score (lúc GATE) | **8/10** (R2 Opus, vòng 2 — Fail §3 Pet/Kid, §8 Hedging) → đã sửa 4 câu sau vòng 2, **chưa chấm lại** (ước 9–10). Agy lỗi 3 lần → cả 2 vòng là 2 Opus, **cùng hãng** |
| Độ dài | 1.885 từ ≈ 11,4′ @165 wpm (khung 10–14′) |

## Title bet
- **Title chốt:** `4 Amish Fall Garden Habits That Beat a Rototiller` (user chọn Title A 18/11; vidIQ không chấm — tool không có)
- Specific quantity? **Y** («4»)
- Leading number? **Y**
- Keyword-first: **Y** — «Amish» ở ký tự thứ 3 (`amish gardening` ~31K/th US)
- Độ dài: **8 từ / 49 ký tự**
- Thumbnail test: `LEAVES ✅` vs máy xới ❌ (bổ trợ: thứ thay máy là lá rụng miễn phí) — chi tiết `thumbnail-prompts.md`.

## Retention bets (3 luật cứng)
- **Topic familiarity:** **Y** — máy xới, phân chuồng, lá rụng: quen với mọi người làm vườn Mỹ. Rủi ro khác: chủ đề **chuẩn bị đất**, không phải «trồng/nhân MỘT cây» (lệch thông số vàng W41 ②③).
- **Giây 40–55:** Loop #1 «một vườn nên xới đúng một lần — có thể là vườn bạn» (gieo ~0:32) + M1 «the real work happens in fall» + sự thật «Amish vẫn cày bằng ngựa» (khác 2 đối thủ). ⚠️ Hook A′ ~0:44, dài hơn A ~8 s.
- **Phút 4–6:** Loop #2 «một ngày trên lịch quyết định phân có an toàn cho xà lách» (3:15 → 4:50) + **Editorial Signature = Timing Wall** (đếm lùi 120 ngày) + re-tease Loop #1 ~5:05. Jenga Retention: **ON** (3 loop, ≤2 chồng).

## Engagement bets
- Themes: ☐ Nostalgia (chỉ «horse-era» — không có chuyện ông bà) · ☑ Pet/kid safety (không dùng phân heo/chó/mèo; giữ thú cưng ra khỏi vườn rau; rửa tay cả tay trẻ) · ☑ USDA zone/climate (rye sống tới zone 3; mốc phủ lá)
- Câu kích theme: «What zone are you in, and when do your leaves usually come down? Tell me in the comments.»

## Dự đoán số (so baseline kênh)
| Chỉ số | Baseline kênh | DỰ ĐOÁN video này |
|--------|---------------|-------------------|
| views_5d | trung vị 597 · an toàn ≥896 · bứt ≥2.982 | **P25 ~350 · P50 ~600 · P75 ~1.200** (ước tay, chưa qua `chi_so.py`). **P(≥896) ≈ 0,28 · P(≥2.982) ≈ 0,05** |
| AVD % | 25,6% (video 7–9′: 27–35%; ≥16′: 12–15%) | **~25%** (11′, listicle 4 mục, phần phân chuồng dày số) — phán đoán |
| CTR % (giờ 48) | video mới 10/10–07/11 1,3–1,6% | **≥2,5%** — có keyword «Amish gardening» mạnh (31K/th) + số dẫn đầu |
| Giây xem/lượt | watch-budget kênh ~195 s | **≥170 s** |

> Căn cứ: (1) outlier ngách Backyard Bill «Why Amish Farmers Never Rototill» 328K (60×) · Rooted Grace «No-Till Forever» 482K — nhưng cả hai dùng khung «họ giấu / never», kênh mình không dùng; (2) Frugal Solutions (Model Link): video Amish làm vườn 11K–127K ở kênh 272K sub, kênh mình nhỏ hơn nhiều; (3) 3 dự báo trước đều cao hơn thực (P50 1.110/1.085/919 → thực 649/316/290) → giảm P50 về ~trung vị; (4) ① kênh mình = 0 (chưa có hit Amish/đất).

## TEST (ghi rõ để retro trả lời)
1. **TEST BÁM MODEL LINK (Frugal Solutions) — đề tài Amish:** video bám thứ 4 (095 · 096 · 097 chưa đăng). Mốc thôi bám: 3 video bám đầu tiên không có video nào ≥896 views_5d. Retro ghi rõ thứ tự đăng thực tế.
2. **TEST KEYWORD «Amish» (KEYWORD-FIRST):** traffic Search có vượt Browse không? So % Search của video này với 095/096. Nếu Search ≥20% → keyword Amish kéo được, làm thêm 1 video Amish khác chủ đề.
3. **TEST CHỦ ĐỀ ĐẤT (lệch thông số vàng):** chuẩn bị đất mùa thu (không phải nhân/trồng một cây) có giữ ≥ trung vị không?
4. **TEST TRUNG THỰC «Amish vẫn cày»:** comment có ai cãi «Amish don't till» không, hay khen? Đếm comment nhắc ngựa/cày.
5. **TEST HOOK A′ (~0:44, dài hơn A):** cú rơi 0:20–0:45 có sâu hơn trung bình kênh không? So với 097 (hook ~0:33).
6. **TEST TIMING WALL (Editorial Signature ở phút 4–5):** đường cong phút 4–6 có phẳng hơn các video trước không?

## Quy tắc dừng
- views_5d < 400 **hoặc** CTR giờ 48 < 2% → gói hỏng: đổi thumbnail trước (biến thể B), rồi mới đổi title (giữ «Amish» ở đầu).
- views_5d ≥ 896 → đạt mức an toàn; làm tiếp «Amish spring garden» (gieo xuyên lớp phủ, rye) hoặc 1 đề Amish khác nếu Search ≥20%.
- views_5d ≥ 2.982 → làm phần tiếp ngay, giữ khung «N Amish … Habits That Beat a …».
