# 身份运算符用于比较两个对象的内存地址是否一致 —— 是否是对同一个对象的引用
# 在Python中针对None比较时，建议使用 is 判断
a = [1, 2, 3]
b = [1, 2, 3]
print(b is a)
print(b == a)