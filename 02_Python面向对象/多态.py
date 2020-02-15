# 新式类：以 object 为基类的类，推荐使用
# 经典类：不以 object 为基类的类，不推荐使用
# 在 Python 3.x 中定义类时，如果没有指定父类，会 默认使用 object 作为该类的 基类 —— Python 3.x 中定义的类都是 新式类
# 在 Python 2.x 中定义类时，如果没有指定父类，则不会以 object 作为 基类
# 今后在定义类时，如果没有父类，建议统一继承自 object
class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)


class XiaoTianDog(Dog):
    # 重写父类方法
    def game(self):
        print("%s 飞到天上去玩耍..." % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))

        # 让狗玩耍
        dog.game()


# 1. 创建一个狗对象
# wangcai = Dog("旺财")
wangcai = XiaoTianDog("飞天旺财")

# 2. 创建一个小明对象
xiaoming = Person("小明")

# 3. 让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)
