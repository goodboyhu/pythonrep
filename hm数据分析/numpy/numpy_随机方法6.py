import numpy as np


t1=np.eye(4)#4阶单位阵
print(t1)
#每一列最大值的位置
print(np.argmax(t1,axis=0))

# 将1替换为-1
t1[t1==1]=-1
print(t1)

# 创建一个全0的数组:
print(np.zeros((3,4)))
# 创建一个全1的数组:
print(np.ones((3,4)))

print("*"*50)
# np.random.seed(10)#随机数种子设定后，后边的随机数的产生都是一样的，不设定则每次都不一样
#创建一个4行5列的数组，范围在10-20之间
print(np.random.randint(10,20,(4,5)))