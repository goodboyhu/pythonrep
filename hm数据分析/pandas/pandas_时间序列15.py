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
cate_list = list(set([i[0] for i in temp_list]))
print(cate_list)

#构造全为0的数组
zero_df=pd.DataFrame(np.zeros((df.shape[0],len(cate_list))),columns=cate_list)
#赋值
for cate in cate_list:
    zero_df[cate][df["title"].str.contains(cate)] = 1

sum_ret=zero_df.sum(axis=0)
print(sum_ret)
