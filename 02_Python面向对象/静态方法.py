# 在开发时，如果需要在 类 中封装一个方法，这个方法：
# 既 不需要 访问 实例属性 或者调用 实例方法
# 也 不需要 访问 类属性 或者调用 类方法
# 这个时候，可以把这个方法封装成一个 静态方法

class Dog(object):
    # 狗对象计数
    dog_count = 0

    @staticmethod
    def run():
        # 不需要访问实例属性也不需要访问类属性的方法
        print("狗在跑...")

    def __init__(self, name):
        self.name = name

Dog.run()