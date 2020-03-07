'''
pandas的常用数据类型
    Series 一维，带标签的数组
    DataFrame 二维，Series容器
'''
import pandas as pd
# 1、Series创建
t0 = pd.Series([1, 21, 34, 14, 5])#左边的1列就是数据的索引值，也就是key
print(t0)
print(type(t0))

print("************指定索引值为abcde**********")
t1 = pd.Series([1, 6, 3, 2, 7], index=list("abcde"))
print(t1)

# 通过字典创建
print("************通过字典创建**********")
temp_dict = {"name": "xiaoxiong", "age": 30, "tel": 10086}
t2 = pd.Series(temp_dict)
print(t2)
print(t2.dtype)

print("************更改类型**********")
print(t1.astype(float))  # 更改类型
print(t1)

print("************Series切片和索引**********")
# 2、Series切片和索引
print(t2["age"])  # 索引取值
print(t2[1])   # 位置取值
#
print(t2[:2])  # 取前2行
print(t2[[1,2]]) # 取指定行
#
print(t2[["age", "tel"]]) # 指定索引
#
print(t0[t0 > 10]) # 大于10的，使用了布尔索引

print("************Series索引操作**********")
# 索引操作
print(t2.index)
for i in t2.index:
    print(i)
print(type(t2.index))
print(len(t2.index))
print(list(t2.index)[:2])

print("************Series值操作**********")
# 值操作
print(t2.values)
print(t2.values[:2])
print(list(t2.values)[:2])
print(type(t0.values))

# print(t2.index)