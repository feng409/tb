# -*- coding: utf-8 -*-
BOT_NAME = 'tb'

SPIDER_MODULES = ['tb.spiders']
NEWSPIDER_MODULE = 'tb.spiders'


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
    {'dnk': 'tb2892052_2013',
     'hng': 'CN%7Czh-CN%7CCNY%7C156',
     'lid': 'tb2892052_2013',
     'cookie2': '1bd78ac3190955301641da94011cb6b8',
     't': '64517359b01d22bde362490d52ee24c5',
     '_tb_token_': 'e81e14bbe884e',
     'cna': '/iKFFMFiQyYCAXEK2ALQ/2K+',
     '_m_h5_tk': '35c1f492643c62e1941ca33e955c0e3d_1550719810093',
     '_m_h5_tk_enc': 'daa4533af4c63f23f8e498c84d4e2dac',
     'uc1': 'cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&cookie21=V32FPkk%2FgihF%2FS5nr3O5&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTZ5Ofw3zSWYA%3D%3D&tag=8&lng=zh_CN',
     'uc3': 'vt3=F8dByEzd9EwBgai%2FHMk%3D&id2=Uoe1hgOxD1%2B6kQ%3D%3D&nk2=F5RHqQ7IP4NQJF94tt8%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D',
     'tracknick': 'tb2892052_2013',
     '_l_g_': 'Ug%3D%3D',
     'ck1': '""',
     'unb': '1614550477',
     'lgc': 'tb2892052_2013',
     'cookie1': 'WvLGliy5OCM9Js16RiEtjciJrry3Tk6rf%2BNAPo%2BIc2A%3D',
     'login': 'true',
     'cookie17': 'Uoe1hgOxD1%2B6kQ%3D%3D',
     '_nk_': 'tb2892052_2013',
     'uss': '""',
     'csg': 'fbf57016',
     'skt': '368767822bda148a',
     'isg': 'BK2tdtxyjWLTX2mNpYpNZv-CvE8nCuHcEc-QqO-yz8SzZswYt1u2rKE0UHolZvmU'}

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
