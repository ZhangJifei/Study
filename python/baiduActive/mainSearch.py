from baiduActive import *
import time
import random
from myLogging import *

words_array = ('祛痘 西南交大', '祛痘 西南交通大学', '痘痘 西南交大', '痘痘 西南交通大学')
page_array = (0, 10, 20)

for i in range(200):
    for words in words_array:
        for page in page_array:
            baidu_search(words, page)
            time.sleep(10)
    logger.info ('Complete the %d th search' % (i+1))
    time.sleep(3500+random.randint(0, 200))
