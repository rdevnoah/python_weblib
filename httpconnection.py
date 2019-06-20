from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')

# 성공
# GET / HTTP/1.1
# 200 OK
conn.request('GET', '/')
resp = conn.getresponse()
print(resp.status, resp.reason)

if resp.status == 200:
    body = resp.read() ## http body의 내용을 읽는 함수
    print(body, type(body))

# 실패
# GET /hello.html HTTP/1.1
# 404 Not Found
conn.request('GET', '/hello.html')
resp = conn.getresponse()
print(resp.status, resp.reason)
