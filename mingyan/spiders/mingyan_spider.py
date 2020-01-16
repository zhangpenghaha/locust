import scrapy


class mingyan(scrapy.Spider): # 继承scrapy.Spider类

    name = "mingyan"   # 定义蜘蛛名

    start_urls = [  # 另外一种写法，无需定义start_requests方法
        'http://lab.scrapyd.cn/page/1/',
        'http://lab.scrapyd.cn/page/2/',
    ]

    # def start_requests(self):
    #     # 定义爬取的连接
    #     urls = [
    #         'http://lab.scrapyd.cn/page/1/',
    #         'http://lab.scrapyd.cn/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse) # 爬取到的页面如何处理? 提交给parse处理

    def parse(self, response):
        """
        :param response: start_requests已经爬取到页面，那如何提取我们想要的内容呢？那就可以在这个方法里面定义。
        这里的话，并木有定义，只是简单的把页面做了一个保存，并没有涉及提取我们想要的数据，后面会慢慢说到
        也就是用xpath、正则、或是css进行相应提取，这个例子就是让你看看scrapy运行的流程：
        1、定义链接；
        2、通过链接爬取（下载）页面；
        3、定义规则，然后提取数据；
        就是这么个流程，似不似很简单呀？
        :return:
        """
        page = response.url.split("/")[-2]        # 根据上面的连接提取分页, 如: /page/1/,提取到的就是: 1
        filename = 'mingyan-%s.html' % page     # 拼接文件名, 如果是第一页, 最终文件名是: mingyan-1.html
        with open(filename, 'wb') as f:          #
            f.write(response.body)                # response.body代表刚才下载的页面
        self.log('保存文件: %s' % filename)      # 打印日志

        text= response.css('title::text').extract_first()
        print(text)