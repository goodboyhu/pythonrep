import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
#设置显示的最大列、宽等参数，消掉打印不完全中间的省略号
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

from matplotlib import pyplot as plt
file_path = "./directory.csv"

df = pd.read_csv(file_path)
# print(df.head(1))
# print(df.info())

# 分组和聚合
grouped=df.groupby(by="Country")#按国家分组
# print(grouped)
# DataFrameGroupBy
# 可以进行遍历
# for i,j in grouped:
#     print(i)
#     print("-"*100)
#     print(j,type(j))
#     print("*"*100)
# print(df[df["Country"]=="US"])#只要美国的店家

# 调用聚合方法
# print(grouped.count())#统计了所有列
# print(grouped["Brand"].count())#按照国家分组后，统计每个国家的Brand
country_count=grouped["Brand"].count()
print(country_count["US"])
print(country_count["CN"])
print("**********************统计中国每个省份店铺的数量**************************")
# 统计中国每个省份店铺的数量(其中原表中State/Province就是用的代号代表省份)
china_data=df[df["Country"]=="CN"]
grouped=china_data.groupby(by="State/Province").count()["Brand"]
print(grouped)

# 数据按照多个条件进行分组,返回Series
grouped=df["Brand"].groupby(by=[df["Country"],df["State/Province"]]).count()
print(grouped)
print(type(grouped))#前两列是索引，最后一列才是数据，所以为pandas.core.series.Series类型

# 数据按照多个条件进行分组,返回DataFrame
grouped1=df[["Brand"]].groupby(by=[df["Country"],df["State/Province"]]).count()
grouped2=df.groupby(by=[df["Country"],df["State/Province"]])[["Brand"]].count()
grouped3=df.groupby(by=[df["Country"],df["State/Province"]]).count()[["Brand"]]

# print(grouped1,type(grouped1))
# print("*"*100)
# print(grouped2,type(grouped2))
# print("*"*100)
# print(grouped3,type(grouped3))

print("*"*100)
# 索引的方法和属性
print(grouped1.index)
print("********************索引的方法和属性**********************************")
a = pd.DataFrame({'a': range(7),'b': range(7, 0, -1),'c': ['one','one','one','two','two','two', 'two'],'d': list("hjklmno")})
print(a)

b=a.set_index(["c","d"])#使用c，d两列作为索引
print(b)
c=b["a"]
print(c)
print(type(c))
print(c["one"]["j"])
print(c["one"])
d=a.set_index(["d","c"])["a"]#使用d,c两列作为索引，并获取a列数据
print(d)
print(d.index)
print(d.swaplevel()["one"])#交换d,c索引，获取one索引的值，用于获取内侧索引的值
print(b.loc["one"].loc["h"])
print(b.swaplevel().loc["h"])