"""Vá G062_auto (đã sửa tay trong CapCut; CapCut phải ĐÓNG; sao lưu trước):
 - viết lại 3 track chữ A / B / SRC theo danh sách từ khóa chọn lọc (bỏ NEW HAMPSHIRE, thưa ILLINOIS, kéo dài nhãn nguồn);
 - thêm track 'SFX TEXT': mỗi hiệu ứng chữ (A, B, SRC, thẻ đếm) có 1 SFX từ 2 mẫu người dùng đã thêm (Woosh, 挥动);
 - gỡ 2 đoạn SFX mẫu ở cuối timeline (vật liệu giữ lại để nhân bản).
Chạy: python -X utf8 -I tools/patch_text_sfx_062.py [--dry]"""
import copy, json, os, shutil, sys, uuid

DRY = '--dry' in sys.argv
D = r'D:\Capcut draft\CapCut Drafts\G062_auto'
BAK = r'D:\Capcut draft\CapCut Drafts\G062_auto_bak_before_text_sfx'
US = 1_000_000
uid = lambda: str(uuid.uuid4()).upper()
us = lambda x: int(round(x * US))

if os.path.exists(os.path.join(D, '.locked')):
    raise SystemExit('CapCut đang mở (.locked)')
p_main = os.path.join(D, 'draft_content.json')
tl = [x for x in os.listdir(os.path.join(D, 'Timelines')) if os.path.isdir(os.path.join(D, 'Timelines', x))][0]
p_tl = os.path.join(D, 'Timelines', tl, 'draft_content.json')
d = json.load(open(p_main, encoding='utf-8'))
mats = {}
for ln, arr in d['materials'].items():
    if isinstance(arr, list):
        for m in arr:
            if isinstance(m, dict) and 'id' in m:
                mats[m['id']] = (ln, m)
tracks = d['tracks']
byname = {t.get('name'): t for t in tracks if t.get('name')}

# ---- nội dung chữ (giây, chữ, thời lượng) ----
A = [(3.9, '6-8 HOURS', 3.0), (36.8, 'THE QUIET SIGN', 2.6), (117.3, 'THE QUIET SIGN', 2.6),
     (175.5, '6-8 HOURS', 2.8), (310.0, '1-2 MORE HARVESTS', 2.8), (359.0, '~4 WEEKS', 2.8),
     (413.9, '3/7', 2.6), (437.5, '10-12 WEEKS', 2.8), (507.8, 'NO LIGHT DATA', 2.8), (550.2, 'TINY TIM: 12-15 IN', 2.8),
     (646.1, '~10 WEEKS', 2.8), (719.9, '7-21 DAYS', 2.6), (726.5, '21-40 DAYS', 2.6), (754.2, '6-8 HOURS', 2.8),
     (908.2, '6 HOURS DARK', 2.8), (940.3, '3 PROBLEMS', 2.8), (1045.8, '7-21 DAYS', 2.6), (1051.8, '~4 WEEKS', 2.6),
     (1058.9, '10-12 WEEKS', 2.6), (1066.4, 'SUN or NO SUN', 2.8), (1073.3, '6-8 HOURS', 2.8)]
B = [(8.5, 'DECEMBER WINDOW'), (19.9, 'PALE & STRETCHED'), (38.6, 'WINDOW NOT ENOUGH'), (64.8, 'UNIVERSITY EXTENSIONS'),
     (82.0, 'WEAK WINTER SUN'), (93.8, 'WEAK LIGHT = STRETCH'), (185.7, 'COOL WHITE FLUORESCENT'), (198.9, 'LEAFY vs FRUITING'),
     (213.6, 'NEEDS DARK NIGHTS'), (242.9, 'SOW THICKLY'), (249.8, 'CUT AT TRUE LEAVES'), (256.3, 'KEEP TRAY COVERED'),
     (271.1, '16 HOURS TOTAL'), (278.0, 'TRY THE WINDOW FIRST'), (284.5, 'SHALLOW TRAY'), (303.7, 'BABY GREENS'),
     (317.2, 'CUT & REGROW'), (331.1, 'WEAK LIGHT OK'), (362.5, 'FIRST CRISP BITE'), (483.6, 'SOURCES GO QUIET'),
     (520.7, 'TEST ONE POT'), (663.1, 'WARM + BRIGHT'), (840.1, '14-16 HOURS A DAY'), (861.0, 'LED USES LESS ENERGY'),
     (877.5, 'LET THE PLANT GUIDE YOU'), (888.0, 'USE A TIMER'), (900.8, '16 HOURS, MAX 18'), (915.0, '2 HRS LAMP : 1 HR SUN'),
     (928.6, 'NO PRICES'), (960.5, 'GENTLE FAN'), (980.4, 'SOAP FOR APHIDS'), (998.3, 'PETS: CHECK ASPCA'),
     (1080.2, 'FRESH IN WINTER'), (1093.5, 'GARDENER FORECAST'), (1107.0, 'GROW A LITTLE')]
B = [(t, x, 2.6) for t, x in B]
SRC = [(0.1, 'ILLINOIS EXTENSION'), (147.5, 'ILLINOIS EXTENSION'), (181.9, 'UTAH STATE EXTENSION'),
       (232.1, 'MARYLAND EXTENSION'), (584.4, 'UTAH STATE EXTENSION'), (809.1, 'PENN STATE EXTENSION'),
       (833.5, 'ILLINOIS EXTENSION')]
SRC = [(t, x, 4.0) for t, x in SRC]


