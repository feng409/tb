# -*- coding: utf-8 -*-
BOT_NAME = 'tb'

SPIDER_MODULES = ['tb.spiders']
NEWSPIDER_MODULE = 'tb.spiders'

# DB Config
MYSQL_HOST = ''
MYSQL_USER = ''
MYSQL_PASS = ''
MYSQL_CHARSET = ''
MYSQL_DB = ''
MYSQL_PORT = ''

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS_PER_IP = 0

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
COOKIES_DEBUG = True

COOKIE = \
    {'JSESSIONID': 'BAC3D5DF95576CFA25C94018AC2CEC39',
     '_cc_': 'Vq8l%2BKCLiw%3D%3D',
     '_l_g_': 'Ug%3D%3D',
     '_m_h5_tk': '279858a7d74b3116fcdf4ad31ff5fdab_1551525641214',
     '_m_h5_tk_enc': '0bef1561ba7dbe6b1e75bb8e6fff3944',
     '_nk_': 'tb2892052_2013',
     '_tb_token_': 'f346818bf87bd',
     'alitrackid': 'world.taobao.com',
     'cna': 'cnE2FIdhKXwCAcYNMjh9cNiL',
     'cookie1': 'WvLGliy5OCM9Js16RiEtjciJrry3Tk6rf%2BNAPo%2BIc2A%3D',
     'cookie17': 'Uoe1hgOxD1%2B6kQ%3D%3D',
     'cookie2': '37ff44f2e0006280b218bb749fbf180f',
     'csg': 'acf1876e',
     'dnk': 'tb2892052_2013',
     'enc': 'BE0z2APzU5Y1CBR5m%2BdpzeNurgvO5egFRqDU2YD4fiHgKWe3I4KiKPNe2wOekLc9BR%2F9vV1MW0ThVYwJXpQtEw%3D%3D',
     'existShop': 'MTU1MTUxNzAxMQ%3D%3D',
     'hng': 'JP%7Czh-CN%7CJPY%7C392',
     'isg': 'BMfHK2APVySgqdO-mFU0QQlAVn1RZOAECoAw9Jm049Z9COfKoZwr_gXKr4jzu3Mm',
     'l': 'bBNwfMzevHxkRTg5BOfwGuI-bTQtwIRbzjFzw4ZYfICPOKCpIypRWZaAKi89C3hVa6myR3oadEZ8B2TUoPaEQ',
     'lastalitrackid': 'world.taobao.com',
     'lgc': 'tb2892052_2013',
     'mt': 'ci=12_1',
     'sg': '374',
     'skt': 'c2ac4049b05c0155',
     't': '9f4ee4ae87be12aedd65433208136b17',
     'tg': '0',
     'thw': 'us',
     'tracknick': 'tb2892052_2013',
     'uc1': 'cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie21=VT5L2FSpccLuJBreK%2BBd&cookie15=UIHiLt3xD8xYTw%3D%3D&existShop=false&pas=0&cookie14=UoTZ5bYgHLdMAg%3D%3D&tag=8&lng=zh_CN',
     'uc3': 'vt3=F8dByEv1QD0QHJ0jsg4%3D&id2=Uoe1hgOxD1%2B6kQ%3D%3D&nk2=F5RHqQ7IP4NQJF94tt8%3D&lg2=VT5L2FSpMGV7TQ%3D%3D',
     'unb': '1614550477',
     'v': '0'}

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    # 'referer': 'https://www.taobao.com/?spm=1.7156474.1581860521.1.0dH2hi'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   #'tb.middlewares.TbSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'tb.middlewares.CharlesMiddleware': 542,
    # 'tb.middlewares.ProxyMiddleware': 543,
    # 'tb.middlewares.UserAgentMiddleware': 544,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'tb.pipelines.ShopPipeline': 500,  # 过滤掉店铺类型信息
    'tb.pipelines.GoodPipeline': 600,  # 淘宝好评过滤
    'tb.pipelines.ParsePipeline': 700,  # 转换为目标item
    'tb.pipelines.ContentPipeline': 800,  # 默认评论过滤
    'tb.pipelines.LengthPipeline': 900,  # 内容长度过滤

    'tb.pipelines.MysqlPipeline': 1000,  # 保存至数据库
}

FEED_EXPORT_ENCODING = 'utf-8'
FEED_EXPORTERS = {
    'csv': 'tb.spiders.csv_item_exporter.CustomCsvItemExporter',
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
