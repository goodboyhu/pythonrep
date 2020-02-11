str1 = "hello hello"
str2 = '我的外号是"大西瓜"'
print(str1[6])
for char in str2:
    print(char)

print("长度：%d" % len(str1))
print("llo出现的次数：%d" % str1.count("llo"))
print("llo第一次出现的位置索引（不存在会报错）：%d" % str1.index("llo"))

# 如果 string 中只包含空格，\t,\r,\n等空白字符，则返回 True
space_str = "    \t\n\r"
print(space_str.isspace())

# 是否只包含数字，但是都不能判断小数
# num_str = "1.1"
# num_str = "1"
# num_str = "(1)"
# num_str = "\u00b2"  # 上标2
num_str = "一千零一"
print(num_str)
print(num_str.isdecimal())  # 不能判断⑴、\u00b2，一般都用这个方法判断数字类型
print(num_str.isdigit())  # 不能判断中文数字
print(num_str.isnumeric())

hello_str = "hello world"
print(hello_str.startswith("he"))
print(hello_str.endswith("world"))
# find返回找到的第一个索引值，如果不存在会返回-1，但是用index方法会返回错误信息。
print(hello_str.find("llo"))
print(hello_str.find("abc"))

# replace方法不会修改原有字符串,会返回一个新的字符串
print(hello_str.replace("world", "python"))
print(hello_str)

poem = ["登鹳雀楼", "王之涣", "白日依山尽", "黄河入海流", "欲穷千里目", "更上一层楼"]
for poem_str in poem:
    print("|%s|" % poem_str.center(10, "　"))  # 长度是10，用全半角中文空格填充
    #print("|%s|" % poem_str.ljust(10, "　"))  # 左对齐



#删除空白字符
poem2 = ["\t\n登鹳雀楼", "王之涣", "白日依山尽\t", "   黄河入海流", "欲穷千里目", "更上一层楼"]
for poem_str in poem2:
    print("|%s|" % poem_str.strip().center(10, "　"))  # 长度是10，用全半角中文空格填充

# 拆分和合并
poem3 = "登鹳雀楼\t王之涣\t白日依山尽\t\n黄河入海流\t\n欲穷千里目\t\n更上一层楼"
poem_list = poem3.split()#拆分字符串
print(poem_list)
#合并字符串
result = " ".join(poem_list)
print(result)

#切片
num_str = "0123456789"
print(num_str[2:6])
print(num_str[2:])
print(num_str[:5])
print(num_str[:])
print(num_str[::3])
print(num_str[1::2])
print(num_str[-1])
print(num_str[2:-1])
print(num_str[-2:])
print(num_str[::-1])#逆序输出字符串用-1步长倒着切片