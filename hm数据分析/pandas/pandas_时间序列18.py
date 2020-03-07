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
print("*"*100)#将原表中的timeStamp转换为时间戳类型
df["timeStamp"] = pd.to_datetime(df["timeStamp"])
df.set_index("timeStamp", inplace=True)  # 重新设置索引
print(df.head())
# 统计出911数据中不同月份电话次数的，resample("M")按照月份重采样
print("*"*100)
count_by_month=df.resample("M").count()["title"]
print(count_by_month)

#画图
print("*"*100)
_x = count_by_month.index
_y = count_by_month.values
plt.figure(figsize=(20,8),dpi=80)
# for i in _x:
#     print(dir(i))
#     break

#格式化时间戳的显示方式
_x = [i.strftime("%Y%m%d") for i in _x]

plt.plot(range(len(_x)),_y)
plt.xticks(range(len(_x)),_x,rotation=45)

plt.show()
