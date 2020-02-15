# 模块能够向外界提供全局变量、函数、类。
# 注意：直接执行的代码不是向外界提供的工具！

def say_hello():
    print("你好你好，我是say_hello()")
print("小明开发的模块")
say_hello()