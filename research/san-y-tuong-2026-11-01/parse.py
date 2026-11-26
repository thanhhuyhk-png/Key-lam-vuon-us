import json,sys
dec=json.JSONDecoder()
def val(seg,key,start=0):
    t='"'+key+'": '
    i=seg.find(t,start)
    if i<0: return None
    try: return dec.raw_decode(seg[i+len(t):])[0]
    except Exception: return None
def parse(path):
    s=open(path,encoding='utf-8').read()
    out=[]
    for seg in s.split('{"kind": "video"')[1:]:
        c=seg.rfind('"channelId": ')
        if c<0: continue
        r={'id':val(seg,'id'),'title':val(seg,'title')}
        for k in ['channelId','channelTitle','publishedAt','viewCount','subscriberCount','vph','outlierScore','duration']:
            r[k]=val(seg,k,c)
        if r['viewCount'] is None: continue
        out.append(r)
    return out
if __name__=='__main__':
    for p in sys.argv[1:]:
        v=parse(p); print(p,len(v))
        for r in v: print(int(r['viewCount']),r['outlierScore'],r['subscriberCount'],r['publishedAt'][:10],r['duration'],(r['title'] or '')[:70],'|',r['id'])
