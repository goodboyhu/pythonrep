def print_line(char, times):
    print(char * times)


def print_lines(char, times):  # 电灯泡提示选择insert document.....，自动插入函数注释的格式
    """打印多行分割线

    :param char:分割字符
    :param times:字符个数
    """
    row = 0

    while row < 5:
        print_line(char, times)

        row += 1


name = "程序员"
