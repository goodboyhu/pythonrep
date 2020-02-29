from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")
# 电影票房
a = ["猩球崛起3：终极之战", "敦刻尔克",  "蜘蛛侠：英雄归来", "战狼2"]
b_16 = [15746,312,4497,319]
b_15=[12357,156,2045,168]
b_14=[2358,399,2358,362]

# 线条宽度
bar_width=0.2

x_14=list(range(len(a)))
x_15=[i+bar_width for i in x_14]
x_16=[i+bar_width*2 for i in x_14]

plt.figure(figsize=(20, 8), dpi=80)  # 设置图形大小和清晰度

plt.bar(range(len(a)), b_14,width=bar_width,label="9月14日")
plt.bar(x_15, b_15,width=bar_width,label="9月15日")
plt.bar(x_16, b_16,width=bar_width,label="9月16日")


# 图例
plt.legend(loc="upper left", prop=my_font)
# 调整x轴的刻度
plt.xticks(x_15, a, fontproperties=my_font)

# plt.grid(alpha=0.3)
# 添加描述信息
# plt.xlabel("时间", fontproperties=my_font)
# plt.ylabel("温度", fontproperties=my_font)
# plt.title("3月和10月的气温", fontproperties=my_font)
#


plt.show()
