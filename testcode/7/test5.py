# 向控制台输出内容结束之后，不会换行
print("*", end="")
print("*")
print("*", end="---")
print("*")
# 单纯的换行
print("")

#方法一
# 1. 定义一个计数器变量，从数字1开始，循环会比较方便
row = 1
while row <= 5:
    print("*" * row)
    row += 1

# 方法二
row = 1
while row <= 5:
    # 假设 python 没有提供字符串 * 操作
    # 在循环内部，再增加一个循环，实现每一行的 星星 打印
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    # 每一行星号输出完成后，再增加一个换行
    print("")
    row += 1

# 乘法表
# 定义起始行
row = 1
# 最大打印 9 行
while row <= 9:
    # 定义起始列
    col = 1
    # 最大打印 row 列
    while col <= row:
        # end = ""，表示输出结束后，不换行
        # "\t" 可以在控制台输出一个制表符，协助在输出文本时对齐
        print("%d * %d = %d" % (col, row, row * col), end="\t")
        # 列数 + 1
        col += 1
    # 一行打印完成的换行
    print("")
    # 行数 + 1
    row += 1