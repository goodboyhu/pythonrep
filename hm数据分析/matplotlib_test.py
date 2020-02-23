from matplotlib import pyplot as plt

# 24小时，每隔两小时的气温显示
x=range(2,26,2)#小时
y=[15,13,14.5,17,20,25,26,26,27,22,28,15]#气温
#实例化一个figure，设置图片大小，figsize=(20,8)设置大小，dpi=80设置分辨率
plt.figure(figsize=(20,8),dpi=80)

#绘图，即小时与气温一一对应，(2,15)、(4,13)、(6,14.5)...
plt.plot(x,y)

#x轴的绘制
#想让x轴显示什么，就给他传什么
#设置x轴的刻度,把之前需要绘制的x点都表示出来
# plt.xticks(x)

#设置x轴的刻度,每隔一个值就标识出来
# plt.xticks(range(2,25))

# plt.xticks(range(25,50))#此时前半部分的图像x是没有标识的，从25之后才有

# 设置x轴的刻度,要求步长为0.5时，range(2,25,0.5)不符合语法，所以：
_xtick_labels=[i/2 for i in range(4,49)]
plt.xticks(_xtick_labels)

# 步长为1.5,即0.5*3=1.5
# plt.xticks(_xtick_labels[::3])


#y轴的绘制
plt.yticks(range(min(y),max(y)+1))

#保存到本地(要先绘制再保存)，还可以保存为svg矢量图格式
plt.savefig("./t1.png")

#展示图形
plt.show()