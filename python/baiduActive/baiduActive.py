﻿from urllib import request
from urllib import parse
import re
import logging
from myLogging import *

def baidu_search(words, page):
    url = "http://www.baidu.com/s?wd=" + parse.quote(words) + "&pn=%s"%(str(page))
    url_58_temp = "http://cd.58.com/mianbumeir/23435086794014x.shtml?PGTID=0d000000-0301-77a5-a9fc-d94212c8db35&ClickID=1"
    url_dianping_temp = "http://www.dianping.com/shop/23583529"

    try:

        with request.urlopen(url) as f:
            data = f.readlines()

            for line in data:
                line = line.decode('utf-8')
                m = re.match(r'^\s*(href = )"(.*?)"',line)
                if m:
                    url_temp = m.group(2)
                if re.match(r'.*瑶芳专业.*',line):
                    logger.info (url_temp)
                    with request.urlopen(url_temp) as f_temp:pass

                    # special access to the link for 大众点评
                    if re.match(r'.*大众点评.*',line):
                        logger.info (url_dianping_temp)
                        with request.urlopen(url_dianping_temp) as url_dianping_temp:pass

                    # special access to the link for 58
                    if re.match(r'.*成都58同城.*',line):
                        logger.info (url_58_temp)
                        with request.urlopen(url_58_temp) as f_58_temp:pass

    except Exception as e:
        logging.exception(e)
        if re.match(r'.*大众点评.*',line):
            logger.info (url_dianping_temp)
            with request.urlopen(url_dianping_temp) as url_dianping_temp:pass