def clone_text_seg(tmpl, start, dur, text):
    seg = copy.deepcopy(tmpl)
    ln, tm = mats[tmpl['material_id']]
    nm = copy.deepcopy(tm)
    nm['id'] = uid()
    c = json.loads(nm['content'])
    c['text'] = text
    for st in c['styles']:
        st['range'] = [0, len(text)]
    nm['content'] = json.dumps(c, ensure_ascii=False, separators=(',', ':'))
    for k in ('base_content', 'words'):
        if k in nm and isinstance(nm[k], str) and k == 'base_content':
            pass
    d['materials'][ln].append(nm)
    refs = []
    for rid in tmpl.get('extra_material_refs', []):
        l2, m2 = mats[rid]
        m3 = copy.deepcopy(m2)
        m3['id'] = uid()
        d['materials'][l2].append(m3)
        refs.append(m3['id'])
    seg.update({'id': uid(), 'material_id': nm['id'], 'extra_material_refs': refs,
                'target_timerange': {'start': us(start), 'duration': us(dur)}})
    return seg


events = []   # (t, kind) para SFX
for name, items, kind in (('TEXT A', A, 'A'), ('TEXT B', B, 'B'), ('TEXT SRC', SRC, 'SRC')):
    tr = byname[name]
    tmpl = tr['segments'][0]
    tr['segments'] = [clone_text_seg(tmpl, t, du, x) for t, x, du in items]
    events += [(t, kind) for t, x, du in items]

# thẻ đếm (png) trên track video thứ 2
counter = [t for t in tracks if t['type'] == 'video'][1]
events += [(s['target_timerange']['start'] / US, 'CNT') for s in counter['segments']]

# ---- SFX ----
aud = [t for t in tracks if t['type'] == 'audio' and not t.get('name')]
sfx_tr = aud[0]
woosh_seg = next(s for s in sfx_tr['segments'] if mats[s['material_id']][1].get('name') == 'Woosh')
swing_seg = next(s for s in sfx_tr['segments'] if mats[s['material_id']][1].get('name', '').startswith('挥动'))


def clone_sfx(base, t, vol):
    seg = copy.deepcopy(base)
    refs = []
    for rid in base.get('extra_material_refs', []):
        ln, m = mats[rid]
        c = copy.deepcopy(m)
        c['id'] = uid()
        d['materials'][ln].append(c)
        refs.append(c['id'])
    dur = base['source_timerange']['duration']
    seg.update({'id': uid(), 'extra_material_refs': refs, 'volume': vol,
                'target_timerange': {'start': us(max(t, 0)), 'duration': dur}})
    return seg


# A (số liệu lớn) -> Woosh đủ rõ; SRC (nhãn nguồn) -> swing vừa; thẻ đếm -> Woosh; B (phụ) -> swing nhỏ
plan = {'A': (woosh_seg, 0.55, -0.05), 'CNT': (woosh_seg, 0.5, -0.05), 'SRC': (swing_seg, 0.35, 0.0), 'B': (swing_seg, 0.2, 0.0)}
sfx_segs = []
for t, k in sorted(events):
    base, vol, off = plan[k]
    sfx_segs.append(clone_sfx(base, t + off, vol))
new_tr = copy.deepcopy(sfx_tr)
new_tr['id'] = uid()
new_tr['name'] = 'SFX TEXT'
new_tr['segments'] = sfx_segs
# gỡ track mẫu ở cuối timeline, thêm track SFX mới
tracks.remove(sfx_tr)
tracks.append(new_tr)
import collections
print('SFX theo loại:', dict(collections.Counter(k for _, k in events)), '| tổng', len(sfx_segs))
print('chữ: A', len(A), '| B', len(B), '| SRC', len(SRC))
# kiểm chồng chéo trong track SFX (CapCut yêu cầu segment cùng track không chồng nhau)
sfx_segs.sort(key=lambda s: s['target_timerange']['start'])
bad = [(a['target_timerange']['start'] / US) for a, b in zip(sfx_segs, sfx_segs[1:])
       if a['target_timerange']['start'] + a['target_timerange']['duration'] > b['target_timerange']['start']]
print('chồng chéo:', bad)
if bad:
    # tách ra track phụ
    keep, over = [], []
    end = -1
    for s in sfx_segs:
        st = s['target_timerange']['start']
        if st >= end:
            keep.append(s)
            end = st + s['target_timerange']['duration']
        else:
            over.append(s)
    new_tr['segments'] = keep
    t2 = copy.deepcopy(new_tr)
    t2['id'] = uid()
    t2['name'] = 'SFX TEXT 2'
    t2['segments'] = over
    tracks.append(t2)
    print('đã tách', len(over), 'segment sang SFX TEXT 2')
end = max(s['target_timerange']['start'] + s['target_timerange']['duration'] for t in tracks if t.get('type') in ('video', 'audio', 'text') for s in t['segments'])
d['duration'] = end
print('độ dài: %.2fs' % (end / US))
if DRY:
    print('dry run: chưa ghi')
    sys.exit(0)
if os.path.exists(BAK):
    raise SystemExit('đã có sao lưu ' + BAK)
shutil.copytree(D, BAK)
for p in (p_main, p_tl):
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
mp = os.path.join(D, 'draft_meta_info.json')
meta = json.load(open(mp, encoding='utf-8'))
meta['tm_duration'] = end
json.dump(meta, open(mp, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('ĐÃ VÁ', D, '| sao lưu:', BAK)
