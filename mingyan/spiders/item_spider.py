import scrapy


class itemSpider(scrapy.Spider): # 继承scrapy.Spider类

    name = "itemSpider"   # 定义蜘蛛名

    start_urls = [  # 另外一种写法，无需定义start_requests方法
        'http://lab.scrapyd.cn']

    def parse(self, response):

        mingyan = response.css('div.quote')[0]

        text = mingyan.css('.text::text').extract_first()  # 提取名言
        autor = mingyan.css('.author::text').extract_first() # 提取作者
        tags = mingyan.css('.tags.tag::text').extract() # 提取标签
        tags = ','.join(tags)  #数组转换为字符串

        fileName = '%s-语录.txt' % autor # 爬取类容出入文件, 文件名为:作者-语录.txt
        with open(fileName, "a+") as f:
            f.write(text)  # 写入名言内容
            f.write('\n')  # 换行
            f.write('标签: ' + tags)  # 写入标签
