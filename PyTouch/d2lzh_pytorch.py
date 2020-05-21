import torch
from IPython import display
from matplotlib import pyplot as plt
import numpy as np
import random


def use_svg_display():
    # ⽤用矢量图显示
    display.set_matplotlib_formats('svg')
def set_figsize(figsize=(3.5, 2.5)):
    use_svg_display()
    # 设置图的尺⼨寸
    plt.rcParams['figure.figsize'] = figsize

# 3.2.2 读取数据
# 在训练模型的时候，我们需要遍历数据集并不断读取小批量数据样本。这里我们定义一个函数：它每次返回 batch_size （批量大小）个随机样本的特征和标签。
# 本函数已保存在d2lzh包中⽅便以后使用
def data_iter(batch_size, features, labels):
    num_examples = len(features)
    indices = list(range(num_examples))
    random.shuffle(indices) # 样本的读取顺序是随机的
    for i in range(0, num_examples, batch_size):
        j = torch.LongTensor(indices[i: min(i + batch_size,num_examples)]) # 最后⼀一次可能不不⾜足⼀一个batch
        yield features.index_select(0, j), labels.index_select(0,j)

# 3.2.4 定义模型
# 下⾯是线性回归的⽮量计算表达式的实现。我们使⽤ mm 函数做矩阵乘法。
def linreg(X, w, b): # 本函数已保存在d2lzh_pytorch包中方便以后使⽤
    X = X.float()  # 原书中的bug，扈晓君调试出。需要转换数字类型。
    w = w.float()
    b = b.float()
    return torch.mm(X, w) + b

# 3.2.5 定义损失函数
# 我们使用上一节描述的平方损失来定义线性回归的损失函数。在实现中，我们需要把真实值 y 变形成预测值 y_hat 的形状。以下函数返回的结果也将和 y_hat 的形状相同。
def squared_loss(y_hat, y): # 本函数已保存在d2lzh_pytorch包中方便以后使用
    # 注意这里返回的是向量, 另外, pytorch里的MSELoss并没有除以 2
    return (y_hat - y.view(y_hat.size())) ** 2 / 2

# 3.2.6 定义优化算法
# 以下的 sgd 函数实现了上一节中介绍的小批量随机梯度下降算法。它通过不断迭代模型参数来优化损失函数。
# 这里自动求梯度模块计算得来的梯度是一个批量样本的梯度和。我们将它除以批量⼤小来得到平均值。
def sgd(params, lr, batch_size): # 本函数已保存在d2lzh_pytorch包中⽅便以后使⽤
    for param in params:
        param.data -= lr * param.grad / batch_size # 注意这里更改param时用的param.data