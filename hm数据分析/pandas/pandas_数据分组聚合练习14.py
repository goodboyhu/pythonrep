import pandas as pd
from matplotlib import pyplot as plt

file_path="./books.csv"
df = pd.read_csv(file_path)
# print(df.head(2))
# print(df.info())

#统计不同年份书的数量
data1 = df[pd.notnull(df["original_publication_year"])]#获取数据中original_publication_year不为空的数据
grouped = data1.groupby(by="original_publication_year").count()["title"]#根据original_publication_year分组，然后统计title的数量
print(grouped)


#不同年份书的平均评分情况
#去除original_publication_year列中nan的行
data1 = df[pd.notnull(df["original_publication_year"])]
grouped = data1["average_rating"].groupby(by=data1["original_publication_year"]).mean()
# print(grouped)

_x = grouped.index
_y = grouped.values
# #画图
plt.figure(figsize=(20,8),dpi=80)
plt.plot(range(len(_x)),_y)
# print(len(_x))
# plt.xticks(range(len(_x)),_y)
plt.xticks(list(range(len(_x)))[::10],_x[::10].astype(int),rotation=45)
# plt.savefig('./t_10.png')
plt.show()

