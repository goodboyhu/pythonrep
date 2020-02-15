def measure():
    """返回当前的温度"""

    print("开始测量...")
    temp = 39
    wetness = 10
    print("测量结束...")

    # 其实是return (temp, wetness)，即返回元组类型，但是这种情况下通常省略括号。
    return temp, wetness


result = measure()
print(result)
print(result[0])
print(result[1])
print("-"*50)
# 在 Python 中，可以将一个元组使用赋值语句同时赋值给多个变量，而不必使用麻烦的下标来访问赋值。
# 注意：变量的数量需要和元组中的元素数量保持一致
gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)


