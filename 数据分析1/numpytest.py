import numpy as np
# 线性代数用到的模块
from numpy.linalg import *


def main():
    lst = [[1, 3, 5], [2, 4, 6]]
    print(type(lst))
    # 定义numpy最基础的数据结构ndarray，其只能包含一种数据类型
    # 可定义的数据类型有bool、int、int8、int16、int32、int64、int128、uint8、uint16、uint32、uint64、uint128、float、float16/32/64、complex64/128
    np_lst = np.array(lst, dtype=np.float)
    # np_lst=np.array(lst)
    print(type(np_lst))
    # 数据的形状，2行3列
    print(np_lst.shape)
    # 数据的维度，维度是2，2行
    print(np_lst.ndim)
    # 数据的类型
    print(np_lst.dtype)
    # 每个数据所占据的字节大小，1个float64占8个字节
    print(np_lst.itemsize)
    # 包含的元素个数
    print(np_lst.size)
    print("-" * 50)

    # 常用的数组
    # 2*4的零数组，一般用于数值的初始化
    print(np.zeros([2, 4]))
    # 3*5的1矩阵
    print(np.ones([3, 5]))

    print("随机数(均匀分布)")
    print(np.random.rand(2, 4))  # 0到1之间均匀分布，2行4列随机数
    print(np.random.rand())  # 生成一个随机数
    print(np.random.randint(1, 10))  # 生成1-10之间的随机整数,注意需要指定生成数的范围
    print(np.random.randint(1, 10, 3))  # 生成3个1-10之间的随机整数
    print("随机数(正态分布)")
    print(np.random.randn())  # 标准正态分布的随机数
    print(np.random.randn(2, 4))  # 标准正态分布的随机数,2行4列

    print(np.random.choice([10, 20, 30, 5, 8, 6]))  # 从10,20,30,5,8,6中随机生成数字
    print(np.random.beta(1, 10, 100))  # 生成符合beta分布的随机数，从1到10生成100个

    # 等差数列1-10
    print(np.arange(1, 11))
    # 等差数列1-10，2行5列
    lst = np.arange(1, 11).reshape([2, 5])
    print(lst)
    print("Exp")
    print(np.exp(lst))  # 自然指数操作
    print("Exp2")
    print(np.exp2(lst))  # 自然指数的平方操作
    print("Sqrt")
    print(np.sqrt(lst))  # 开平方操作
    print("Sin")
    print(np.sin(lst))
    print("Log")
    print(np.log(lst))

    lst = np.array([[[1, 2, 3, 4],
                     [4, 5, 6, 7]],
                    [[7, 8, 9, 10],
                     [10, 11, 12, 13]],
                    [[14, 15, 16, 17],
                     [18, 19, 20, 21]]
                    ])
    print(lst)
    print("Sum")
    print(lst.sum())
    print(lst.sum(axis=0))
    print(lst.sum(axis=1))
    print(lst.sum(axis=2))  # axis最大为维度-1
    print("Max")
    print(lst.max(axis=1))
    print("Min")
    print(lst.max(axis=0))

    lst1 = np.array([10, 20, 30, 40])
    lst2 = np.array([4, 3, 2, 1])
    print("Add数组相加")
    print(lst1 + lst2)
    print("数组相减、乘、除、平方")
    print(lst1 - lst2)
    print(lst1 * lst2)
    print(lst1 / lst2)
    print(lst1 ** 2)
    print("Dot点乘")
    print(np.dot(lst1.reshape([2, 2]), lst2.reshape([2, 2])))  # 分别将lst1和lst2变为2*2的数组
    print("给数组追加")
    print(np.concatenate((lst1, lst2), axis=0))
    print("给数组追加的2个简单用法")
    print(np.vstack((lst1, lst2)))
    print(np.hstack((lst1, lst2)))
    print("分离数组")
    print(np.split(lst1, 2))
    print(np.split(lst1, 4))
    print("复制数组")
    print(np.copy(lst1))

    print("线性代数")
    print(np.eye(3))  # 3阶单位矩阵
    lst = np.array([[1, 2],
                    [3, 4]])
    print("矩阵的逆")
    print(inv(lst))
    print("转置矩阵")
    print(lst.transpose())
    print("矩阵的行列式求值")
    print(det(lst))
    print("特征值和特征向量，第一个array是特征值，第二个array是特征向量")
    print(eig(lst))
    print("解线性方程组")
    '''
    1x+2y=5
    3x+4y=7
    '''
    lst = np.array([[1, 2],
                    [3, 4]])
    y = np.array([[5.], [7.]])
    print(solve(lst, y))
    print("皮尔逊相关系数")
    print(np.corrcoef([1, 0, 1], [0, 2, 1]))
    print("生成一元多次函数")
    print(np.poly1d([2, 1, 3]))


if __name__ == "__main__":
    main()
