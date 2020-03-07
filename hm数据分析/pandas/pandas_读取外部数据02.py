import pandas as pd
#读取csv数据
print("************指定索引值为abcde**********")
df = pd.read_csv("./dogNames2.csv")
print(df)
# pd.read_sql(sql语句，连接)连接数据库数据

# 访问mongo，pip install pymongo

