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
print 'age:',42
print 1,2,3
print (1,2,3)
print greeting,',',saluation,name #逗号前会加空格
print greeting+',',saluation,name
from somemodule import somefunction,anotherfunction,yetanotherfunction
from somemodule import *
module1.open()
module2.open()#多个模块同时含有相同函数的处理方法
import math as foobar#提供模块别名
foobar.sqrt(4)
from math import sqrt as foobar#提供函数别名
foobar(4)
x,y,z = 1,2,3#序列解包
print x,y,z
x,y=y,x
values=1,2,3
x,y,z=values
scoundrel={'name':robin,'girlfriend':'marion'}
key,value=scoundrel.popitem()
x=y=somefunction()#链式赋值，不等价于x=function,y=x
x+=2#增量赋值
x*=2
x+='foor'
False ,None,"",[],{},()#均被默认为false
bool("")
num=input('Enter a number:')
if num>0:#循环语句
    print 'The number is positive'
elif num<0:
    print 'The number is negative'
else :
    print 'The number is zero'
x=y=[1,2,3]
z=[1,2,3]
x==y#相等性运算符
x==z
x is y
x is z#同一性运算符is
'alpha'<'beta'
age=-1
assert 0<age<100 #断言
assert 0<age<100,'The age must be realistic'
name=''
while not name.strip():
    name=raw_input('Please Enter your name: ')
print 'Hello,%s'%name
words=['this','is','an','ex','parrot']
for word in words:
    print word
for num in range(0,101):#xrange()可以一次创建一个数
    print number
for key,value in d.items():
    print key,'corresponds to ',value
names=['anne','beth','george','damn']
ages=[12,45,32,102]
zip(names,ages)#压缩两个序列
for name,age in zip(names,ages):
    print name ,'is',age,'years old'
zip(range(5),xrange(1000000))#对付不等长的序列时，当最短的序列'用完'就会停止
for index,string in enumerate(strings):#在提供索引的地方迭代索引-值对
    if 'xxx' in string:
        strings[index]='[censored]'
list(reversed('Hello,World'))#reversed返回的是迭代对象
from math import sqrt
for n in range(99,81,-1):
    root=sqrt(n)
    if root == int(root):
        print n
        break
else:#使用在循环语句中的else
    print "Didn't find it "
[x*x for x in range(10)] #列表推导式，轻量循环
[x*x for x in range(10) if x%3==0]
[(x,y) for x in range(3) for y in range(3)]
scoundrel={'age':42,'frist name':'robin','last name ':'of locksley'}
robin=scoundrel
scoundrel=None
robin=None#此时python删除该字典
x=1
del x#不仅移除一个对象的引用，也会移出那个名字的本身
exec "print 'Hello,World!'"#exec执行字符串
from math import sqrt
scope={}#放置代码字符创命名空间
exec "sqrt=1" in scope
sqrt(4)
scope[sqrt]
len(scope)
scope.keys()#内建函数和值
eval(raw_input("Enter an arithmetic expression:"))#计算以字符串形式书写的表达式
import math
y=math.sqrt
callable(y)#用来检查调用函数是否可用
def hello(name):
    print 'hello '+name
    return 'hello'+name
hello('peter')
def square(x):
    'Calculates the square of the number x'#文档字符串
    return x*x
square.__doc__
help(square)
def change(n):
    n[0]='Mr.Gumby'
names=['Mr.Entity','Mrs.Thing']
change(names)
names#字符串和元组无法被改变，只能用新值覆盖，而可变数据结构，若是替换部分值，则会改变，可参考copy
n=names[:]#切片总是副本
n is names
n==names
storage={}#改变数据结构
my_sisiter='Anne Lie Hetland'
storage['frist'].setfault('Anne',[]).append(my_sisiter)
storage['second'].setfault('Lie',[]).append(my_sisiter)
storage['last'].setfault('Hetland',[]).append(my_sisiter)
def init(data):
    data['first']={}
    data['second']={}
    data['last']={}
def lookup(data,label,name):
    return data[label].get(name)
def store(data,full_name):
    names=full_name.split()
    if len(name)==2: names.insert(1,' ')
    labels='first','middle','last'
    for label,name in zip(lables,names):
        people = lookup(data,label,name)
        if people:
            people.append(full_name)#!!!利用了可变数据结构的性质
        else :
            data[label][name]=[full_name]
