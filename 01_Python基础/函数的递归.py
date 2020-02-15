# 函数内部的 代码 是相同的，只是针对 参数 不同，处理的结果不同
# 当 参数满足一个条件 时，函数不再执行！这个非常重要，通常被称为递归的出口，否则 会出现死循环！
def sum_numbers(num):
    print(num)

    # 递归的出口很重要，否则会出现死循环
    if num == 1:
        return

    sum_numbers(num - 1)
    print("完成%d"%num)


sum_numbers(3)


# 需求
# 定义一个函数 sum_numbers
# 能够接收一个 num 的整数参数
# 计算 1 + 2 + ... num 的结果
def sum_numbers(num):
    if num == 1:
        return 1

    # 假设 sum_numbers 能够完成 num - 1 的累加
    temp = sum_numbers(num - 1)

    # 函数内部的核心算法就是 两个数字的相加
    return num + temp


print(sum_numbers(100))
# 提示：递归是一个 编程技巧，初次接触递归会感觉有些吃力！在处理 不确定的循环条件时，格外的有用，例如：遍历整个文件目录的结构
