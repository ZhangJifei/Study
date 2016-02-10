from urllib import request
from urllib import parse

url = "http://www.baidu.com/s?wd=" + parse.quote('中文')

with request.urlopen(url) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
