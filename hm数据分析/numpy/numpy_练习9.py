import numpy as np
import matplotlib.pyplot as plt
#美国youtube1000的数据，结合之前的matplotlib绘制出各自的评论数量的直方图
us_data="USvideos.csv"
uk_data="GBvideos.csv"

t_us = np.loadtxt(us_data,delimiter=",",dtype=int)

# 取评论数(最后一列)
t_us_comments=t_us[:,-1]
# 选择比5000小的数据（因为数据差距太大了，大多数数据都在5000以下，此处也是使用了布尔索引，即返回位置为true的值）
t_us_comments=t_us_comments[t_us_comments<5000]
# 计算组数
d = 250 # 组距
bin_nums = (max(t_us_comments) - min(t_us_comments)) // d

# 绘图
plt.figure(figsize=(20,8),dpi=80)
plt.hist(t_us_comments,bin_nums,density=False)
plt.savefig('./t_04.png')
plt.show()

# 希望了解英国的youtube中视频的评论数和喜欢数的关系，应该如何绘制改图
# import numpy as np
# import matplotlib.pyplot as plt
#
# us_data = "USvideos.csv"
# uk_data = "GBvideos.csv"
#
# t_uk = np.loadtxt(uk_data, delimiter=",", dtype='int')
# #选择喜欢数比50万小的数据
# t_uk=t_uk[t_uk[:,1]<500000]
#
# t_uk_comment=t_uk[:,-1]
# t_uk_like=t_uk[:,1]
#
# plt.figure(figsize=(20,8),dpi=80)
# plt.scatter(t_uk_like,t_uk_comment)
# plt.savefig('./t_05.png')
# plt.show()