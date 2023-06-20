# 별칭을 사용하여 라이브러리 임포트
import requests as req

res = req.get('https://api64.ipify.org/')
print(res.status_code)            # 200
print(res.text)                   # 175.117.84.242
print(res.raw)                    # <urllib3.response.HTTPResponse object at 0x000001A3AF6F49D0>

# 응답 받은 것에 대한 request
print(res.request.method)         # GET
print(res.request.headers)        
# {'User-Agent': 'python-requests/2.31.0', 
# 'Accept-Encoding': 'gzip, deflate', 
# 'Accept': '*/*', 'Connection': 'keep-alive'}

print(res.cookies)                # <RequestsCookieJar[]>
print(res.elapsed)                # 0:00:17.105375
