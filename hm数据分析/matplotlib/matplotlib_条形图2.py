from matplotlib import pyplot as plt
from matplotlib import font_manager

interval = [0,5,10,15,20,25,30,35,40,45,60,90]#每组的起始位置
width = [5,5,5,5,5,5,5,5,5,15,30,60]#组距
quantity=[836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]#每组中的数据个数

plt.figure(figsize=(20, 8), dpi=80)  # 设置图形大小和清晰度

# 绘制条形图
plt.bar(range(12), quantity, width=1)

# 调整x轴的刻度
_x=[i-0.5 for i in range(13)]
_xtick_labels=interval+[150]
plt.xticks(_x,_xtick_labels)


plt.grid()
# 添加描述信息
# plt.xlabel("时间", fontproperties=my_font)
# plt.ylabel("温度", fontproperties=my_font)
# plt.title("3月和10月的气温", fontproperties=my_font)
#
# # 图例
# plt.legend(loc="upper left", prop=my_font)

plt.show()
