import scrapy

from mingyan.items import ImageSpiderItem


class ImgspiderSpider(scrapy.Spider):
    name = 'ImgSpider'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html']

    def parse(self, response):
        item = ImageSpiderItem()  # 实例化item
        imgurls = response.css(".post img::attr(src)").extract() # 注意这里是一个集合也就是多张图片
        item['imgurl'] = imgurls
        # 抓取文章标题作为图集名称
        item['imgname'] = response.css(".post-title a::text").extract_first()
        yield item
