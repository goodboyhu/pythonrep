# 提示：多值参数 的应用会经常出现在网络上一些大牛开发的框架中，知道多值参数，有利于我们能够读懂大牛的代码
# 参数名前增加 一个 * 可以接收 元组，*args —— 存放 元组 参数，前面有一个 *，args 是 arguments 的缩写，有变量的含义。
# 参数名前增加 两个 * 可以接收 字典，**kwargs —— 存放 字典 参数，前面有两个 *，kw 是 keyword 的缩写，kwargs 可以记忆 键值对参数
def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


demo(1)
print("-" * 50)
demo(1, 2, 3, 4, 5, 6)
print("-" * 50)
demo(1, 2, 3, 4, 5, 6, name="小明")
print("-" * 50)
demo(1, 2, 3, 4, 5, name="小明", age=18, gender=True)


# 提示：多值参数 的应用会经常出现在网络上一些大牛开发的框架中，知道多值参数，有利于我们能够读懂大牛的代码

# 1.定义一个函数 sum_numbers，可以接收的 任意多个整数
# 2.功能要求：将传递的 所有数字累加 并且返回累加结果
def sum_numbers(*args):
# def sum_numbers(args):
    num = 0
    # 遍历 args 元组顺序求和
    for n in args:
        num += n

    return num


print(sum_numbers(1, 2, 3))
# print(sum_numbers((1, 2, 3)))
