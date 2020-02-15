# 无论传递的参数是 可变 还是 不可变，只要 针对参数 使用 赋值语句，会在 函数内部 修改 局部变量的引用，不会影响到 外部变量的引用
def demo(num, num_list):

    print("函数内部")

    # 赋值语句
    num = 200
    num_list = [1, 2, 3]

    print(num)
    print(num_list)

    print("函数代码完成")


gl_num = 99
gl_list = [4, 5, 6]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)

# 如果传递的参数是 可变类型，在函数内部，使用 方法 修改了数据的内容，同样会影响到外部的数据
def mutable(num_list):
    # num_list = [1, 2, 3]
    num_list.extend([1, 2, 3])

    print(num_list)

gl_list = [6, 7, 8]
mutable(gl_list)
print(gl_list)