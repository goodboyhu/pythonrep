import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
file_path = "./IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)
# print(df.head(1))
print(df.info())
print(df["Rating"].mean())#获取平均分
print(len(set(df["Director"].tolist())))#获取导演人数
print(len(df["Director"].unique()))#效果同上
#获取演员数量
temp_actors_list=df["Actors"].str.split(",").tolist()
# print(temp_actors_list)
actors_list=[i for j in temp_actors_list for i in j]
actors_num=len(set(actors_list))
print(actors_num)