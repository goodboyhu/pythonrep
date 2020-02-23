import numpy as np
import matplotlib.pyplot as plt
'''
# 绘制线形图
def main():
    # 绘制一条线，定义横轴x，从负π到π之间定义256个点，且包含最后一个点
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    # 定义余弦函数和正弦函数
    c, s = np.cos(x), np.sin(x)
    # 绘制第一个图
    plt.figure(1)
    # x是自变量，余弦c和正弦s都是因变量
    # plt.plot(x, c)
    # plt.plot(x, s)
    plt.plot(x, c, color="blue", linewidth=1.0, linestyle="-", label="COS", alpha=0.5)  # alpha是透明度
    plt.plot(x, s, "r*", label="SIN")  # r*表示红色的，线型为*的线
    plt.title("COS&SIN")
    # 获取轴编辑器
    ax = plt.gca()
    ax.spines["right"].set_color("none")  # 将图表右边的线隐藏
    ax.spines["top"].set_color("none")  # 将图表顶端的线隐藏
    ax.spines["left"].set_position(("data", 0))  # 将图表左边的线设置到数据域的0位置
    ax.spines["bottom"].set_position(("data", 0))  # 将图表底部的线设置到数据域的0位置
    ax.xaxis.set_ticks_position("bottom")  # 将x轴的数字设置在轴线下方
    ax.yaxis.set_ticks_position("left")  # 将y轴的数字设置在轴线左边
    # 第一个数组参数是标示的位置，第二个数组是标示的文字(省略为数字)，两个数组中的元素一一对应
    plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
    # plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], [r'3.1415926', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
    # plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], [r'π', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
    # 从-1到1标识5个点，且包含最后一个点
    plt.yticks(np.linspace(-1, 1, 5, endpoint=True))
    # 设置坐标轴字体样式，ax.get_xticklabels()+ax.get_yticklabels()是获取x和y轴的标识
    for lable in ax.get_xticklabels() + ax.get_yticklabels():
        lable.set_fontsize(16)
        lable.set_bbox(dict(facecolor="white", edgecolor="None", alpha=0.2))  # 设置标识为方框，背景色为白色，边框为无，透明度0.2
    plt.legend(loc="upper left")  # 显示图例在左上方
    plt.grid()  # 打印网格线
    # plt.axis([-1, 1, -0.5, 1])  # 设置显示范围，横轴是-1到1，纵轴是-0.5到1

    #一下是有意思的事
    # 填充
    # plt.fill_between(x, np.abs(x) < 0.5, c, c > 0.5, color="green", alpha=0.25)
    plt.show()
'''
def main():
    #绘制散点图
    fig = plt.figure()
    # fig.add_subplot(3,3,1)#创建一个figure分为3行3列显示，此图位于第一幅的位置
    # fig.add_subplot(3,3,1)
    ax = fig.add_subplot(3, 3, 1)
    n = 128
    X = np.random.normal(0, 1, n)#生成随机数
    Y = np.random.normal(0, 1, n)#生成随机数
    T = np.arctan2(Y, X)#上色
    # plt.axes([0.025,0.025,0.95,0.95])#显示范围
    # 画散点的 s是点的大小，c是颜色，alpha是透明度
    ax.scatter(X, Y, s=75, c=T, alpha=0.5)
    # x和y的范围limit
    plt.xlim(-1.5, 1.5), plt.xticks([])
    plt.ylim(-1.5, 1.5), plt.yticks([])
    plt.axis()
    plt.title("scatter")
    plt.xlabel("x")
    plt.ylabel("y")
    # plt.show()


    # 柱状图
    fig.add_subplot(332)
    n = 10
    X = np.arange(n)#构建0-9的一个数列
    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)#一个数乘以一个随机数，随机数在0.5-1之间
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')#正的在上面
    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')#负的在下面
    #注释
    for x, y in zip(X, Y1):
        plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')

    for x, y in zip(X, Y2):
        plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')

    # 饼图
    fig.add_subplot(333)
    n = 20
    Z = np.ones(n)
    Z[-1] = 2
    plt.pie(Z, explode=Z * .05, colors=['%f' % (i / float(n)) for i in range(n)],
            labels=['%.2f' % (i / float(n)) for i in range(n)])
    plt.gca().set_aspect('equal')
    plt.xticks([]), plt.yticks([])

    # 极坐标 polar = True
    fig.add_subplot(334, polar=True)
    n = 20
    theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / n)
    radii = 10 * np.random.rand(n)
    # plt.plot(theta,radii)
    plt.polar(theta, radii)

    # 热图 heatmap
    fig.add_subplot(335)
    from matplotlib import cm
    data = np.random.rand(3, 3)
    cmap = cm.Blues
    map = plt.imshow(data, interpolation='nearest', cmap=cmap, aspect="auto", vmin=0, vmax=1)

    # 3D图
    from mpl_toolkits.mplot3d import Axes3D
    ax = fig.add_subplot(336, projection='3d')
    ax.scatter(1, 1, 3, s=100)

    # hot map 热例图
    fig.add_subplot(313)

    def f(x, y):
        return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

    n = 256
    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)
    X, Y = np.meshgrid(x, y)
    plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)

    # 保存图片
    plt.savefig("./data/fig.png")

    plt.show()


if __name__ == "__main__":
    main()
