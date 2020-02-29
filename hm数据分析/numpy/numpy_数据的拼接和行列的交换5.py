import numpy as np

t1=np.arange(12).reshape((2,6))
print(t1)
t2=np.arange(12,24).reshape((2,6))
print(t2)
print("*"*50)
print(np.vstack((t1,t2)))#垂直拼接
print("*"*50)
print(np.hstack((t1,t2)))#水平拼接

print("*"*50)
t3=np.arange(12,24).reshape((3,4))
print(t3)
# t3[[1,2],:]=t3[[2,1],:]#交换2,3行
# print(t3)
t3[:,[0,2]]=t3[:,[2,0]]#交换1,3列
print(t3)

#将us数据和gb数据分别加上标识列1和0，并垂直拼接在一起
us_path = "USvideos.csv"
gb_path = "GBvideos.csv"
#加载数据
t1 = np.loadtxt(us_path,delimiter=",",dtype="int")
t2 = np.loadtxt(gb_path,delimiter=",",dtype="int")
#构造和t1行数一样的1列0向量，作为标志位
zeros=np.zeros((t1.shape[0],1)).astype(int)
#构造和t2行数一样的1列1向量，作为标志位
ones=np.ones((t2.shape[0],1)).astype(int)

#分别水平拼接
t1=np.hstack((t1,zeros))
t2=np.hstack((t2,ones))

#垂直拼接uk和gb两组数据
final_data=np.vstack((t1,t2))
print(final_data)



