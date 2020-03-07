import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df1=pd.DataFrame(np.ones((2,4)),index=["A","B"],columns=list("abcd"))
print(df1)

df2=pd.DataFrame(np.ones((3,3)),index=["A","B","C"],columns=list("xyz"))
print(df2)

# 数据合并join（按行）
print(df1.join(df2))
print(df2.join(df1))
df3=pd.DataFrame(np.arange(9).reshape((3,3)),columns=list("fax"))
print(df3)


# 数据合并merge（按列）
print(df1.merge(df3, on="a"))#默认是内连接，此案例的条件是按照df1的a列进行匹配连接，即交集
print(df1.merge(df3, on="a",how="outer"))#外连接，即并集
print(df1.merge(df3, on="a",how="left"))#左外连接，即以左边df1为准
print(df1.merge(df3, on="a",how="right"))#右外连接，即以右边df3为准

print(df1.merge(df3, left_on="a",right_on="a",how="inner"))#也可以指定df1的a列和df3的a列匹配（一般是针对列名不同的情况下）


#注意一下取法的类型
print("*"*100)
print(type(df1["c"]))
print(type(df1[["c"]]))
print(type(df1[["c","a"]]))
print("*"*100)
#修改行索引
print(df1.index)
df1.index=["a","b"]
print(df1)
print("*"*100)
#以某一列作为索引
print(df1.set_index("a"))
print(df1.set_index("a").index)
print(df1.set_index("a",drop=False))#保留这一列作为索引
print(df1["d"].unique())#返回索引唯一值
print(df1.set_index(["a","b"]))#使用两列作为索引
