import os
# -*- coding: utf-8 -*-

# Scrapy settings for emails project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'emails'

SPIDER_MODULES = ['emails.spiders']
NEWSPIDER_MODULE = 'emails.spiders'
DOWNLOAD_DELAY = 1
ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
IMAGES_STORE = os.getcwd() + '/output'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'emails (+http://www.yourdomain.com)'
