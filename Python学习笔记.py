#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 9:36
# @Author  : Ryu
# @Site    : 
# @File    : Python学习笔记1.py
# @Software: PyCharm

#格式化输出：
print('%d'%x)
#值转换为字符串的两种机制
print repr("Hello,world")   #合法的python表达式形式
print repr(10000L)   #可用``反引号代替, 如：
print 'The Temperature is'+ `temp`  #temp可以为一个变量
print str("Hello,world")  #合理的形式的字符串
print str(10000L)
#ceil()和floor()、round()、int()
#字符串连接
x='x'
y='y'
print x+y
#数据输入
name=input('What is your name') #输入的字符串没有引号时会报错
print "Hello,"+name+'!'
name=raw_input("what is your name ")#可以自动将格式转化为字符串
#长字符串用'''开头和结尾
print '''This is a very long string.
It continues here.
And it's over yet.
'Hello woorld '
still here .'''
print "HELLO,\
      WORLD" #同样可以实现
#原始字符串
print 'HELLO,\nWORLD'
print 'c:\\nowhere' #使用反斜杠避免被转义
print r'c:\nowhere'
print r'This is illlegal \' #最后一个字符不能够是反斜杠
#unicode字符串
u'HELLO,WORLD'
#列表与元组的区别在于：列表可以修改，而元组不可以修改
edward=['Edward Gumby',42]#列表
(a.b)#元组
john=['John smith',32]
database=[edward,john]
database
greeting='Hello'
greeting[0]#序列的索引从0开始，使用负数时从右边开始
number=[1,2,3,4,5,6,7]
number[0:1]#第一个索引元素包含在分片内，第二个元素不包含在分片内
number[-3:0]#报错，实际上分片最左边的索引比它右边的晚出现在序列，会出现空序列
number[-3:]#只需空置最后一个索引即可
number[::1]#设置步长
number[7:3:-1]#步长可以为负数，即从右边往左边取
number[0:10:-2]#空序列
[1,2,3]+[4,5,6]
[1,2,3]+'world'#同类型的序列才能相加
'python'*7
[42]*7
[None]*10 #意味着产生了一个没有在里面放置元素的序列
permission='ws'
'x' in permission
users=['mhl','foo','bar']
raw_input("What your name:") in users
list('Hello')#列表
' '.join('hello')
x[1]=2#列表复制
names=['Alice','Beth','Cecil','Dee-Dee','Earl']
del names[2]#采用del语句删除元素
name=list('Perl')
name[2:]=list('ar')
name[2:]=list('ython')#可以使用不等长赋值
name[1:1]=list('a')#在不替换元素下插入新元素
name[2:3]=[]#通过分片赋值来删除元素




