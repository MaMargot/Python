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
[1,2,3]+[4,5,6]#相加连接
[1,2,3,4]+1#错误
import numpy as np
a = np.array([1,2,3,4])
b = np.array([7,8,9,10])
s = a + b #将序列转换为数组，才能够实现序列的相加
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
对象.方法(参数)#列表方法
lst.append(4)#在表尾添加新对象，直接修改原表
lst.count(1)#统计某个元素在列表出现的次数
a=[1,2,3]
b=[4,5,6]
a.extend(b)
a#实现多个值的连接，同时更改了原列表
a[len(a):]=b #也可以实现
knight=['We','are','the','knight','who','say','ni']
knight.index('we')#通过index查找元素，区分大小写
number=[1,2,3,4,5,6]
number.insert(3,'Four')#插入元素(指定位置-索引)
number[3:3]='four'#亦可以实现
x.pop()#移除列表中的一个元素，（指定位置-索引）,采用类似于栈的做法
x.remove('be')#移除列表中的某个值的第一个匹配项,没有返回值
x.reverse()#将列表元素方向存放
x=reverse(x)
list(x)#同样可以实现，但reverse返回的是一个迭代对象，而非一个列表
x.sort()#对列表进行排序，改变原来的列表
y=x.sort()#并不能返回一个排序后的列表，返回的是NONE
y=sorted(x)#则可以实现
cmp(x,y)#x>y,返回正值，x=y返回0，x<y返回负值
number.sort(cmp)#可定义一个比较函数，用于排序
x.sort(key=len)
x.sort(reverse=True)
1,2,3#(1,2,3)属于元组，元组内元素不可以改变
()#空元组
42,#才能创建一个元组
3*(12*4,)#逗号是区分元组的主要部分
tuple()#将参数转换为元组
x[1]#元素
x[0:2]#元组
website='http://www.python.org'
website[-3:]='com'#字符串的都是不可变的
format='Hello,%s.%s enough for ya?'
value=('world','Hot')#一般情况下用元组,只有元组和字典可以格式化一个以上的值，如果格式化字符串中有百分号，则必须用%%
print format%value
format='pi with three decimals : %.3f'
from string import Template
s=Template('$x , glorious %x !')
s.substitute(x='slurm') #模板字符串
s=Template('It\'s  ${x}tastic')#替换单词的一部分
s=Template('Make $$ selling $x')#使用美元符号
s=Tempalte('A $thing must never $action')
d={}
d['thing']='gentlman'
d['action']='show his socks'
s.substitute(d) #可以使用字典的值/名称对
'%s plus %s equals %s'%(1,2,3)# 必须用圆括号括起
'price of egg : $%d'% 2 #表示正数需在前面加上空格
'%.5s'%'Gido van rossum' #若是字符串则决定字符串的最大字符串长度
'%10.2f'%pi #+向右对齐，-向左对齐
'%010.2f'%pi #用0填充
print('% 5d'% 10)+'\n'+('% 5d'% -10)
'With a moo-moo here. and a moo-moo there '.find('moo')#返回子串所在位置的最左端索引，没有找到则返回-1
subject='$$$ Get rich now !!! $$$'
subject,find('$$$')#in操作符只能查询单个字符
subject.find('!!!',0,16)#提供起始位和结束位
seq=[1,2,3,4]
sep='+'
sep.join(seq)#报错，不能连接数字列表
seq.split(sep)#分割
'Using the default'.split()#不提供分割符时，把所有空格当分隔符
'Trondheim'.lower()#小写
'that\'s all folks'.title()#开头大写
'This is a test'.replace('is','eez')#替换
'   Inter whitespace    '.strip()#提出头尾的空格
'* Inter ** fro **!!!'.strip(' *!')#可提供参数剔除
from string import maketrans
table =maketrans('cs','kz')#在使用translate之前要先完成转换表
'This is an icredible test '.translate(table,' ')#translate每次能替换多个单字符，仅能替换单字符，第二个参数是用于删除需要删除的字符
phonebook={'Alice':'2341','Beth':'9012','Cecil':'32580'}#创建字典
items=[('name','Gumby'),('age',32)]#dict-列表内的元组键值对应
d=dict(items)
d['name']
x=[] #键可以为任何不可变类型
x[42]='foolar'
x={}
x[42]='foolar'#键具有自动添加功能,可以有子健
people={'Alice':{
    'phone':'2341'
    ,'adress':'foo drive 23'},
    'Beth':{
        'phone':'9102'
        ,'address':'bar street 42'
    }
}
phonebook={'Beth':'9210',
           'Alice':'2314',
           'Ceil':'2358'}
"Cecil's phone number is %(Ceil)s"%phonebook #格式化字符串，此处键的格式化用元组表示
return_value=d.clear()#clear方法清除字典中的所有项，且无返回值
#下面注意
x={}
y=x
x['key']='value'
x={}
y#在将x关联到一个空字典上时，y不会改变
x.clear()
y#如果想要清除原字典所有元素时，必须用clear方法
x={'usrname':'admin','machines':['foo','bar','baz']}
y=x.copy()#浅复制
y['usrname']='mlh'
y['machines'].remove('baz')
y#在副本中替换值时，原始字典不受影响
x#在副本中修改某个值时，原字典也会改变
from copy import deepcopy
d={}
d['name']=['Alfred','bertand']
c=d.copy()
dc=deepcopy(d)#深复制，复制其包含的所有值，且不受更改的影响
d['name'].append('Clive')
c
dc
#
{}.fromleys(['name','age'],'(unknown)')#使用给定键建立新的字典，每个键的默认值为None,可自己设置
print d.get('named')#试图访问字典中不存在的项时不会报错
d.get('name','N/A')#使用get访问一个不存在的键时，会返回None,可设置默认值替换None
d.items()#将字典以列表形式返回
d.iteritems()#返回列表的迭代器
list(d.iteritems())#返回列表
d.pop('x')#获得对应键的值，并将键对从字典中剔除
d.popitem()#弹出随即项
d={}
d['name']='Gumby'
d.setdefault('name','N/A')#可以在字典中不含有定键的情况下设定相应的键值
d.update(x)#可以用一个字典更新另一个字典
d.values()#以列表的形式返回字典中的值（itervalues返回迭代器），返回列表中可以包含重复元素









