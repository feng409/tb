# -*- coding: utf-8 -*-
BOT_NAME = 'tb'

SPIDER_MODULES = ['tb.spiders']
NEWSPIDER_MODULE = 'tb.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tb (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
COOKIES_DEBUG = True

COOKIE = \
    {'JSESSIONID': 'B55F2F5B01941AD5B485E71FD6CBCD02',
     'UM_distinctid': '16893111eb672a-015ffe7e050cca-10336653-1fa400-16893111eb7713',
     '_cc_': 'W5iHLLyFfA%3D%3D',
     '_l_g_': 'Ug%3D%3D',
     '_nk_': 'tb2892052_2013',
     '_tb_token_': 'e81e14bbe884e',
     'alitrackid': 'www.taobao.com',
     'cna': '/iKFFMFiQyYCAXEK2ALQ/2K+',
     'cookie1': 'WvLGliy5OCM9Js16RiEtjciJrry3Tk6rf%2BNAPo%2BIc2A%3D',
     'cookie17': 'Uoe1hgOxD1%2B6kQ%3D%3D',
     'cookie2': '1bd78ac3190955301641da94011cb6b8',
     'csg': '826f781d',
     'dnk': 'tb2892052_2013',
     'enc': 'dGCq3hqVB8YyTz5EYS5i9N6IJmfPAJHEE8Fzi20pcpU0zDA1PCI2sic6H9%2FxugULtC4XTa%2Bc%2FLtZhutU%2FIbl%2Fg%3D%3D',
     'existShop': 'MTU1MDU2OTAyNw%3D%3D',
     'hng': 'CN%7Czh-CN%7CCNY%7C156',
     'isg': 'BN3d6ETKXRdFmzkacYLkMn7g7L8XUmo7Yd-gOJ-iGTRjVv2IZ0ohHKvEgAp1jSkE',
     'l': 'bBLGAfXIvRBK5EsxBOCgNuI-bf7ORIRAguPRwonvi_5KT6L_38QOlo8XPFp6Vj5Rs_Ty4JWkwg99-etXw',
     'lastalitrackid': 'www.taobao.com',
     'lgc': 'tb2892052_2013',
     'mt': 'ci=0_0&np=',
     'sg': '374',
     'skt': '2cbd709d3aadab11',
     't': '64517359b01d22bde362490d52ee24c5',
     'tg': '0',
     'thw': 'cn',
     'tracknick': 'tb2892052_2013',
     'uc1': 'cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&cookie21=URm48syIYB3rzvI4Dim4&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=false&pas=0&cookie14=UoTZ5OXqLL5QnQ%3D%3D&tag=8&lng=zh_CN',
     'uc3': 'vt3=F8dByEzfi2gcRSM4K7o%3D&id2=Uoe1hgOxD1%2B6kQ%3D%3D&nk2=F5RHqQ7IP4NQJF94tt8%3D&lg2=URm48syIIVrSKA%3D%3D',
     'unb': '1614550477',
     'v': '0'
     }

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'referer': 'https://www.taobao.com/?spm=1.7156474.1581860521.1.0dH2hi'
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
    'tb.middlewares.UserAgentMiddleware': 544,
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