def inc(x): return x+1
foo=10
foo=inc(foo)#若想返回多个值，用元组的形式返回
foo=[10]
inc(foo)#此处同样用了可变数据类型的性质
def hello_world1(greeting,name):
    print '%s,%s'%(greeting,name)
hello_world1(greeting='hello',name='world')#关键字参数
def hello_world2(greeting='HELLO',name='WORLD'):#提供默认值
    print '%s,%s'%(greeting,name)
def print_params(title,*params):#收集其余的位置参数，返回元组
    print title
    print params
print_params('titile:',(1.2,3))
print_params('title')
print_params('humm',somthing=2)#不能处理关键字参数
def print_params1(x,y,z=3,*pospar,**keypar):#另外一个收集位置参数，返回字典
    print x,y,z
    print pospar
    print keypar
def add(x,y): return x+y
params=(1,2)
add(*params)#反转过程
params={'name':'sir robin','greeting':'Well met'}
hello_world2(**params)
x=1
scope=vars()#一般来说，vars()返回的字典是不能修改的
scope['x']
scope['x']+=1#
x
def combine(parameter):print parameter+external
external='berry'
combine('shurb')#函数内读取全局变量
def combine(parameter):print parameter+globals()['parameter']#正确调用全局变量的方法，相应地局部为locals
parameter='berry'
combine('shrub')
x=1
def change_global():
    global x #重绑定全局变量
    x=x+1
from random import choice
x=choice(['Hello,world!',[1,2,'e','e',4]])
x.count('e')#方法
def add(x,y):
    return x+y
add(1,2)
add('Fish','License')
o=OpenObject()#This is how we create objects，将变量绑定到对象上，在用全局变量写下类的情况下
o.setName('Sir Lancrlot')
o.getName
globalName=o.getname()#如果o变量的存储在全局变量globalName中
globalName='Sir Gumby'#全局变量发生变化时，变量也发生改变，不得不关心globalName的内容，要确保不会对变量进行任何更改
o.getName()
o1=OpenObjects()
o2=OpenObjects()
o1.setName('Robin Hood')
o2.getName()#设置多个OpenObjects实例时，因为变量相同，可能会发生混淆，此例中，设定一个名字后，其他的名字也自动设定
c=CloseObject()#在用特性重写类的情况下，特性即对象的内部变量，封装在对象内
c.SetName('Sir Lancelot')
c.getname()
r=CloseObject()
r.setName('Sir Robin')#方法改变的是对象的内部特性，而非全局变量
r.getName()
c.getName()
##重要：关于类
__metaclass__=type #确定使用新式类
class Person:
    def setName(self,name):#self是方法与函数的区别，方法可以将他们的第一个参数绑定到所属的实例上
        self.name=name
    def getName(self):
        return self.name
    def greet(self):
        print "Hello,world!I'm %s."%self.name
foo=Person()
bar=Person()
foo.setName('Luke Skywalker')
bar.setName('Anakin Skywalker')
foo.greet()
bar.greet()
foo.name
bar.name='Yoda'#特性可以外部访问
bar.greet()
__metaclass__=type
class Class:
    def method(self):
        print 'i have a self!'
def function():
    print 'i don\'t'
instance=Class()#其实是一个实例
instance.method()
instance.method=function()
instacne.method
class Bird:
    song='Squaawk'
    def sing(self):
        print self.song
bird=Bird()
bird.sing()
birdsong=bird.sing#变量绑定到绑定方法上，它仍旧绑定在类的相同实例上
birdsong()
c.getName
c.name='Sir Gumby'#从程序外部访问一个对象特性
c.getname()
class Secretive:
    def __inaccessible(selfself):#通过增加双下划线，可以讲方法或者特性变为私有化
        print "Bet you can't see me ..."
    def accessible(selfself):
        print "the secret message is "
        self.__inaccessible
s=Secretive()
s.__inaccessible()
s.accessible()
s._Secretive__inacccesible()#在类的内部定义中，所有的双下划线都被翻译成了单下划线，实际还是可以在类外访问的
def foo(x):return x*x
foo=lambda x:x*x#上下等价
class C :
    print "Class C being defined"
class MemberCounter:
    members=0#定义一个可供所有成员（实例）访问的变量
    def init(self):
        MemberCounter.members+=1
m1=MemberCounter()
m1.init()
MemberCounter.members
m2=MemberCounter()
m2.init()
MemberCounter.members#类内的变量可以被所有实例访问
m1.members='Two'
m1.members#重！！！绑定members的特性，屏蔽了类范围内的变量
m2.members
class Filter:
    def init(self):
        self.blocked=[]
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked ]
class SPAMFilter(Filter):#SPAMFilter是Filter的子类
    def init(self):#重写Filter超类中的init方法
        self.blocked=['SPAM']
