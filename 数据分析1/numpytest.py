import numpy as np


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
    print("-"*50)


    # 常用的数组
    # 2*4的零数组，一般用于数值的初始化
    print(np.zeros([2,4]))
    # 3*5的1矩阵
    print(np.ones([3,5]))

    print("随机数(均匀分布)")
    print(np.random.rand(2,4))#0到1之间均匀分布，2行4列随机数
    print(np.random.rand())#生成一个随机数
    print(np.random.randint(1,10))# 生成1-10之间的随机整数,注意需要指定生成数的范围
    print(np.random.randint(1, 10,3))#生成3个1-10之间的随机整数
    print("随机数(正态分布)")
    print(np.random.randn())#标准正态分布的随机数
    print(np.random.randn(2,4))  # 标准正态分布的随机数,2行4列

    print(np.random.choice([10,20,30,5,8,6]))#从10,20,30,5,8,6中随机生成数字
    print(np.random.beta(1,10,100))#生成符合beta分布的随机数，从1到10生成100个



if __name__ == "__main__":
    main()
