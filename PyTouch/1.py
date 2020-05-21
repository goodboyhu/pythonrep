import torch
from IPython import display
from matplotlib import pyplot as plt
import numpy as np
import random
import torch.nn as nn


class LinearNet(nn.Module):
    def __init__(self, n_feature):
        super(LinearNet, self).__init__()
        self.linear = nn.Linear(n_feature, 1)

    # forward 定义前向传播
    def forward(self, x):
        y = self.linear(x)
        return y


num_inputs = 2
net = LinearNet(num_inputs)
# print(net)  # 使用print可以打印出网络的结构

net = nn.Sequential(nn.Linear(num_inputs, 1))# 此处还可以传入其他层
# print(net)
# print(net[0])

for param in net.parameters():
    print(param)