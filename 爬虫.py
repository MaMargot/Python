#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/18 9:21
# @Author  : Ryu
# @Site    : 
# @File    : 爬虫.py
# @Software: PyCharm

#1
import bs4
import urllib
html=urllib.urlopen("http://www.pythonscraping.com/pages/page1.html")
print(html.read())
bsObj=bs4.BeautifulSoup(html.read())
print(bsObj.h1)
print(bsObj.nonExitentag)#返回NONE
print(bsObj.nonExitentag.somtag)#返回AttributeError
#异常：
#1、网页在服务器上不存在(或者获取页面的时候出现错误)
#2、服务器不存在
try:
    html=urllib.urlopen("http://pythonscraping.com/pages/page1.html")
except urllib.HTTPError,e:
    print(e)
    #返回空值，中断程序，或者执行另一个方案
else:
    #程序继续。注意：如果你已经在上面异常捕捉那一段代码里返回或中断
    #那么就不需要使用else语句了，或者执行另一个方案
    html

if html.h1 is None:
    print ("URL is not found")
else:
    #程序继续
    html

try:
    badContent=bsObj.nonExistingTag.anotherTag
except AttributeError,e:
    print("Tag was not found")
else:
    if badContent==None:
        print("Tag was not found")
    else:
        print(badContent)

import urllib
from bs4 import BeautifulSoup
def getTitle(url):
    try:
        html=urllib.urlopen(url)
    except urllib.HttpError,e:
        return None
    try:
        bsObj=BeautifulSoup(html.read())
        title=bsObj.body.h1
    except AttributeError,e:
        return None
    return title
title=getTitle("http://www.pythscraping.com/pages/page1.html")
if title==None:
    print("Title could not be found")
else:
    print(title)

#2
from urllib import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj=BeautifulSoup(html.read())
namelist=bsObj.findAll("span",{"class":"green"})#返回的是标签对象
for name in namelist:
    print(name.get_text())#get_text()会将所有标签清除，返回只含有一个包含文字的字符串
#findALL(tag,attributes,recursive,text,limit,keywords)
#find(tag,attributes,recursive,text,keywords)
#tag,可以传递一个或多个名称标签，如{"h1","h2","h3"}
#attribus，用一个python字典封装一个标签的若干属性和对应的属性值，如{"class":{"green","red"}
#recursive,一个布尔变量，决定是否递归，查找标签参数的所有字标签
#text，文本参数，用标签的文本内容去匹配，而不是标签的属性
namelist=bsObj.findAll(text="the prince")
print(len(namelist))
#limit,find等价于findALL的limit为1，获得的前几项结果是按照网页上的额顺序排序
#keyword，可以选择具有指定属性的标签
allText=bsObj.findAll(id="text")
print(allText[0].get_text())#获得的是naviablestring对象，表示标签里面的文字
#等价于bsObj.findALL("",{"id":"text"}
#注意在使用class属性查找标签时，因为class是关键字，会产生语法错误
#bsObj.findALL(class="Green")
#解决方法：1、bsObj.findALL(class_="Green")
#解决方法：2、bsObj.findALL("",{"class":"Green"})
#<!--像这样-->用来查找HTML文档的注释标签,comment对象

#导航树：痛过标签在文档中的位置来查找标签








