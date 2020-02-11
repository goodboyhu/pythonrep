# Tuple（元组）与列表类似，不同之处在于元组的 元素不能修改
# 元组 表示多个元素组成的序列
# 元组 在 Python 开发中，有特定的应用场景

# 元组中 只包含一个元素 时，需要 在元素后面添加逗号
info_tuple = (50, )
print(type(info_tuple))
info_tuple = (50)
print(type(info_tuple))
info_tuple = ("zhangsan", 18, 1.75,"zhangsan")
print(info_tuple)
print(type(info_tuple))

# 取值和索引
print(info_tuple[2])
print(info_tuple.index("zhangsan"))

# 统计计数
print(info_tuple.count("zhangsan"))
print(len(info_tuple))

# for 循环内部使用的变量 in 元组
for item in info_tuple:
    # 在Python中，可以使用for循环遍历所有非数字型类型的变量：列表、元组、字典 以及 字符串
    # 提示：在实际开发中，除非能够确认元组中的数据类型，否则针对元组的循环遍历需求并不是很多
    # 循环内部针对元组元素进行操作
    print(item)

# 但是在开发中，更多的应用场景是：
# 函数的 参数 和 返回值，一个函数可以接收 任意多个参数，或者 一次返回多个数据
# 格式字符串，格式化字符串后面的 () 本质上就是一个元组
# 让列表不可以被修改，以保护数据安全
info = ("张三", 18, 175.8)
print("%s 的年龄是 %d岁,身高是 %.2f厘米。" % info)

info2 = "%s 的年龄是 %d岁,身高是 %.2f厘米。" % info
print(info2)

# 元组和列表之间的转换
num_list = [1,2,3,4]
print(type(num_list))
num_tuple = tuple(num_list)
print(type(num_tuple))
num2_list = list(num_tuple)
print(type(num2_list))