f=Filter()
f.init()
f.filter([1,2,3])
s=SPAMFilter()
s.init()
s.blocked=['SPAM','SPAM','SPAM','EGGS','bacons']
issubclass(Filter,SPAMFilter)#查看一个类是否另一个类的子类
issubclass(SPAMFilter,Filter)
SPAMFilter.__bases__#利用特殊特性查看基类
Filter.__bases__
s=SPAMFilter
isinstance(s,SPAMFilter)#查看一个对象是否一类的实例
isinstance(s,Filter)
isinstance(s,str)
s.__class__#查看对象属于哪个类
class Calculator:
    def calculate(self,expression):
        self.value=eval(expression)
class Talker:
    def talk(self):
        print "Hi,my value is ",self.value
class TalkingCalculator(Calculator,Talker):#多个超类
    pass
tc=TalkingCalculator()
tc.calculate('1+2*3')
tc.talk()#多重继承，如果一个方法从多个超类继承，要注意超类的顺序，先继承的方法会重写后继承的方法
hasattr(tc,'talk')#检查所需方法是否存在
hasattr(tc,'fnord')
callable(getattr(tc,'talk',NONE))
callable(getattr(tc,'fnord',None))
setattr(tc,'name','Mr.Gumby')#设置变量特性
#__dict__,可以查看对象内所有存储的值
#inspect模块，可以找到对象由什么组成

#异常
raise Expection
raise Expection("hyperdrive overload")
import exceptions
dir(exceptions)
raise ArithmeticError
x=input('Enter the first number:')
y=input('Enter the second number:')
print x/y
try:#捕获异常
    x=input('Enter the first number:')
    y=input('Enter the second number:')
    print x/y
except ZeroDivisionError:
    print "The second number can't be zero"
