message = "你好！Hello Python world!"
print(message)
#2.3.1 使用方法修改字符串的大小写
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
#2.3.2 合并（拼接）字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
#2.3.4 删除空白
favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

print(3/2)
print(0.2 + 0.1)
print(3 * 0.1)

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)