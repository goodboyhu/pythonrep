import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#设置显示的最大列、宽等参数，消掉打印不完全中间的省略号
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

'''
pandas之时间序列
'''
#每隔一天
print(pd.date_range(start="20171230", end="20191231", freq="D"))
#每隔10天
print(pd.date_range(start="20171230", end="20191231", freq="10D"))
#生成10个，以月为单位（每月最后一个日历日）
print(pd.date_range(start="20171230", periods=10, freq="M"))
