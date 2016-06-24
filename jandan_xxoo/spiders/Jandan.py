import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from jandan_xxoo.items import JandanItem

class JandanSpider(CrawlSpider):
    name = 'jandan.net'
    allowed_domains = ['jandan.net']
    start_urls = [
        'http://jandan.net/ooxx'
    ]

    rules = (
        Rule(LinkExtractor(allow=('.*?/ooxx/page-\d+.*?')), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        # self.logger.info('A response from %s just arrived!', response.url)
        for sel in response.xpath('//ol[@class="commentlist"]/li//div[@class="row"]'):
            item = JandanItem()
            item['author'] = sel.xpath('div[@class="author"]/strong/text()').extract()
            item['id'] = sel.xpath('div[@class="text"]/span/a/text()').extract()
            item['image_urls'] = sel.xpath('div[@class="text"]/p/a[@class="view_img_link"]/@href').extract()
            item['like'] = sel.xpath('div[@class="text"]/div[@class="vote"]/span[2]/text()').extract()
            item['dislike'] = sel.xpath('div[@class="text"]/div[@class="vote"]/span[3]/text()').extract()
            yield item