import scrapy

class DmozSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = [
        "rehttp://quotes.toscrape.com/"
    ]

    def parse(self, response):
        print(response.text)