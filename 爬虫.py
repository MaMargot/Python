#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 9:21
# @Author  : Ryu
# @Site    : 
# @File    : 爬虫.py
# @Software: PyCharm

import bs4
import urllib
html=urllib.urlopen("http://www.pythonscraping.com/pages/page1.html")
print(html.read())
bsObj=bs4.BeautifulSoup(html.read())
print(bsObj.h1)
