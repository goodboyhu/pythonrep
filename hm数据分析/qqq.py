from numpy import random



indices = list(range(1000))#构建长度为1000的列表[0,1,2....999]
random.shuffle(indices) # 样本的读取顺序是随机的，如[55,67,5,2,999,.......]
print(indices)
for i in range(0, 1000, 10):
    j = indices[i: min(i + 10,1000)] # 最后一次可能不⾜一个batch
    print(j)
    # yield features.index_select(0, j), labels.index_select(0,j)