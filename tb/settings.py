# -*- coding: utf-8 -*-

# Scrapy settings for tb project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tb'

SPIDER_MODULES = ['tb.spiders']
NEWSPIDER_MODULE = 'tb.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tb (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
COOKIES_DEBUG = False

COOKIE = {
    'cna': 'ydYHEYpp4kcCAXQarxK6dIP9',
    'otherx': 'e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0',
    'enc': 'ovOhKwTFvD03bY%2BEjcb4qKukBRIH%2F4kT%2B%2B2sCNB9PJcKZEGjxn%2FSCKIdiMReDlUkwm7E8oVCfs%2BpA1%2BjJ1Wgeg%3D%3D',
    'hng': 'CN%7Czh-CN%7CCNY%7C156',
    'uc1': 'cookie14=UoTfKLNb36nxAQ%3D%3D',
    't': '75a10d4e05fbed756c51ea7144d1a4f9',
    'uc3': 'vt3=F8dBzrhPheyEtjjcV%2B0%3D&id2=Uoe1hgOxD1%2B6kQ%3D%3D&nk2=F5RHqQ7IP4NQJF94tt8%3D&lg2=WqG3DMC9VAQiUQ%3D%3D',
    '_tb_token_': 'ed3d3379e1a1e',
    'cookie2': '20e2c9040295e64a91c0888b1e87385a',
    '_m_h5_tk': '6c51944c5539f96904a98a4ccccba34f_1533666447689',
    '_m_h5_tk_enc': '49727615173eb8acd340a8c0cd921ef9',
    'isg': 'BLCw5KQfn9rdJkJaZ2VX00DZgXfCUe8spE5t36oB6IveZVIPUglM0zQ3uC2gQEwb'
}

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.39',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   'tb.middlewares.TbSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'tb.middlewares.ProxyMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'tb.pipelines.GoodPipeline': 300,
    'tb.pipelines.ParsePipeline': 310,
    'tb.pipelines.ContentPipeline': 320,
    'tb.pipelines.LengthPipeline': 330,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
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
