from urllib import request
from urllib import parse
import re

url = "http://www.baidu.com/s?wd=" + parse.quote('祛痘 西南交大')
url_58_temp = "http://cd.58.com/mianbumeir/23435086794014x.shtml?PGTID=0d000000-0301-77a5-a9fc-d94212c8db35&ClickID=1"

with request.urlopen(url) as f:
    data = f.readlines()

    for line in data:
        line = line.decode('utf-8')
        m = re.match(r'^\s*(href = )"(.*?)"',line)
        if m:
            url_temp = m.group(2)
        if re.match(r'.*瑶芳专业.*',line):
            print (url_temp)
            with request.urlopen(url_temp) as f_temp:pass
            if re.match(r'.*成都58同城.*',line):
                print (url_58_temp)
                with request.urlopen(url_58_temp) as f_58_temp:pass




