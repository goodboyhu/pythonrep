# 当一个 对象被从内存中销毁 前，会 自动 调用 __del__ 方法
# __del__ 如果希望在对象被销毁前，再做一些事情，可以考虑一下 __del__ 方法
class Cat:

    def __init__(self, new_name):

        self.name = new_name

        print("%s 来了" % self.name)

    def __del__(self):

        print("%s 去了" % self.name)

# tom 是一个全局变量
tom = Cat("Tom")
print(tom.name)

# del 关键字可以删除一个对象
del tom

print("-" * 50)