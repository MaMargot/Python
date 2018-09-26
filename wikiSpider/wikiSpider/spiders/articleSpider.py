#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/25 9:22
# @Author  : Ryu
# @Site    : 
# @File    : articleSpider.py
# @Software: PyCharm

from  scrapy.selector import Selector
from scrapy import Spider
from wikiSpider.items import Article
#在目录上右键，选择Mark Directory As Sources root,把你的项目目录添加到sources root里.

class ArticleSpider():
    #该类与wikiSpider类（爬虫文件）不同,这个类只是在wikiSpider目录里的一员，仅仅用于维基词条页面的采集
    name="article"
    allowed_domains=["en.wikipedia.org"]
    start_urls=["http://en.wikipedia.org/wiki/Mian_page","http://en.wokopedia.org/wiki/Python_%28programming_language%29"]
    def parse(self,response):
        item=Article()
        title=response.xpath('//h1/text()')[0].extract()
        print("Title is :"+title)
        item['title']=title
        return item
#可以在wikiSpider主目录中用如下命令运行ArticleSpider
#$scrapy crawl article,会用条目名称article调用爬虫（不是类名，也不是文件名，而是由ArticleSpider的name='article'决定的）


from scrapy.contrib.spiders import CrawlSpider,Rule
from wikiSpider.items import Article
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class ArticleSpider(CrawlSpider):
    name='article'
    allowed_domains=["en.wikipedia.org"]
    start_urls=["http://en.wikipedia.org/wiki/Python_%28progamming_language%29"]
    rules=[Rule(SgmlLinkExtractor(allow=('(/wiki/)((?!:).)*$'),),callback="parse_item",follow=True]
    def parse_item(self,response):
        item=Article()
        title=response.xpath('//h1/text()')[0].extract()
        print("Title is :"+title)
        item['title']=title
        return item
