#一般不用numpy读取本地数据，一般用pandas来做
import numpy as np

t1=np.arange(24).reshape((4,6))
print(t1)
print("*"*50)
#将第2,3列修改为0
# t1[:,2:4]=0
# print(t1)
print(t1<10)#小于10的元素（布尔索引）

print("*"*50)
print(t1[t1<10])

print("*"*50)
t1[t1<10]=3#将小于10的元素替换为3
print(t1)

print("*"*50)
print(np.where(t1<=3,100,300))#三元运算符,小于等于3的元素替换为100，否则替换为300

#无法赋值nan，因为nan是浮点型
# t1[3,3]=np.nan
print("*"*50)
t1=t1.astype(float)#将元素转换为浮点型数据，才能赋值nan
t1[3,3]=np.nan
print(t1)

print("*"*50)
t2=np.arange(24).reshape((4,6))
print(t2)
print(t2.clip(10,18))#裁剪：小于等于10的都替换为10，大于等于18的都替换为18

