# 字典是无序的，所以输出顺序可能会不一致
xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 1.75}
print(xiaoming)

# 提示：在实际开发中，由于字典中每一个键值对保存数据的类型是不同的，所以针对字典的循环遍历需求并不是很多
# for 循环内部使用的 `key 的变量` in 字典
for k in xiaoming:
    print("%s: %s" % (k, xiaoming[k]))

# 但是在开发中，更多的应用场景是：
# 使用 多个键值对，存储 描述一个 物体 的相关信息 —— 描述更复杂的数据信息
# 将 多个字典 放在 一个列表 中，再进行遍历，在循环体内部针对每一个字典进行 相同的处理
card_list = [{"name": "张三",
              "qq": "12345",
              "phone": "110"},
             {"name": "李四",
              "qq": "54321",
              "phone": "10086"}
             ]
for k in card_list:
    print(k)

# 取值
print(xiaoming["name"])

# 增加/修改
xiaoming["weight"] = 75
xiaoming["name"] = "小张"
print(xiaoming)

# 删除
xiaoming.pop("name")
print(xiaoming)

# 统计键值对数量
print(len(xiaoming))
# 合并字典
temp = {"ceshi": "测试", "ceshi2": "测试2"}
xiaoming.update(temp)
print(xiaoming)
# 如果合并的字典中和原字典有重复项，会被覆盖
temp2 = {"age": 22}
xiaoming.update(temp2)
print(xiaoming)

# 清空字典
xiaoming.clear()
print(xiaoming)

