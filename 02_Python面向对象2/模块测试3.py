# from...import 导入
# 如果希望 从某一个模块 中，导入 部分 工具，就可以使用 from ... import 的方式
# import 模块名 是 一次性 把模块中 所有工具全部导入，并且通过 模块名 / 别名 访问

# 导入之后,不需要 通过 模块名.可以直接使用 模块提供的工具 —— 全局变量、函数、类
from 测试模块1 import Dog
from 测试模块2 import say_hello


say_hello()

wangchai = Dog()
print(wangchai)
