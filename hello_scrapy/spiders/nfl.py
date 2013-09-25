from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from hello_scrapy.items import HelloScrapyItem

class NflSpider(CrawlSpider):
    name = 'nfl'
    allowed_domains = ['http://nfl.com']
    start_urls = ['http://www.nfl.com/']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        items = []
        #i['domain_id'] = hxs.select('//input[@id="sid"]/@value').extract()
        #i['name'] = hxs.select('//div[@id="name"]').extract()
        #i['description'] = hxs.select('//div[@id="description"]').extract()
        print "Parsing all teams:"
        for h in hxs.select('//ul[@class="ft-teams-list"]/li/a'):
            i = HelloScrapyItem()
            i['name']=h.select('text()').extract()[0]
            i['link']=h.select('@href').extract()[0]
            items.append(i)
            print "Team:",i['name'],i['link']
        print "Total %d teams"%len(items)
        return items
