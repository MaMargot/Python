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
#limit,find等价于findALL的limit为1，获得的前几项结果是按照网页上的顺序排序
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
#一般情况下，BeauitfulSoup函数总是处理当前标签的后代标签，如bsObj.body.h1
import urllib
from bs4 import BeautifulSoup
html=urllib.urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj=BeautifulSoup(html)
for child in bsObj.find("table",{"id":"giftList"}).children:
    print(child)
from urllib import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj=BeautifulSoup(html)
for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)
#打印产品列表里的所有行的产品，第一行标题除外：
#1、对象不能把自己作为兄弟标签
#2、只调用后面的兄弟标签
#next_sibling与previous_sibling返回的是单个标签，previous_sibling一组兄弟标签中的前一个标签
#next_sibling与previous_siblings返回的是一组标签
from urllib import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.pythonscraping.com/pages/page3/html")
bsObj=BeautifulSoup(html)
print(bsObj.find("img",attrs={"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
print(bsObj.find("img",src="../img/gifts/img1.jpg").parent.previous_sibling.get_text())
bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent
from urllib import urlopen
from bs4 import BeautifulSoup
import re
html=urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj=BeautifulSoup(html)
images=bsObj.findAll("img",{"src":re.compile(r"../img/gifts/img.*.jpg")})#用于过滤标签的内容
for image in images:
    print (image["src"])
Mytag.attrs#获取一个标签对象的全部属性
bsObj.attrs
bsObj.attrs["src"]#返回的是一个python字典对象，可以获取和操作这些属性
bsObj.h1.get('attr')
#Lambda表达式,本质上是一个函数，可以作为其他函数的变量使用，即一个函数不是定义成f(x,y)，而是定义成f(g(x),y)或f(g(x),h(x))
#允许我们把特定函数类型当做findAll函数的参数，唯一的限制条件是这些函数必须把一个标签作为参数且返回布尔类型。
soup=BeautifulSoup(html)
soup.findAll(lambda tag:len(tag.attrs)==2)#获取两个属性标签，评估每一个标签对象，把评估结果为真的标签保留，把其他标签剔除

#动态页面爬取
from urllib import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://en.wikipedia.org/wiki/Kevin_Baocon")
bsObj=BeautifulSoup(html)
bsObj.findAll("a")
for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print (link.attrs['href'])
link.attrs
from urllib import urlopen
from bs4 import BeautifulSoup
import re
html=urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj=BeautifulSoup(html)
for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
links=bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
str(links)
type(links)
links
links[1]
#其中^((?!:).)*$匹配不以：结尾的
from urllib import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
random.seed(datetime.datetime.now())
def getlinks(articleurl):
    html=urlopen("htt://en.wikipedia.org"+articleurl)
    bsObj=BeautifulSoup
    return bsObj.find("div",{'id':'bodyContent'}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
links=getlinks("/wiki/Kevin_Bacon")
while len(links)>0:
    newArticle=links[random.randint(0,len(links)-1)].attrs["href"]
    print (newArticle)
    links=getlinks(newArticle)

from urllib import urlopen
from bs4 import BeautifulSoup
import re
pages=set()#存放不重复元素，元素顺序随意
def getlinks(pageurl):
    global pages
    html=urlopen("http://en.wikipedia.org"+pageurl)
    bsObj=BeautifulSoup(html)
    for link in bsObj.findAll("a",href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if(link.attrs['href']) not in pages:
                #我们遇到了新页面
                newpage=link.attrs['href']
                print(newpage)
                pages.add(newpage)
                getlinks(newpage)
getlinks("")
#python默认的递归限制是1000次！！！！
from urllib import urlopen
from bs4 import BeautifulSoup
import re
pages=set()
def getlinks(pageurl):
    global pages
    html=urlopen("http://en.wikipedia.org"+pageurl)
    bsObj=BeautifulSoup(html)
    try:
        print (bsObj.h1.get_text())
        print (bsObj.find(id="mw-content-text").findAll("p")[0])
        print (bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("页面缺少一些属性！不过不用担心！")
    for link in bsObj.findAll("a",href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #我们遇到了新页面
                newpage=link.attrs['href']
                print("----------\n"+newpage)
                pages.add(newpage)
                getlinks(newpage)
getlinks("")

from urllib import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
pages=set()
random.seed(datetime.datatime.now())
#获取页面所有内链的列表
def getinternallinks(bsObj,includeurl):
    internallinks=[]
    #找出所有以“/”开头的链接
    for link in bsObj.findAll("a",href=re.compile("^(/|.*"+includeurl+")")):#其中双引号全部换成单引号也一样，但不能将“+”号两边的双引号换成单引号，这样就将+includeUrl+变成一个字符串了
        #^ (/ |.* "+includeUrl+")此正则表达式意思为：匹配以“ / ”开头的字符串，或匹配包含“includeUrl”这个变量内容的字符串
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internallinks:
                internallinks.append(link.attrs['href'])
    return internallinks
#获取页面所有外链的列表
def getexternallinks(bsObj,excludeurl):
    externallinks=[]
    #找出所有以"http"或"www"开头且不包含当前url的链接
    for link in bsObj.findAll("a",href=re.compile("^(http|www)((?!"+excludeurl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externallinks:
                externallinks.append(link.attrs['href'])
    return externallinks
def splitAddress(address):
    addressParts=address.replace("http://","").split("/")
    return addressParts
def getrandomexternallinks(startingpage):
    html=urlopen(startingpage)
    bsObj=BeautifulSoup(html)
    externallinks=getexternallinks(bsObj,splitAddress(startingpage)[0])
    if len(externallinks)==0:
        internallinks=getinternallinks(startingpage)
        return getexternallinks(internallinks[random.randint(0,len(internallinks)-1)])
    else:
        return externallinks[random.randint(0,len(externallinks)-1)]
def followexternalonly(startingsite):
    externallink=getrandomexternallinks("http://oreilly.com")
    print("随机外链式："+externallink)
    followexternalonly(externallink)

#收集网站上发现的所有外链列表
allExtlinks=set()
allintlinks=set()
def getallexternallinks(siteurl):
    html=urlopen(siteurl)
    bsObj=BeautifulSoup(html)
    internallinks=getinternallinks(bsObj,splitAddress(siteurl)[0])
    externallinks=getexternallinks(bsObj,splitAddress(sireurl)[0])
    for link in externallinks:
        if link not in allExtlinks:
            allExtlinks.add(link)
            print(link)
    for link in internallinks:
        if link not in allintlinks:
            print("即将获取连接的URL是："+link)
            allintlinks.add(link)
            getallexternallinks(link)
getallexternallinks("http://oreilly.com")

#scrapy采集,可采集一个或多个域名的信息
#$scrapy startproject wikiSpider ，在cmd中运行建立Scrapy项目
#创建articleSpider.py程序,并在items.py定义不同的条目(比如url、content、header、image等)
#$scrapy crawl article -s LOG_FILE=wiki.log,输出到一个独立的文件里
#Scrapy用Item对象决定要从它的浏览页面中提取哪些信息
#$ scrapy crawl article -o articles.csv -t csv
#$ scrapy crawl article -o articles.json -t json
#$ scrapy crawl article -o articles.xml -t xml
#https://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html

#API
#GET 就是你在浏览器中输入网址浏览网站所做的事情。当你访问 http://freegeoip.net/
#json/50.78.253.58 时， 就会使用 GET 方法。
#POST 基本就是当你填写表单或提交信息到网络服务器的后端程序时所做的事情。每次当你
#登录网站的时候，就是通过用户名和（有可能加密的）密码发起一个 POST 请求。如果你用
#API 发起一个 POST 请求，相当于说“请把信息保存到你的数据库里”。
#PUT 在网站交互过程中不常用，但是在 API 里面有时会用到。 PUT 请求用来更新一个对象
#或信息。例
#DELETE 用于删除一个对象。例如，如果我们向 http://myapi.com/user/23 发出一个 DELETE 请
#求，就会删除 ID 号是 23 的用户。
#http://developer.echonest.com/api/v4/artist/songs?api_key=<你的api_key>%20&name=guns%20n%27%20roses&format=json&start=0&results=100
token = "<your api key>"
webRequest = urllib.request.Request("http://myapi.com", headers={"token":token})
html = urlopen(webRequest)

from twitter import Twitter#将对应的信息替换成Twitter给出来的信息
t=Twitter(auth=OAuth(<Access  Token>,<Access Token Secret>,<Consumer Key>,<Consumer Secret>))
pythonTweets=t.search.tweets(q="#python")
print(pythonTweets)#打印一个含有#python标签的推文JOSN列表
from twitter import *
t=Twitter(auth=OAuth(Access  Token>,<Access Token Secret>,<Consumer Key>,<Consumer Secret>)))
statusUpdate=t.status.update(status="Hello,world!")#发布推文
print(statusUpdate)
#或区域一组推文的请求，限制条数，请求@montypython推文中按时间排序最靠前的5条推文
pythonStatus=t.statuses.user_timeline(screen_name="montpython",count=5)
print(pythonStatus)

#JOSN数据
import json
from urllib import urlopen
def getCountry(ipAddress):
    response=urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    responseJson=json.loads(response)
    return responseJson.get("country_code")
print(getCountry("50.78.253.58"))

import json
jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],"arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'
jsonObj=json.loads(jsonString)
print(jsonObj)
print(jsonObj.get("arrayOfNums"))
print(jsonObj.get("arrayOfNums")[1])
print(jsonObj.get("arrayOfNums")[1]).get("number")+jsonObj.get("arrayOfNums")[2]).get("number")
print(jsonObj.get("arrayOfFruits")[2]).get("fruit"))

from urllib import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
random.seed(datetime.datetime.now())
def getlinks(articleurl):
   html=urlopen("http://en.wikipedia.org"+articleurl)
   bsObj=BeautifulSoup(html)
   return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
def gethistoryips(pageurl):
    #编辑历史页面url链接格式
    #http://en.wikipedia.org/w/inde.php?title=Title_in_URL&action=history
    pageurl=pageurl.replace("/wiki/","")
    historyurl="http://en.wikipedia.org/w/index.php?title="+pageurl+"&acton=history"
    print("history url is:"+historyurl)
    html=urlopen(historyurl)
    bsObj=BeautifulSoup(html)
    #找出class属性是“mw-anonuserlink”链接
    #它们用ip地址代替用户名
    ipAddresses=bsObj.findAll("a",{"class":"mw-anonuserlink"})
    addresslist=set()
    for ipAddress in ipAddresses:
        addresslist.add(ipAddress)
    return addresslist
links=getlinks("/wiki/Python_(programming_language)")
while(len(links)>0):
    for link in links:
        print("----------")
        historyips=gethistoryips(link.attr["href"])
        for historyip in historyips:
            print(historyip)
    newlink=links[random.randint(0,len(links)-1)].attr["href"]
    links=getlinks(newlink)
def getCountry(ipAddress):
    try:
        response=urlopen("http://freegeoip.net/json/"+ipAddress).read().decode("utf-8")
    except re.HTTPError:
        return None
    responseJson=json.loads(response)
    return responseJson.get("coountry_code")
links=getlinks("/wiki/Python_(programming_language)")
while(len(links)>0):
    for link in links:
        print("-----------")
        historyips=gethistoryips(link.attrs["href"])
        for historyip in historyips:
            country=getCountry(historyip)
            if country is not None:
                print(historyip+" is from "+country)
    newlink=links[random.randint(0,len(links)-1)].attrs["href"]
    links=getlinks(newlink)

#储存文件
from urllib import urlretrieve
from urllib import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.pythonscraping.com")
bsObj=BeautifulSoup(html)
imageLocation=bsObj.find("a",{"id":"logo"}).find("img")["src"]
urlretrieve(imageLocation,"logo.jpg")

import os
from urllib import urlretrieve
from urllib import urlopen
from bs4 import BeautifulSoup
downloadDirectory="downloaded"
baseurl="http://pythonscraping.com"
def getAbsoluteUrl(baseurl,source):
    if source.startswith("http://www."):
        url="http://"+source[11:]
    elif source.startswith("http://"):
        url=source
    elif source.startswith("www."):
        source=source[4:]
        url="http://"+source
    else:
        url=baseurl+"/"+source
    if baseurl not in url:
        return None
    return url
def getDownloadPath(baseurl,absoluteurl,downloadDirectory):
    path=absoluteurl.replace("www.","")
    path=path.replace(baseurl,"")
    path=downloadDirectory+path
    directory=os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path
html=urlopen("http://www.pythonscraping.com")
bsObj=BeautifulSoup(html)
downloadlist=bsObj.findAll(src=True)
for download in downloadlist:
    fileurl=getAbsoluteUrl(baseurl,download["src"])
    if fileurl is not None:
        print(fileurl)
        urlretrieve(fileurl, getDownloadPath(baseurl, fileurl, downloadDirectory))
#编辑csv文件
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import csv
csvfile=open("../file/test.csv","w+")
try :
    writer=csv.writer(csvfile)
    writer.writerow(("number","number plus 2","number times 2"))
    for i in range(10):
        writer.wirterow((i,i+2,i*2))
finally:
    csvfile.close()
#爬取表格数据
import csv
from urllib import urlopen
from bs4 import BeautifulSoup
html=urlopen("https://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj=BeautifulSoup(html)
#主对比表格是当前页面的的第一个表格
table=bsObj.findAll("table",{"class":"wikitable"})[0]
table
rows=table.findAll("tr")
rows
csvfile=open("editors.csv","wt")
writer=csv.writer(csvfile)
try:
    for row in rows:
        csvRow=[]
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
            writer.writerow(csvRow)
finally:
    csvfile.close()

html=urlopen("https://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj=BeautifulSoup(html)
bsObj.find("h1").get_text()
bsObj.find("h1")

#Mysql链接
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pymysql
conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='S13227mcj',db='mysql')
cur=conn.cursor()
cur.execute("USE scraping")
cur.execute("select * from page where id=123")
print(cur.fetchone())
cur.close()
conn.close()

from urllib import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql
conn=pymysql.connect(host="localhost",port=3306,user='root',passwd="S13227mcj",db="mysql")
cur=conn.cursor()
cur.execute("Use scraping")
random.seed(datetime.datetime.now())
def create(table):
    cur.execute("CREATE TABLE %s (title varchar(100) primary key,content varchar(100));"%table)
    cur.connection.commit()
def store(title,content):
    cur.execute("INSERT INTO pages(title,content) Values(\"%s\",\"%s\");"%(title,content))
    cur.connection.commit()
def getlinks(articleurl):
    html=urlopen("https://en.wikipedia.org"+articleurl)
    bsObj=BeautifulSoup(html)
    title=bsObj.find("h1").get_text()
    content=bsObj.find("div",{"id":"mw-content-text"}).find("p").get_text()
    store(title,content)
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
create("pages")
links=getlinks("/wiki/Kevin_Bacon")
try:
    while len(links)>0:
        newArticle=links[random.randint(0,len(links)-1)].attrs["href"]
        print(newArticle)
        links=getlinks(newArticle)
finally:
    cur.close()
    conn.close()
html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html)
bsObj.find("div",{"id":"mw-content-text"}).find("p").get_text()

from bs4 import BeautifulSoup
import re
import pymysql
conn=pymysql.connect(host="localhost",port=3306,user='root',passwd='S13227mcj',db='mysql')
cur=conn.cursor()
cur.execute("Create database wikipedia;")
cur.execute("USE wikipedia;")
cur.execute("Create table pages (url varchar(100) primary key not null);")
cur.execute("Create table links(frompageid int not null,tooageid int not null);")
def insertpageifnotexists(url):
    cur.execute("select * form pages where url=%s;",(url))
    if cur.rowcount==0:
        cur.execute("Insert into pages (url) value (%s)",(url))
        conn.commit()
        return cur.lastrowid
    else:
        cur.fetchone([0])
def insertlink(frompageid,topageid):
    cur.execute("select * from links where frompageid=%s and topageid=%s",(int(frompageid),int(topageid)))
    if cur.rowcount==0:
        cur.execute("Insert into links(from pageid,topageid) values (%s,$s)",(int(frompageid),int(topageid)))
        conn.commit()
pages=set()
def getlinks(pageurl,recursionlevel):
    global pages
    if recursionlevel>4:
        return;
    pageid=insertpageifnotexists(pageurl)
    html=urlopen("http://en.wikipedia.org"+pageurl)
    bsObj=BeautifulSoup(html)
    for link in bsObj.findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
        insertlink(pageid,insertpageifnotexists(link.attrs["href"]))
        if link.attrs["href"] not in pages:
            #遇到一个新页面，加入集合并搜索里面的词条链接
            newpage=link.attr["href"]
            pages.add(newpage)
            getlinks(newpage,recursionlevel+1)
getlinks("/wiki/Kevin_Bacon",0)
cur.close()
conn.close()















