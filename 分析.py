#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/26 10:42
# @Author  : Ryu
# @Site    : 
# @File    : 分析.py
# @Software: PyCharm

#NumPy库,高性能科学计算和数据分析的基础包，目的在于更高效地辅助使用数据分析功能
#ndarray是一个通用的同构数据多维容器,其中shape表示各维度的数组，dtype用于说明数组数据类型的对象
import numpy as np
data1=[6,7.5,8,1,0]
arr1=np.array(data1)
arr1*10
data1*10
arr1+arr1
data1+data1
arr1.shape
arr1.dtype
data2=[[1,2,3,4],[5,6,7,8]]
arr2=np.array(data2)
arr2#嵌套序列将转换为一个多维数组
arr2.ndim
arr2.shape
data3=[[1,2,3,4],[5,6,7]]#!!!
arr3=np.array(data3)
arr3
arr3.ndim
arr3.shape#!!!
np.zeros(10)
np.zeros((3,10))
np.ones((3,10))
np.empty((2,3,2))
np.arange(15)
arr1=np.array([1,2,3],dtype=np.float64)#dtype是一个特殊的对象，数据类型
arr2=np.array([1,2,3],dtype=np.int32)
arr1.dtype
arr2.dtype
arr=np.array([1,2,3,4,5])
arr.dtype
float_arr=arr.astype(np.float64)#转换
float_arr.dtype
arr=np.array([3.7,-1.2,-2.6,0.5,12.9,10.1])
arr
arr.astype(np.int32)
numeric_strings=np.array(['1.25','-9.6','42'],dtype=np.string_)
numeric_strings.astype(float)
int_array=np.arange(10)
calibers=np.array([.22,.270,.357,.380,.44,.50],dtype=np.float64)
int_array.astype(calibers.dtype)
empty_unit32=np.empty(8,dtype='u4')
empty_unit32
arr=np.array([[1,2,3],[4,5,6]])
arr
arr*arr
arr-arr
1/arr
arr**0.5
arr=np.arange(10)
arr
arr[5]
arr[5:8]
arr[5:8]=12
arr_slice=arr[5:8]
arr_slice[1]=12345#注意，会对arr即原数据产生影响
arr
arr_slice
arr_slice[:]=64
arr
arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d[2]
arr2d[0][2]
arr2d[0,2]#可用，来实现上面的功能
arr3d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
arr3d
arr3d[0]
old_values=arr3d[0].copy()
arr3d[0]=42
arr3d
arr3d[0]=old_values
arr3d
arr3d[1,0]
np.array([7,8,9])
arr[1:6]
arr2d
arr2d[:2]
arr2d[:2,:1]
arr2d[1,:2]
arr2d[2,:1]
arr2d[:,:1]
arr2d[:2,1:]=0
arr2d
names=np.array(['Bob','Joe','Will','Bob','Joe','Will','Joe'])
names
import random
data=np.random.randn(7,4)#numpy.random中的randn函数生成一些正态分布的随机数据
data
names=='Bob'
np.array([True,False,False,True,False,False,False],dtype=bool)
data[names=='Bob']
data[names=='Bob',2:]
data[names=='Bob',3]
names!='Bob'
data[-(names=="Bob")]#负号对条件进行否定
mask=(names=='Bob')|(names=='Will')
mask
data[mask]
data[data<0]=0
data
data[names!='Joe']=7
data
#花式索引
arr=np.empty((8,4))
for i in range(8):
    arr[i]=i
arr
arr[[4,3,0,6]]
arr[[-3,-5,-7]]#负数会从索引的末尾开始选取行
arr=np.arange(32).reshape((8,4))
arr[[1,5,7,2],[0,3,1,2]]#!!!类似于交点
arr[[1,5,7,2]][:,[0,3,1,2]]#!!!类似于交集
arr[np.ix_([1,5,7,2],[0,3,1,2])]#np.ix_()将两个以为整数数组转换为一个用于选取方形区域的索引器

