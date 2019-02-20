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
DOWNLOAD_DELAY = 10
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS_PER_IP = 0

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
COOKIES_DEBUG = True

COOKIE = \
    {'_l_g_': 'Ug%3D%3D',
     '_nk_': 'tb2892052_2013',
     '_tb_token_': 'ee5b61e8b9ee8',
     'ck1': '""',
     'cna': 'cnE2FIdhKXwCAcYNMjh9cNiL',
     'cookie1': 'WvLGliy5OCM9Js16RiEtjciJrry3Tk6rf%2BNAPo%2BIc2A%3D',
     'cookie17': 'Uoe1hgOxD1%2B6kQ%3D%3D',
     'cookie2': '11f307c9c9a7baf9c5e0ac4a933dd813',
     'csg': '2ebdc790',
     'dnk': 'tb2892052_2013',
     'hng': 'JP%7Czh-CN%7CJPY%7C392',
     'isg': 'BD4-TDYP7oS3xzqgaqxkcGkyj1JA13lTwzRojuhHhgEci99lUA4MCe5tAhfi5_oR',
     'l': 'bBSclpOcvHcfdzWUKOCNcuI-bTQtOIRXDuPRwoeWi_5IT1XOyRQOlkMe5ev62j5PtOYB4cyBluetceqLJPvf.',
     'lgc': 'tb2892052_2013',
     'lid': 'tb2892052_2013',
     'login': 'true',
     'skt': 'a9c66060148d452b',
     't': '9f4ee4ae87be12aedd65433208136b17',
     'tracknick': 'tb2892052_2013',
     'uc1': 'cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&cookie21=VT5L2FSpccLuJBreK%2BBd&cookie15=URm48syIIVrSKA%3D%3D&existShop=false&pas=0&cookie14=UoTZ5Oa3PK2cGw%3D%3D&tag=8&lng=zh_CN',
     'uc3': 'vt3=F8dByEzc6zZhEzv%2FEPo%3D&id2=Uoe1hgOxD1%2B6kQ%3D%3D&nk2=F5RHqQ7IP4NQJF94tt8%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D',
     'unb': '1614550477',
     'uss': '""',
     'x5sec': '7b22726174656d616e616765723b32223a223961663936306666383630356238663136356633306631346430613366383635434e726d74654d46454a7179312f54393965657231414561444445324d5451314e5441304e7a63374d513d3d227d'}

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
