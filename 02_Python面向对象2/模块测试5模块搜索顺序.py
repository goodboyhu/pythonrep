import random

# Python 的解释器在 导入模块 时，会：
# 搜索 当前目录 指定模块名的文件，如果有就直接导入;
# 如果没有，再搜索 系统目录.
# 在开发时，给文件起名，不要和 系统的模块文件 重名
'''注意：如果当前目录下，存在一个 random.py 的文件，程序就无法正常执行了！
这个时候，Python 的解释器会 加载当前目录 下的 random.py 而不会加载 系统的 random 模块'''


# Python 中每一个模块都有一个内置属性 __file__ 可以 查看模块 的 完整路径
print(random.__file__)
rand = random.randint(0,10)
print(rand)