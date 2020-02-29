import numpy as np
import matplotlib.pyplot as plt

# 希望了解英国的youtube中视频的评论数和喜欢数的关系，应该如何绘制改图
us_data = "USvideos.csv"
uk_data = "GBvideos.csv"

t_uk = np.loadtxt(uk_data, delimiter=",", dtype='int')
#可以只选择喜欢数比50万小的数据集合
t_uk=t_uk[t_uk[:,1]<500000]#t_uk[:,1]<500000是喜欢数列小于50万的数据位置（行位置），返回true的一个矩阵

t_uk_comment=t_uk[:,-1]#评论数
t_uk_like=t_uk[:,1]#喜欢数

plt.figure(figsize=(20,8),dpi=80)
plt.scatter(t_uk_like,t_uk_comment)#散点图
plt.savefig('./t_05.png')
plt.show()