class MuffledCalculator:
    muffled = False
    def calc(self,expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print 'Division by zero is illegal'
            else:
                raise
calculator=MuffledCalculator()
calculator.calc("10/2")
calculator.calc("10/0")
calculator.muffled=True
calculator.calc("10/0")
try:
    x = input('Enter the first number:')
    y = input('Enter the second number:')
    print x / y
except ZeroDivisionError:
    print "The second number can't be zero"
except TypeError:#多条except捕获异常
    print "That wasn't a number ,was it?"
try:
    x = input('Enter the first number:')
    y = input('Enter the second number:')
    print x / y
except (ZeroDivisionError,TypeError,NameError):#一个块捕获两个异常
    print "Your number were bugs...."
try:
    x = input('Enter the first number:')
    y = input('Enter the second number:')
    print x / y
except (ZeroDivisionError,TypeError) ,e:#在expect字句中访问异常本身，就算是捕获到多个异常，也只需要向except提供一个元组
    print e
try :
    print "A simple task"
except :#except子句中忽略所有异常类，可以捕捉所有异常，但会隐藏错误、捕获用户终止执行的命令
    print "what? somthing went wrong?"
else:
    print "ah....it went as planned"

while True:
    try :
        x = input('Enter the first number:')
        y = input('Enter the second number:')
        value= x / y
        print 'x/y is ',value
    except :
        print 'Invalid input .please try again'
    else:
        break

while True:
    try :
        x = input('Enter the first number:')
        y = input('Enter the second number:')
        value= x / y
        print 'x/y is ',value
    except Exception,e:
        print 'Invaild input:',e
        print 'please try again'
    else:
        break
x=None
try:
    x=1/0
finally:
    print 'Cleaning up.....' #不管try子句是否发生异常
    del x

try:
    x=1/0
except NameError:
    print "Unknow varibale"
else:
    print "That went well"
finally:
    print 'Cleaning up.....' #不管try子句是否发生异常

def default():
    rasie Exception("Something is wrong")
def ignore_exception():
    faulty()
def hanle_exception():
    try:
        faulty()
    except:
        print 'Exception handled'
ignore_exception()
hanle_exception()

def describePerson(person):
    print 'Description of ',person['name']
    print 'Age:',person['age']
    try:
        print 'Occupation: '+person['occupation']#此处使用加号而不是逗号，防止occupation在异常引发前被打印出来
    except KeyError:
        pass

try:
    obj.write
except AttributeError:
    print 'The object is not writeable'
else:
    print 'The object is writeable'

#魔法方法、属性和迭代器
class FooBar:
    def __init__(self):#当一个对象被创建后，会立即调用构造方法
        self.somevar=42
f=FooBar()
f.somevar
class FooBar:
    def __init__(self,value=42):
        self.somevar=value
f=FooBar("This is a construct argument")
f.somevar
class A:
    def hello(self):
        print "hello,I'm A"
class B(A):
    pass
a=A()
b=B()
a.hello()
b.hello()
class B(A):
    def hello(self):
        print "hello,I'm B"
b=B()
b.hello()
class Bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print "Aaaah...."
            self.hungry=False
        else:
            print 'No.thanks'
b=Bird()
b.eat()
b.eat()
class SongBird(Bird):
    def __init__(self):
        self.sound("Squawk")
    def sing(self):
        print self.sound
sb=SongBird()
sb.sing()
sb.eat()#在SongBird中，构造方法被重写，但新的构造方法没有任何关于初始化hungry的代码，必须调用超类构造方法未绑定版本或使用super

class SongBird:
    def __init__(self):
        Bird.__init__(self)
        self.sound='Squawk'
    def sing(self):
        print self.sound
sb=SongBird()
sb.sing()
sb.eat()
sb.eat()

__metaclass__=type
class Bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print "Aaaa...."
            self.hungry=False
        else :
            print "No,thanks"
class SongBird(Bird):
    def __init__(self):
        super(SongBird,self).__init__()
        self.sound = 'Squawk'
        def sing(self):
            print self.sound
sb=SongBird()
sb.sing()
sb.eat()
sb.eat()

def checkIndex(key):
    """
    所给的键是能接受的索引吗？
    为了能被接受，键应该是一个非负整数，会引发TypeError；如果它是负数，则会引发一个IndexError （因为序列是无限长的）
    """
    if not isinstance(key,(int,long)) : raise TypeError
    if key<0: raise IndexError
class ArithmeticSequence:
    def __init__(self,start=0,step=1):
       """
       初始化算术序列
        起始值——序列中的第一个值
        步长--两个相邻值之间的差别
        改变——用户修改的值的字典
       """
    self.start=start #保存开始值
    self.step=step #保存步长值
    self.change={} #没有被修改项
    def __getitem__(self,key):
        """
        Get an item from arithmetic sequence
        """
        checkIndex(key)
        try :
            return self.change[key] #修改了吗
        except KeyError:#否则....
            return self.start+key*self.step #....计算值
    def __setitem__(self, key, value):
        """
        修改算术序列中的一个值
        """
        checkIndex(key)
        self.change[key]=value #保存更改后的值
s=ArithmeticSequence(1,2)
s[4]
s[4]=2
s[5]
s["four"]
s[-42]
class CounterList(list):#子类化内建类型
    def __init__(self,*args):
        super(CounterList,self).__init__(*args)
        self.counter=0
    def __getitem__(self, index):
        self.counter+=1
        return super(CounterList,self).__getitem__(index)
C1=CounterList(range(10))
C1
C1.reverse()
C1
del C1[3:6]
C1.counter()
C1
C1[4]+C[2]
C1.counter()
class Rectangle:
    def __init__(self):
        self.width=0
        self.heigth=0
    def setsize(self,size):
        self.width,self.hight=size
    def getsize(self):
        return self.width,self.height
r=Rectangle()
r.width=10
r.hight=5
r.getsize()
r.setsize((150,100))
#新式类中的property，创建特殊属性
__metaclass__=type
class Retangle:
    def __init__(self):
        self.width=0
        self.heigth=0
    def setSize(self,size):
        self.width,self.heigth=size
    def getsize(self):
        return self.width,self.heigth
    size=property(getsize,setsize)
r=Rectangle()
r.width=10
r.heigth=5
r.size
r.size=150,100#property函数创建了一个属性size，其中访问器函数被用作参数（先是取值，然后是赋值）
r.width
#静态方法和类成员方法,classmethod必须有一个指向类对象的引用作为第一个参数而staticmethod可以没有任何参数
__metaclass__=type
class Myclass:
    def smeth():
        print "This is a static method"
    smeth=staticmethod(smeth)
    def cmeth(cls):
        print "This is a class method of ",cls
    cmeth=classmethod(cmeth)
#修饰器
__metaclass__=type
class Myclass:
    @staticmethod
    def semth():
        print "This is a static method"
    @classmethod
    def cmeht(cls):
        print "This is a class method of ",cls
Myclass.smeth()
Myclass.cmeth()
class Rectangle:
    def __init__(self):
        self.width=0
        self.height=0
    def __setattr__(self,name,value):
        if name=='size':
            self.width,self.width=value
        else:
            self.__dict__[name]=value##此处采用__dict__是为了避免__setattr__再次被调用，导致程序进入死循环
    def __getattr__(self, name):##__getattr__会拦截所有的特性的访问，也会拦截对__dict__的访问，访问__getattribute__中与self相关特性时，使用超类__getattribute__方法（使用super）时唯一的安全途径
        if name=='size':
            return self.width,self.height
        else:
            raise AttributeError
class Fibs:
    def __init__(self):
        self.a=0
        self.b=1
        self.n=0
    def next(self):##相当于__next__的存在
        self.a,self.b=self.b,self.a+self.b
        return self.a
    def call(self):
        self.n=self.n+1
        return self.n
    def __iter__(self):
        return self
fibs=Fibs()
fibs
for f in fibs:
    if f>1000:
        print f
        break
it=iter({1,2,3})
it.next()
it.next()
class TestIterator:
    value=0
    def next(self):
        self.value+=1
        if self.value>10:
            raise StopIteration
        return self.value
    def __iter__(self):
        return self
ti=TestIterator()
list(ti)##使用list构造方法显式地将迭代器转化为列表
nested=[[1,2],[3,4],[5]]
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element#包含yield的语句生成器,每次产生多个值，每次产生一个值，函数就会被冻结，即函数停在那点等待被激活
for num in flatten(nested):
    print num
list(flatten(nested))
g=((i+2)**2 for i in range(2,27))#返回的是生成器，与列表推导式不同在于，其用圆括号
g.next()
sum(i**2 for i in range(10))#生成器推导式可在当前圆括号内使用
def flatten(nested):#递归生成器，若nested为字符串，会产生两个问题:1、类似于字符串对象当成原子值，而不是一个应当展开的对象；2、迭代实际上会产生无穷递归，一个字符串的第一个元素是另一个长度为1的字符串，而长度为1的字符创的第一个元素是字符串本身
    try :
        for sublist in nested:
            for element in sublist:
                yield element
    except  TypeError:
        yield nested#避免对一个元素进行迭代
list(flatten([[[1],2],3,4,[5,[6,7]],8]))
def flatten(nested):
    try:
        try: nested +''
        except TypeError: pass
        else: raise TypeError
        for sublist in nested:
            for element in sublist :
                yield element
    except TypeError:
        yield nested
list(flatten(['foo',['bar',['baz']]]))
def simple_generator():#生成器的函数部分
    yield 1#生成器的迭代部分
simple_generator
simple_generator()
#生成器方法
#1、外部作用域访问生成器的send方法，就像访问next方法一样，只不过前者使用一个参数
#2、在内部则挂起生成器，yield现在作为表达式而不是语句使用，换句话说，当生成器重新运行的时候，yield方法返回一个值，也就是外部通过send方法发送的值。当next方法，nameyield方法返回None
#使用send方法(而不是next方法)只有在生成器挂起之后才有意义（也就是在yield函数第一次被执行之后）
#入股真想对刚刚启动的生成器使用send方法，那么可以将None作为其参数调用
def repeater(value):
    while True:
        new=(yield value)#注意yield表达式的使用
        if new is not None: value=new
r=repeater(42)
r.next()
r.send("Hello,world!")
#throw 方法（使用异常类型的调用，还有可选的值以及回溯对象）用于在生成器中引发一个异常（在yield表达式中）
#close方法（调用时不用参数），用于停止生成器,也是建立在异常的基础上
r=repeater([1,[3,4]])
r.next()
r.send("hell,world")
r
r.next()
def flatten(nested):#普通函数版本
    result=[]
    try:#不要迭代类似字符串的对象
        try:
            nested+" "
        except TypeError: pass
        else: raise TypeError
        for sublist in nested :
            for element in sublist:
                result.append(element)
    except TypeError:
        result.append(nested)
    return result
#re模块
#通配符：
#（.）可以匹配任何字符串（除了换行符），只能匹配一个字母
#（\\）双反斜杠，进行转义，也可以用r'...'原始字符串减少为单反斜杠
#[a-zA-Z0-9]字符集，匹配a-z，A-Z，0-9的任意一个字符，只能匹配一个这样的字符
#（^）脱字符，匹配除内容外的字符，[^abc]
#（|）管道字符，匹配选定的特殊字符，如：'python|perl'
#（），子模式，也适用于单个字符如：'p(ython|erl)'
#?,可选项，如r'(http://)?(www\.)python\.org'
#(pattern)*:允许模式重复0次或多次；
#(pattern)+:允许模式重复1次或多次；
#(pattern){m,n}:允许模式重复m-n次；如：r'w*\.python\.org'
#如果想在字符串开头，而不是其他位置匹配,可以用（^）脱字符标记开始，'^ht+p'会匹配'http://python.org'及其他类似的
#如果想在字符串结尾，则用（$）符号
import re
some_text="alpha, beta,,,,ganma delta"
re.split('[, ]+',some_text)
re.split('o(o)',foobar)
re.split('[, ]+',some_text,maxsplit=2)
re.split('[, ]+',some_text,maxsplit=1)
pat='[a-zA-Z]+'
text='"Hm...Err--are you sure?"he said ,sounding insecure'
re.findall(pat.text)
pat=r'[.?\-",]+'#-被转义了，不会被当a-z
re.finall(pat,text)
s = "aa bb aaa bbb aabbcc aaabbb  abab ababab"
re.findall('(ab).*?',s)  #同时匹配ab
re.findall('(ab).*',s)  #同时匹配ab
re.findall('(ab).',s)  #同时匹配ab
re.findall('(ab)',s)  #同时匹配ab
pat='{name}'
text='Dear {name}'
re.sub(pat,'Me.Gumby',text)#替换最左端并且非重叠的子字符串
re.compile('[^abc]')#根据包含正则表达式的字符串创建模式对象
if re.search(pat,string):#在字符串中寻找模式
    print 'Found it'
re.escape('www.python.org')
re.escape("But where is the ambiguity")#将字符串中的所有特殊正则表达式字符转义
m=re.match(r'www\.(.*)\..{3}','www.python.org')
m.group(1)#返回模式中与给定组匹配的子字符串
m.statr(1)#返回给定匹配项的开始索引
m.end(1)#返回结果是结束索引+1
m.span(1)#以元组形式放回定组的开始和结束位置索引，默认为0，即整个模式
emphasis_pattern=r'\*([^\*]+)\*'
emphasis_pattern=re.compile(r'''
    \* #beginning emphasis tag -- an asterisk
    (  #begin group for capture pharse
    [^\*]+ #capture anything except asterisks
    ) #End group
    \* #ending emphasis tag
    ''',re.VERBOSE) #re.VERBOSE允许模式中添加空白（空白字符、tab、换行符等等）
re.sub(emphasis_pattern,r'<em>\1</em>','hello,*world*!')#在替换字符串中使用组号(很重要)
emphasis_pattern=r'\*(.+)\*'#重复运算符默认是贪婪地，会尽可能多的匹配
re.sub(emphasis_pattern,r'<em>\1</em>','*This* is *it*! ')
emphasis_pattern=r'\*\*(.+?)\*\*'#用+？来替换+，他会尽可能少的匹配
re.sub(emphasis_pattern,'r\*\*<em>\1<em>','**This **is **it**!')
#find_sender.py,寻找Email发信人
import fileinput,re
pat=re.compile(r'From:(.*)<.*?>$')
for line in fileinput.input():
    m=pat.match(line)
    if m:print m.group(1)
#寻找表头的发信人
import fileinput,re
pat=re.compile(r'[a-z\-\.]+@[a-z\-\.]+',re.IGNORECASE)#忽略大小写
addresses=set()#集合
for line in fileinput.input():
    for address in pat.findll(pat.line):
        addresses.add(address)
    for address in sorted(addresses):
        print address
#模板系统
#template.py
import fileinput,re
#匹配中括号里的字段
field_pat=re.compile(r'\[.+?\]')
#将变量收集到这里
scope={}
#用于re.sub中
def replacement(match):
    code=match.group(1)
    try :
        #如果字段可以求值，则返回他
        return str(eval(code,scope))
    except SyntaxError:
        #否则执行相同域内的赋值语句
        exec code in scope
        #.......返回空字符串
        return ''
#将所有文本以一个字符串形式获取：
#还有其他方法，参见第11章
lines=[]
for line in fileinput.input():
    lines.append(line)
text=' '.join(lines)
#将field魔石的所有匹配项都替换掉
print field_pat.sub(replacement,text)












