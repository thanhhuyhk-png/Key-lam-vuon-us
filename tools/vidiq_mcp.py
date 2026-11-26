"""Gọi vidIQ MCP bằng API key riêng (tài khoản vidIQ phụ) qua HTTP, khi connector claude.ai hết credit.

Usage:
    python -X utf8 -I tools/vidiq_mcp.py tools                       # liệt kê công cụ
    python -X utf8 -I tools/vidiq_mcp.py call vidiq_balance '{}'     # gọi một công cụ (JSON tham số)
    VIDIQ_ACCT=2 python -X utf8 -I tools/vidiq_mcp.py call ...       # chọn tài khoản (mặc định 3)
Khóa đọc từ .env (VIDIQ_API_KEY_<n>) hoặc biến môi trường; không in khóa ra màn hình.
Endpoint: https://mcp.vidiq.com/mcp (vidiq.com/mcp ghi hỗ trợ xác thực bằng API key).
"""
import json
import os
import pathlib
import sys
import urllib.error
import urllib.request

URL = "https://mcp.vidiq.com/mcp"
ENV = pathlib.Path(__file__).resolve().parent.parent / ".env"


def key():
    name = "VIDIQ_API_KEY_" + os.environ.get("VIDIQ_ACCT", "3")
    k = os.environ.get(name)
    if not k and ENV.exists():
        for ln in ENV.read_text(encoding="utf-8", errors="ignore").splitlines():
            if ln.startswith(name + "="):
                k = ln.split("=", 1)[1].strip().strip('"')
    if not k:
        raise SystemExit("thiếu " + name)
    return k


def rpc(method, params=None, sid=None, hdr="bearer", rid=1):
    h = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream", "User-Agent": "curl/8.5.0"}
    k = key()
    if hdr == "bearer":
        h["Authorization"] = "Bearer " + k
    else:
        h["x-api-key"] = k
    if sid:
        h["Mcp-Session-Id"] = sid
    body = {"jsonrpc": "2.0", "method": method, "params": params or {}}
    if not method.startswith("notifications/"):
        body["id"] = rid
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), headers=h, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        txt = r.read().decode("utf-8", "ignore")
        sid2 = r.headers.get("Mcp-Session-Id") or sid
    if txt.lstrip().startswith("event:") or "data:" in txt[:20]:
        for ln in txt.splitlines():
            if ln.startswith("data:"):
                txt = ln[5:].strip()
                break
    return (json.loads(txt) if txt.strip() else {}), sid2


def session(hdr):
    r, sid = rpc("initialize", {"protocolVersion": "2025-03-26", "capabilities": {}, "clientInfo": {"name": "garden-us", "version": "1"}}, hdr=hdr)
    rpc("notifications/initialized", sid=sid, hdr=hdr)
    return sid


def main():
    cmd = sys.argv[1]
    last = None
    for hdr in ("bearer", "x-api-key"):
        try:
            sid = session(hdr)
            if cmd == "tools":
                r, _ = rpc("tools/list", sid=sid, hdr=hdr, rid=2)
                for t in r.get("result", {}).get("tools", []):
                    print(t["name"])
            else:
                r, _ = rpc("tools/call", {"name": sys.argv[2], "arguments": json.loads(sys.argv[3] if len(sys.argv) > 3 else "{}")}, sid=sid, hdr=hdr, rid=2)
                res = r.get("result", r)
                out = pathlib.Path(os.environ.get("VIDIQ_OUT", "")) if os.environ.get("VIDIQ_OUT") else None
                if out:
                    out.write_text(json.dumps(res, ensure_ascii=False), encoding="utf-8")
                sc = res.get("structuredContent") if isinstance(res, dict) else None
                print(json.dumps(sc if sc is not None else res, ensure_ascii=False)[:60000])
            return
        except urllib.error.HTTPError as e:
            last = f"{hdr}: HTTP {e.code} {e.read().decode('utf-8', 'ignore')[:200]}"
        except Exception as e:
            last = f"{hdr}: {type(e).__name__} {str(e)[:200]}"
    raise SystemExit("không kết nối được: " + str(last))


if __name__ == "__main__":
    main()
