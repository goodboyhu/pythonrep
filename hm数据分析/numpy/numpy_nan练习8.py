import numpy as np


# 将当前列的nan，替换为当前列不含nan的其他数的均值
def fill_ndarray(t1):
    for i in range(t1.shape[1]):  # 获取矩阵的列数，遍历每一列
        temp_col = t1[:, i]  # 获取当前列
        nan_num = np.count_nonzero(np.isnan(t1))  # 获取当前列中nan的个数
        if nan_num != 0:  # 不为0，说明当前列有nan值
            # 获取当前一列不为nan的array。此处使用了布尔索引，在temp_col == temp_col表达式中，因为其中的nan元素不等于nan元素，
            # 所以除了nan的位置，其他都是true，只把位置为true的元素赋值给temp_not_nan_col
            temp_not_nan_col = temp_col[temp_col == temp_col]
            # np.isnan(temp_col)返回的是一个布尔矩阵，其中nan的位置是true，选中当前nan的位置（即true的位置），替换为不为nan的均值
            temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()
    return t1


if __name__ == '__main__':
    t1 = np.arange(12).reshape((3, 4)).astype("float")
    t1[1, 2:] = np.nan
    print(t1)
    t1 = fill_ndarray(t1)
    print(t1)
