from baiduActive import *
import time
from myLogging import *

words_array = ('祛痘 西南交大', '祛痘 西南交通大学', '痘痘 西南交大', '痘痘 西南交通大学')
page_array = (0, 10, 20)

for i in range(100):
    for words in words_array:
        for page in page_array:
            baidu_search(words, page)
            time.sleep(10)
    logger.info ('Start to trigger search')
    time.sleep(3600)
