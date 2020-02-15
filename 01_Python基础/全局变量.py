# 定义一个全局变量
# 为了避免局部变量和全局变量出现混淆，在定义全局变量时，全局变量名前应该增加 g_ 或者 gl_ 的前缀
gl_num = 10


def demo1():
    print(gl_num)


def demo2():
    print(gl_num)


demo1()
demo2()

print("over")
