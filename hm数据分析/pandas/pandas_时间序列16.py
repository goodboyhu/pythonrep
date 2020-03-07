import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#设置显示的最大列、宽等参数，消掉打印不完全中间的省略号
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
file_path="./911.csv"
df = pd.read_csv(file_path)
# print(df.head(2))
# print(df.info())
# 获取分类
# print()df["title"].str.split(": ")
temp_list = df["title"].str.split(": ").tolist()
cate_list = [i[0] for i in temp_list]
# cate_df=pd.DataFrame(np.array(cate_list).reshape((df.shape[0],1)),columns=["cate"])
# print(cate_df)
#给df添加一列cate作为分组依据，然后统计title的次数，是时间序列15的另一种做法
df["cate"] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0],1)))

print(df.head(5))
print(df.groupby(by="cate").count()["title"])
