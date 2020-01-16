import scrapy


class itemSpider(scrapy.Spider): # 继承scrapy.Spider类

    name = "listspider"   # 定义蜘蛛名

    start_urls = [  # 另外一种写法，无需定义start_requests方法
        'http://lab.scrapyd.cn']

    def parse(self, response):

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

        mingyan = response.css('div.quote')
        fileName = '语录.txt'  # 爬取类容出入文件, 文件名为:作者-语录.txt
        for i in mingyan:
            text = i.css('.text::text').extract_first()  # 提取名言
            autor = i.css('.author::text').extract_first() # 提取作者
            tags = i.css('.tag::text').extract() # 提取标签
            tags = ','.join(tags)  #数组转换为字符串


            with open(fileName, "a+", encoding='utf-8') as f:
                f.write(text)  # 写入名言内容
                f.write('\n')  # 换行
                f.write('作者: ' + autor)  # 写入作者
                f.write('\n')  # 换行
                f.write('标签: ' + tags )  # 写入标签
                f.write('\n\n')  # 换行
