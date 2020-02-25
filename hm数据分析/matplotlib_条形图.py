from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")
# 电影票房
a = ["战狼2", "速度与激情8", "羞羞的铁拳", "前任3：\n再见前任", "功夫瑜伽", "西游伏妖篇", "变形金刚5：\n最后的骑士", "芳华", "摔跤吧！爸爸", "寻梦环游记", "加勒比海盗5：\n死无对证",
     "金刚：骷髅岛", "极限特工：\n终极回归", "生化危机6：\n终章", "乘风破浪", "神偷奶爸3", "智取威虎山", "蜘蛛侠：\n英雄归来", "大闹天竺", "雷神3：\n诸神黄昏"]
b = [56.39, 26.49, 21.9, 19.26, 17.53, 16.49, 15.45, 14.11, 12.96, 12.02, 11.8, 11.61, 11.28, 11.12, 10.38, 10.3, 8.74,
     7.67, 7.55, 7.36]

plt.figure(figsize=(20, 15), dpi=80)  # 设置图形大小和清晰度

# 绘制条形图
plt.bar(range(len(a)), b, width=0.3)

# 调整x轴的刻度

plt.xticks(range(len(a)), a, fontproperties=my_font, rotation=90)

# 添加描述信息
# plt.xlabel("时间", fontproperties=my_font)
# plt.ylabel("温度", fontproperties=my_font)
# plt.title("3月和10月的气温", fontproperties=my_font)
#
# # 图例
# plt.legend(loc="upper left", prop=my_font)

plt.show()
