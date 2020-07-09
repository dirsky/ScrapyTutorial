# ScrapyTutorial

scrapy startproject ScrapyTutorial
cd ScrapyTutorial
scrapy genspider douban douban.com
scrapy crawl douban

settings.py

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 3
COOKIES_ENABLED = False
启动middlewares、pipelines

会乱码
scrapy crawl douban -o douban.json -t json
-o 后面是导出文件名，-t 后面是导出类型(写清文件后缀名自动识别)

scrapy crawl douban -o douban.xml
scrapy crawl douban -o douban.csv
