from urllib.parse import urlencode
from urllib.request import urlopen, Request

# GET
httpresponse = urlopen('http://www.example.com?a=10&b=20')
body = httpresponse.read()
print(body)


# post
data = {
    'email': 'zzagam2@gmail.com',
    'name': 'rdevnoah',
    'company': '카페24'
}

data = urlencode(data).encode('utf-8')

request = Request('http://www.example.com', data)
request.add_header('Content-Type', 'text/html')
# request.add_header('cookies:jsessionid=2123124klasdfk') # session id hijacking
httpresponse = urlopen(request)
body = httpresponse.read()
print(body)

