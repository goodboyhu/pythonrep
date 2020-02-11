# 尽管 Python 的 列表 中可以 存储不同类型的数据
# 但是在开发中，更多的应用场景是：
# 列表 存储相同类型的数据
# 通过 迭代遍历，在循环体内部，针对列表中的每一项元素，执行相同的操作


name_list = ["zhangsan","lisi","wangwu"]

# 1.访问列表以及下标
print(name_list)
print(name_list[2])
# 查找索引位置,如果数据不再列表中，程会报错
print(name_list.index("lisi"))

#2.修改
name_list[1] = "李四"


# 添加数据
name_list.append("王小二")
name_list.insert(1,"哈哈")
temp_list = ["孙悟空","猪八戒","唐僧"]
name_list.extend(temp_list)

# 删除
# remove删除第一个元素，找不到元素会报错
name_list.remove("wangwu")
name_list.pop()
name_list.pop(3)
# 在日常开发中，要从列表删除数据，建议 使用列表提供的方法,不用del
#del name_list[1]
name_list.clear()

print(name_list)



