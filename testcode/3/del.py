# del 关键字本质上是用来 将一个变量从内存中删除的
# 如果使用 del 关键字将变量从内存中删除，后续的代码就不能再使用这个变量了
# 在日常开发中，要从列表删除数据，建议 使用列表提供的方法
name_list = ["zhangsan","lisi","wangwu"]
del name_list[1]
print(name_list)
name = "小明"
del name
# print(name)
