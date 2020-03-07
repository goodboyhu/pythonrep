import pandas as pd
import numpy as np

#读取csv数据
print("************指定索引值为abcde**********")
df = pd.read_csv("./dogNames2.csv")

# 常用方法
print(df.head())#默认获取前5行数据
print(df.tail())#默认获取最后5行数据
# print(df.info)#基本信息，如占用的内存，几行几列，每列的类型，有无缺失数据（几个）等
# print(df.describe())#快速统计每列的基本统计量（只针对数值类型），如最大值，最小值，均值，标准差，中位数（50%），四分之三中位数（75%）等
print("************排序,取特定的行列**********")
# pandas取行或列的注意点
# - 方括号写数组，表示取行索引，对行进行操作
# - 方括号写字符串，表示取列索引，对列进行操作
df = df.sort_values(by="Count_AnimalName",ascending=False)#按照Count_AnimalName排序，降序
# print(df.head(10))#取前十个排名最高的
# print(df[:20])#取前20行
# print(df["Row_Labels"])
print(df[:20]["Row_Labels"])#取前20行的Row_Labels列

'''
pandas之loc
    df.loc 通过标签索引行数据
'''
print("************排序,取特定的行列-loc，即通过标签获取**********")
t3=pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("wxyz"))
print(t3)
print(t3.loc["a", "z"])#获取a行z列
print(type(t3.loc["a", "z"]))
print(t3.loc["a"])#获取a行，或者print(t3.loc["a",:])
print(t3.loc[:,"y"])#获取Y列
print(t3.loc[["a","c"],:])#获取a行，c行,或者print(t3.loc[["a","c"]])
print(t3.loc[:,["w","z"]])#获取w列，z列
print(t3.loc[["a","c"],["w","z"]])
#注意，与切片不同的是，"a":"c"包含了c！！！即包含了端点
print(t3.loc["a":"c",["w","z"]])#

print("************取特定的行列-iloc，通过位置获取**********")
print(t3.iloc[1])#第“1”行
print(t3.iloc[:,2])#第“2”列
print(t3.iloc[[0,2],[2,1]])
print(t3.iloc[1:,:2])
t3.iloc[1:,:2]=30#赋值操作
print(t3)
t3.iloc[1:,:2]=np.nan#赋值操作nan，dataFrame会自动转换数据类型
print(t3)
