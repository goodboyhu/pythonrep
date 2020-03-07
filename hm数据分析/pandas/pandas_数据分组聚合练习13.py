import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager
#设置显示的最大列、宽等参数，消掉打印不完全中间的省略号
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")
file_path = "./directory.csv"

df = pd.read_csv(file_path)

# 2、使用matplotlib呈现出每个中国每个城市的店铺数量
df=df[df["Country"]=="CN"]
#准备数据
data1 = df.groupby(by="City").count()["Brand"].sort_values(ascending=False)[:25]

_x = data1.index
_y = data1.values

#画图
plt.figure(figsize=(20,8),dpi=80)

# plt.bar(range(len(_x)),_y,width=0.3,color="orange")
plt.barh(range(len(_x)),_y,height=0.3,color="orange")

# plt.xticks(range(len(_x)),_x,fontproperties=my_font)
plt.yticks(range(len(_x)),_x,fontproperties=my_font)

# plt.savefig("./t_09_02.png")

plt.show()