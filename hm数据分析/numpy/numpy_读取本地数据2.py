#一般不用numpy读取本地数据，一般用pandas来做
import numpy as np

us_path = "USvideos.csv"
#一般不用numpy读取本地数据，一般用pandas来做.
#delimiter指定分隔符，dtype指定存储类型
t1 = np.loadtxt(us_path,delimiter=",",dtype="int")
print(t1)

# #转置
# t1=np.arange(24).reshape((4,6))
# print(t1)
# #转置方法一
# print(t1.transpose())
# #转置方法二，数学方法
# print(t1.T)
# #转置方法三，交换轴
# print(t1.swapaxes(1,0))