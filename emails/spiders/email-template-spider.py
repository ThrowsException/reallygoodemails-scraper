import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from emails.items import ImageItem


class EmailTemplateSpire(CrawlSpider):
    name = "email"

    start_urls = [
        'https://reallygoodemails.com/category/inaugural/welcome/',
    ]

    rules = [
        Rule(LinkExtractor(
            allow=(
                'inaugural\/welcome\/[a-z-]+\/',
                'inaugural\/welcome\/page/\D+\/'
            ),
            unique=True,
            allow_domains=('reallygoodemails.com'),
            restrict_css=('.entry_hover', '.page-numbers', )),
            follow=True),
        Rule(LinkExtractor(allow=('.*\.html', ),
                           unique=True,
                           allow_domains=('reallygoodemails.com'),
                           restrict_css=('.entry_copy', )),
             callback='download_email',
             follow=True),
    ]

    def download_email(self, response):
        page = response.url.split("/")[-1]
        with open(f'output/{page}', 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % page)
