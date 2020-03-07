import pandas as pd
import numpy as np

#读取csv数据
df = pd.read_csv("./dogNames2.csv")
#并且&，或者|
print(df[(800<df["Count_AnimalName"])&(df["Count_AnimalName"]<1000)])#获取800<Count_AnimalName<1000的数据
print(df[(df["Row_Labels"].str.len()>4)&(df["Count_AnimalName"]>700)])#
print("-------------缺失值的填充--------------")
t3=pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("wxyz"))
t3.iloc[1:,:2]=np.nan#赋值操作nan，dataFrame会自动转换数据类型
print(t3)
print(pd.isnull(t3))#判断是否为NAN
print(pd.notnull(t3))#判断是否为NAN
print(pd.notnull(t3["w"]))
print(t3[pd.notnull(t3["w"])])#选择了t3中w列中，不是nan元素的行
print("-------------缺失值的处理方式1：删除为nan的行或者列--------------")
#删除为nan的行或者列
print(t3.dropna(axis=0, how="all",inplace=False))#axis=0表示删除行，how="all"，表示该行元素全为nan时，才删除该行，inplace=False表示是否进行原地修改，即是否直接将修改结果存入t3.默认就是false不修改原数组。很多方法中都有inplace参数
print(t3.dropna(axis=0, how="any",inplace=False))#默认参数how="any"，表示只要该行有nan，就删除该行

print("-------------缺失值的处理方式2：填充nan--------------")
d2=[{"name": "xiaohong", "age": 32, "tel": 10010},{"name": "xiaogang", "tel": 10000},{"name": "xiaowang", "age": 22}]
print(d2)
t2=pd.DataFrame(d2)
print(t2)
print(t2.fillna(0))#将nan填充为0
print(t2.fillna(t2.mean()))#将nan填充为均值，其中均值是不包含nan的均值
#只对age这一列进行操作
print(t2["age"].fillna(t2["age"].mean()))
t2["age"]=t2["age"].fillna(t2["age"].mean())#操作完后，重新给age这一列赋值
print(t2)

'''
处理为0的数据：t[t==0]=np.nan
当然并不是每次为0的数据都需要处理
计算平均值等情况，nan是不参与计算的，但是0会
'''