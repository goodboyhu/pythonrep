# 不可变类型，内存中的数据不允许被修改：
# 数字类型 int, bool, float, complex, long(2.x)
# 字符串 str
# 元组 tuple
# 可变类型，内存中的数据可以被修改：列表 list，字典 dict


# 不可变类型可以做元组中的key，如数字、字符串、元组，可变类型不可以，如列表、字典不可以做元组的key！value可以是任意类型。

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)