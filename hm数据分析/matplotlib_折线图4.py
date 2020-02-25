from matplotlib import pyplot as plt
from matplotlib import font_manager

#还可以添加水印防止盗版！

#默认matplotlib不显示中文，导入中文字体库
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

# 绘制10点到12点每一分钟的气温
x = range(11, 31)
y_1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_2 = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]
plt.figure(figsize=(20, 8), dpi=80)#设置图形大小和清晰度
#绘制多次折线图，plt.plot是绘制折线图。
plt.plot(x, y_1,label="自己",color="orange",linestyle=":")
plt.plot(x, y_2,label="同桌",color="#DB7093",linestyle="-.")

# 调整x,y轴的刻度
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x,_xtick_labels,fontproperties=my_font)#rotation=45让标签旋转45度
plt.yticks(range(0,9))

#绘制网格,设置透明度为0.4
plt.grid(alpha=0.4,linestyle=":")

#添加图例
plt.legend(prop=my_font,loc="upper left")

#添加描述信息,并设置中文显示
# plt.xlabel("时间",fontproperties=my_font)
# plt.ylabel("温度 单位(℃)",fontproperties=my_font)
# plt.title("10点到12点每分钟的气温变化情况",fontproperties=my_font)

plt.show()
# 实例化一个figure，设置图片大小，figsize=(20,8)设置大小，dpi=80设置分辨率
# plt.figure(figsize=(20,8),dpi=80)
