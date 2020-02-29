import numpy as np


print(np.nan==np.nan)

print("*"*50)
t1=np.arange(24).reshape((4,6))

t1=t1.astype(float)#将元素转换为浮点型数据，才能赋值nan
t1[3,3]=np.nan
print(t1)
print("*"*50)
t1[:,0]=0
print(t1)
print("*"*50)
print(np.count_nonzero(t1))#非零元素个数
print("*"*50)
print(t1!=t1)
print("*"*50)
print(np.count_nonzero(t1!=t1))
print("*"*50)
print(np.isnan(t1))
print(np.count_nonzero(np.isnan(t1)))#统计nan个数
print("****************nan运算结果均为nan*******************")
print(np.sum(t1))
t2=np.arange(12).reshape((3,4))
print(t2)
print(np.sum(t2))
print(np.sum(t2,axis=0))#行向量相加之和