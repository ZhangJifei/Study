from urllib import request
from urllib import parse
import re
import logging
from myLogging import *


def baidu_search(url_pre, words, page):
    url = url_pre + parse.quote(words) + "&pn=%s"%(str(page))
    url_58_temp = "http://cd.58.com/mianbumeir/23435086794014x.shtml?PGTID=0d000000-0301-77a5-a9fc-d94212c8db35&ClickID=1"

    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

        with request.urlopen(request.Request(url=url, headers=headers)) as f:
            data = f.readlines()

            for line in data:
                line = line.decode('utf-8')
                m = re.match(r'^(.*?)(href\s*=\s*)"(.*?)"(.*?)',line)
                if m:
                    url_temp = m.group(3)
                if re.match(r'.*瑶芳专业.*',line):
                    if (re.match(r'^(.*?)http://(.*?)',url_temp)) and (not re.match(r'^(.*?)url=(.*?)',url_temp)):
                        logger.info (url_temp)
                        with request.urlopen(request.Request(url=url_temp, headers=headers)) as f_temp:pass

                    # special access to the link for 58
                    if re.match(r'.*成都58同城.*',line):
                        logger.info (url_58_temp)
                        with request.urlopen(request.Request(url=url_58_temp, headers=headers)) as f_58_temp:pass

    except Exception as e:
        logging.exception(e)
        logger.info ('An exception happen here when search %s at page %d ' % words, page)



