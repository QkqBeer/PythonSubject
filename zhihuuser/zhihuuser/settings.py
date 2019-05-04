# -*- coding: utf-8 -*-

# Scrapy settings for zhihuuser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuuser'

SPIDER_MODULES = ['zhihuuser.spiders']
NEWSPIDER_MODULE = 'zhihuuser.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihuuser (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
  'cookie':'zap=e1897532-da3b-4e32-979b-08c40f3ee28f; d_c0="AKAiPABtnA2PTseXlFw8Yr0NCeXB44aWBwo=|1526615856"; _xsrf=wcyEe3aWtf6AdQ5iemRacmj0wueNL0Qg; tst=r; q_c1=f3da4070bef84663bfb4d23bb064689a|1551251793000|1523441494000; l_cap_id="NjUwYWZkYjBlMzljNDQwMTkzNTdkZDMwNzNlZDA3N2E=|1551252741|894d9b9a1be7759e6ed0d8406de45a6ac76b0c1e"; r_cap_id="ODY2MmVkYWRmZmVkNDY0ZmE4MDJjN2RkYTQxOGI1YmQ=|1551252741|c34c6db718838a2c47537f13b903fe3ea6a1880d"; cap_id="YmM1YTcyZDBkODA3NDMzYTgwYjQzZGFjY2IzNWU4MjA=|1551252741|d29b03736e95bb1dd0a4309f7415cc124b402153"; capsion_ticket="2|1:0|10:1551253109|14:capsion_ticket|44:NzA1NGEzNDgxZTlmNGQwODgzNWI0NWZkMTMyM2VjNGE=|3ebe13ccbd4fb6dbde612798240a620da678952cec32c1a4fc4fc13cfa6ac1ec"; z_c0="2|1:0|10:1551253144|4:z_c0|92:Mi4xTWJrV0F3QUFBQUFBb0NJOEFHMmNEU1lBQUFCZ0FsVk5tSXhqWFFDX0NvRVZEZUhQWFBkQ3gzenZjalpsYl92b05B|889050a4f41e3403f11ad038abe6e4af2b010bc54e0617a23ea2c58f0867c965"; __utmv=51854390.100--|2=registration_date=20160529=1^3=entry_date=20160529=1; tgw_l7_route=578107ff0d4b4f191be329db6089ff48; __utma=51854390.1309993040.1551267623.1551267623.1551411017.2; __utmb=51854390.0.10.1551411017; __utmc=51854390; __utmz=51854390.1551411017.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/topic/20004648/hot',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuuserSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuuserDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'zhihuuser.pipelines.ZhihuuserPipeline': 300,
#}

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
