import json,re
from parse import parse
def dur(s):
    m=re.match(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?',s or '')
    return sum(int(x or 0)*k for x,k in zip(m.groups(),(3600,60,1))) if m else 0
def build(files,keep,nguon,dd,out):
    seen={};loai={'ngan':0,'kenh_lon':0,'lac_de':0,'khong_eng':0}
    for f in files:
        for r in parse(f):
            if r['id'] in seen: continue
            t=r['title'] or ''
            if dur(r['duration'])<240: loai['ngan']+=1; continue
            if (r['subscriberCount'] or 0)>188000: loai['kenh_lon']+=1; continue
            if not keep(t.lower()): loai['lac_de']+=1; continue
            if re.search(r'[\u0600-\u06FF\u0900-\u0DFF\u0E00-\u0EFF\u3040-\u9FFF]',t): loai['khong_eng']+=1; continue
            seen[r['id']]=dict(id=r['id'],title=t,channel_id=r['channelId'],channel_sub=r['subscriberCount'],views=r['viewCount'],om=r['outlierScore'],vph=r['vph'],published=r['publishedAt'][:10],dinh_dang=dd)
    d=dict(ngay_do='2026-11-01',nguon_mau=nguon+f' · loại trước khi đưa vào: {loai}',cach_sap=['relevance','date'],view_dien_hinh_toi_thieu=500,
      kenh_minh=dict(sub=62700,trung_vi_view=597,view_dien_hinh_uoc=None),moc_nganh_p50=None,he_so_kenh_moi=0.5,nguong_thang=1.5,nguong_om=2.0,he_so_khop=1.0,chi_phi=2,tuoi_toi_thieu_ngay=14,videos=list(seen.values()))
    json.dump(d,open(out,'w',encoding='utf-8'),ensure_ascii=False,indent=1); print(out,len(seen),loai)
    for v in sorted(seen.values(),key=lambda x:-(x['om'] or 0))[:14]: print(' ',v['published'],v['views'],'OM',v['om'],'sub',v['channel_sub'],'vph',round(v['vph'] or 0,1),v['title'][:70],v['id'])
build(['b-r1.json','b-r2.json','b-r3.json','b-r4.json','b-r5.json'],lambda t:'rose' in t and 'desert rose' not in t and 'rosemary' not in t and re.search(r'winter|cold|freez|frost|dormant|protect',t),
 "vidiq_youtube_search tk3 US 2025-11-01..: 'overwinter potted roses' + 'roses in pots winter protection' (relevance) + 'overwintering roses containers' (date), medium 4-20' + 'winterize roses protect roses from freezing' (medium) + 'container roses winter care zone' (long); kênh ≤188K; tiêu đề có rose + mùa đông",'qua đông','mau-c1-roses.json')
build(['b-h1.json','b-h2.json','b-h3.json','b-h4.json','b-h5.json'],lambda t:'hibiscus' in t and not re.search(r'hair|tea|shampoo|mask|oil|recipe|drink|skin|henna|pipe cleaner|diy|paper|crochet|craft|paint|draw',t),
 "vidiq_youtube_search tk3 US 2025-11-01..: 'hibiscus dropping leaves' + 'hibiscus care indoors winter' (relevance) + 'hibiscus yellow leaves overwatering' (date) + 'tropical hibiscus overwintering bring indoors' + 'hibiscus leaves turning yellow falling off', medium 4-20'; kênh ≤188K; tiêu đề có hibiscus, bỏ tóc/trà",'sửa lỗi','mau-c1-hibiscus.json')
