import numpy as np

print("-" * 20 + " t1 " + "-" * 20)
t1 = np.arange(12)
print(t1)
print(t1.shape)  # 一维，因为shape返回1个值

print("-" * 20 + " t2 " + "-" * 20)
t2 = np.array([[1, 2, 3], [4, 5, 6]])
print(t2)
print(t2.shape)  # 二维，2行3列，因为shape返回2个值

print("-" * 20 + " t3 " + "-" * 20)
t3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(t3)
print(t3.shape)  # 三维，2块，每块2行3列，因为shape返回3个值

print("-" * 20 + " t4 " + "-" * 20)
t4 = np.arange(12)
print(t4)
print(t4.reshape((3, 4)))  # 把一维变为二维，3行4列
# print(t4.reshape((3,4)))会报错

print("-" * 20 + " t5 " + "-" * 20)
t5 = np.arange(24).reshape((2, 3, 4))
print(t5)
print(t5.reshape((4, 6)))  # 将三维的t5变为二维的
print(t5)  # t5变量本身不会发生改变
print(t5.reshape((24,)))  # 一维
print(t5.reshape((1, 24)))  # 二维
t5 = t5.reshape((4, 6))
print(t5)

print("-" * 20 + " t6 " + "-" * 20)
t6 = t5.reshape((t5.shape[0] * t5.shape[1],))
print(t6)
print(t5.flatten())  # 效果同上，将t5展开为一维数组

print("-" * 20 + " 数组与数字的加减乘除（行列的每个值都计算） " + "-" * 20)
print(t5)
print(t5 + 5)
print(t5 * 5)
print(t5 / 5)
print(t5 / 0)  # nan表示不是一个数，inf表示无限

print("-" * 20 + " 数组与数组的加减乘除（对应行列位置的数值进行运算，这与行列式不同） " + "-" * 20)
print(t5)
t6=np.arange(100,124).reshape((4,6))
print(t6)
print(t6+t5)
print(t6*t5)
print(t6/t5)  # nan表示不是一个数，inf表示无限

print("-" * 20 + " 数组与数组的加减乘除2（每行/列的数值都与对应位置进行运算，这与行列式不同） " + "-" * 20)
print(t5)
t7=np.arange(0,6)
print(t7)
print(t5-t7)
t8=np.arange(4).reshape((4,1))
print(t8)
print(t5-t8)
#下述情况无法计算，维度不同
# t9=np.arange(10)
# print(t9)
# print(t5-t9)