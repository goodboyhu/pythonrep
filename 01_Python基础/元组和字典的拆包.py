def demo(*args, **kwargs):

    print(args)
    print(kwargs)


# 需要将一个元组变量/字典变量传递给函数对应的参数
gl_nums = (1, 2, 3)
gl_xiaoming = {"name": "小明", "age": 18}

# 会把 num_tuple 和 xiaoming 作为元组传递个 args
demo(gl_nums, gl_xiaoming)
# 拆包语法,简化元组/字典变量的传递
demo(*gl_nums, **gl_xiaoming)
#
demo(1, 2, 3,name="小明", age=18)