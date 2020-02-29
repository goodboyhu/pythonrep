import numpy as np
import random

print("-" * 20 + " t1 " + "-" * 20)
t1 = np.array([1,2,3])
print(t1)
print(type(t1))

t2 = np.array(range(10))
print(t2)
print(type(t2))

t3 = np.arange(10) #等同于上述方法
print(t3)
print(type(t3))

t4 = np.arange(4,10,2) #等同于上述方法
print(t4)
print(type(t4))
print(t4.dtype)#数组中存放的数据的类型，还有int8等类型

t5 = np.array(range(1,4),dtype="i1")#指定float等类型
print(t5)
print(type(t5))
print(t5.dtype)#数组中存放的数据的类型，还有int8等类型

t6 = np.array([1,1,0,1,0,0],dtype=bool)
print(t6)
print(t6.dtype)

#修改数据类型
t7=t6.astype("int8")
print(t7)
print(t7.dtype)

#numpy中的小数
t8=np.array([random.random() for i in range(10)])
print(t8)
print(t8.dtype)
#四舍五入保留2位小数
t9=np.round(t8,2)
print(t9)
