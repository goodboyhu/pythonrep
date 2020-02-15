class Women:

    def __init__(self, name):

        self.name = name
        self.age = 18
        # 不要问女生的年龄
        # self.__age = 18

    def secret(self):
        print("%s 的年龄是 %d" % (self.name,self.age))
    # def __secret(self):
    #     print("我的年龄是 %d" % self.__age)


xiaofang = Women("小芳")
print(xiaofang.age)
xiaofang.secret()

# 私有属性 就是 对象 不希望公开的 属性
# 私有方法 就是 对象 不希望公开的 方法
# 在 定义属性或方法时，在 属性名或者方法名前 增加 两个下划线，定义的就是 私有 属性或方法
class Women2:

    def __init__(self, name):

        self.name = name
        # 不要问女生的年龄
        self.__age = 18

    # 对象方法内部可以访问私有属性
    def __secret(self):
        print("%s 的年龄是 %d" % (self.name,self.__age))

    def secret2(self):
        print("%s 的年龄是 %d" % (self.name, self.__age))


xiaofang2 = Women2("小美")
xiaofang2.secret2()


# 私有属性，外部不能直接访问
# print(xiaofang.__age)
#
# 私有方法，外部不能直接调用
# xiaofang.__secret()