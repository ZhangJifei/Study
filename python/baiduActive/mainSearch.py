from baiduActive import *
import time
import random
from myLogging import *


words_array = ('祛痘 西南交大', '祛痘 西南交通大学', '痘痘 西南交大', '痘痘 西南交通大学',
               '祛痘 犀浦', '治疗青春痘 西南交通大学', '治疗痘痘 西南交通大学')

baidu_page_array = (0, 10, 20)
baidu_url_pre = 'http://www.baidu.com/s?wd='

so360_page_array = (1, 2, 3)
so360_url_pre = 'http://www.so.com/s?q='

for i in range(200):
    for words in words_array:
        for page in baidu_page_array:
            baidu_search(baidu_url_pre, words, page)
            time.sleep(5)
    logger.info ('Complete the %d th search at baidu \n' % (i+1))

    for words in words_array:
        for page in so360_page_array:
            baidu_search(so360_url_pre, words, page)
            #time.sleep(10)
    logger.info ('Complete the %d th search at so 360 \n' % (i+1))

    time.sleep(3500+random.randint(0, 200))
