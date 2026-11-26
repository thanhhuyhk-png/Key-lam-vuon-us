import json,re,sys
sys.path.insert(0,'../san-y-tuong-2026-10-24')
from parse import parse
def dur(s):
    m=re.match(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?',s or '')
    return sum(int(x or 0)*k for x,k in zip(m.groups(),(3600,60,1))) if m else 0
def build(files,keep,ten,nguon,dd,out):
    seen={};loai={'ngan':0,'kenh_lon':0,'lac_de':0,'khong_eng':0}
    for f in files:
        for r in parse(f):
            if r['id'] in seen: continue
            t=r['title'] or ''
            if dur(r['duration'])<240: loai['ngan']+=1; continue
            if (r['subscriberCount'] or 0)>188000: loai['kenh_lon']+=1; continue
            if not keep(t.lower()): loai['lac_de']+=1; continue
            if re.search(r'[^\x00-ɏ -⯿\U0001F000-\U0001FFFF]',t): loai['khong_eng']+=1; continue
            seen[r['id']]=dict(id=r['id'],title=t,channel_id=r['channelId'],channel_sub=r['subscriberCount'],views=r['viewCount'],om=r['outlierScore'],vph=r['vph'],published=r['publishedAt'][:10],dinh_dang=dd)
    d=dict(ngay_do='2026-10-26',nguon_mau=nguon+f' · loại trước khi đưa vào: {loai}',cach_sap=['relevance','date'],view_dien_hinh_toi_thieu=500,
      kenh_minh=dict(sub=62600,trung_vi_view=597,view_dien_hinh_uoc=None),moc_nganh_p50=None,he_so_kenh_moi=0.5,nguong_thang=1.5,nguong_om=2.0,he_so_khop=1.0,chi_phi=2,tuoi_toi_thieu_ngay=14,videos=list(seen.values()))
    json.dump(d,open(out,'w',encoding='utf-8'),ensure_ascii=False,indent=1); print(out,len(seen),loai)
build(['b-p1.json','b-p2.json','b-p3.json','b-p4.json','b-p5.json'],lambda t:('pepper' in t or 'chili' in t or 'overwinter' in t) and re.search(r'overwinter|winter|throw|alive|again|years|forever|revive|dig up|replant',t),'pepper',
 "vidiq_youtube_search (tk3) US 2025-10-26..2026-10-12: 'overwinter pepper plants' (relevance) + 'overwintering peppers indoors' (date) + 'how to keep pepper plants alive over winter' (relevance, medium) + 'bring pepper plants inside for winter' + 'cut back pepper plants dormant over winter save for next year' (relevance, medium); long-form ≥4′, kênh ≤188K (3× kênh mình), tiêu đề về giữ ớt qua đông",'giữ qua đông','mau-c1-pepper-overwinter.json')
build(['b-t1.json','b-t2.json','b-t3.json','b-t4.json','b-t5.json'],lambda t:re.search(r'brown|crispy|humidity|misting',t),'tips',
 "vidiq_youtube_search (tk3) US 2025-10-26..2026-10-12: 'brown tips on houseplant leaves' (relevance) + 'why do my plant leaves have brown tips' (date) + 'houseplant brown leaf tips winter dry air' + 'brown leaf tips houseplant fix' + 'why are my plant leaves turning brown' (relevance, medium); long-form ≥4′, kênh ≤188K, tiêu đề về lá nâu/cháy đầu/độ ẩm",'sửa lỗi','mau-c1-brown-tips.json')
