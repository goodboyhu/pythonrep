#一般不用numpy读取本地数据，一般用pandas来做
import numpy as np

us_path = "USvideos.csv"
#一般不用numpy读取本地数据，一般用pandas来做.
#delimiter指定分隔符，dtype指定存储类型
t1 = np.loadtxt(us_path,delimiter=",",dtype="int")
print(t1)
print("*"*50)
print(t1[2])#取第3行
print("*"*50)
print(t1[2:])#取连续的多行
print("*"*50)
print(t1[[2,5,8]])#取不连续的多行，第3,6,9行。
print("*"*50)

#通用方法print(t1[行,列])
print(t1[1,:])#取第2行，从第2行开始，每列都要
print("*"*50)
print(t1[2:,:])#取第3行，从第3行开始，每行每列都要
print("*"*50)
print(t1[[2,5,8],:])#取第3,6,9行
print("*"*50)
print(t1[:,0])#取第1列
print("*"*50)
print(t1[:,2:])#取第3列之后的列
print("*"*50)
print(t1[:,[0,2]])#取第1,3列
print("*"*50)
print(t1[2,3])#取第3行第4列的元素
print("*"*50)
print(t1[2:5,1:4])#取第3-5行，,2-4列的元素，即行列交叉点的位置元素
print("*"*50)
print(t1[[0,2,2],[0,1,3]])#取第1行第1列，第3行第2列，第3行第4列的元素
