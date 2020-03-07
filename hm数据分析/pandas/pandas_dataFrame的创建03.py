import pandas as pd
import numpy as np

# 创建DataFrame
data = pd.DataFrame(np.arange(12).reshape(3, 4))
print(data)
print("************指定行和列的索引值e**********")
# 创建DataFrame，并为其添加索引
t = pd.DataFrame(np.arange(12).reshape(3, 4), index=list("abc"), columns=list("wxyz"))
print(t)

# 通过字典创建DataFrme
temp_dict = {"name": ["xiaoxiong", "xiaogan"], "age": [30, 24], "tel": [10086, 10010]}
t1 = pd.DataFrame(temp_dict)
print(t1)
print("************通过列表创建DataFrme（mongo数据库就是这种数据组织）**********")
# 通过列表创建DataFrme
d2=[{"name": "xiaoxiong", "age": 30, "tel": 10086},{"name": "xiaoxiong", "tel": 10000},{"name": "xiaoxiong", "age": 30}]
print(d2)
t2=pd.DataFrame(d2)
print(t2)

# 常用基础属性
print("************常用基础属性**********")
print(t2.shape)#形状3*3
print(t2.ndim)#维度是2，也就是说是张表
print(t2.index)#行索引
print(t2.columns)#列索引
print(t2.dtypes)#每列数据的类型

print("************常用方法**********")
# 常用方法
print(t2.head(2))#获取前两行数据
print(t2.tail(2))#获取最后两行数据
print(t2.info)#基本信息，如占用的内存，几行几列，每列的类型，有无缺失数据（几个）等
print(t2.describe())#快速统计每列的基本统计量（只针对数值类型），如最大值，最小值，均值，标准差，中位数（50%），四分之三中位数（75%）等