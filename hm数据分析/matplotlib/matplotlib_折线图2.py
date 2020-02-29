from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

#默认matplotlib不显示中文，导入中文字体库
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

# 绘制10点到12点每一分钟的气温
x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]  # 得到120个随机温度
plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y)

# 调整x轴的刻度
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
# plt.xticks(_xtick_labels)仅限于标签_xtick_labels是纯数字的情况，如果标签不是纯数字，就需要传入2个参数，让标签_xtick_labels和数轴上的数字_x一一对应。因此_x与_xtick_labels的长度应该是一样的。
plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45,fontproperties=my_font)#rotation=45让标签旋转45度


#添加描述信息,并设置中文显示
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度 单位(℃)",fontproperties=my_font)
plt.title("10点到12点每分钟的气温变化情况",fontproperties=my_font)

plt.show()
# 实例化一个figure，设置图片大小，figsize=(20,8)设置大小，dpi=80设置分辨率
# plt.figure(figsize=(20,8),dpi=80)
