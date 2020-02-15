# 子类对象 不能 在自己的方法内部，直接 访问 父类的 私有属性 或 私有方法
# 子类对象 可以通过 父类 的 公有方法 间接 访问到 私有属性 或 私有方法

class A():
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
    def __test(self):
        print("父类的私有方法 %d，%d" % (self.num1,self.__num2))
    # 在公有方法中访问私有属性和私有方法
    def test(self):
        print("父类的公有方法，输出父类的私有属性%d"%self.__num2)
        self.__test()

class B(A):
    def deom(self):
        # 在子类的对象方法中，不能访问父类的私有属性
        # print("访问父类的私有属性%d"%self.__num2)
        # 在子类的对象方法中，不能调用父类的私有方法
        # self.__test()

        # 可以再子类中访问父类的公有属性
        print("子类方法调用父类公有属性：%d"%self.num1)
        # 可以再子类中调用父类的公有方法
        self.test()

b=B()
# print(b)
# 在外界不能直接访问私有属性和方法
# print(b.__num2)
# b.__test()
b.deom()
# print(b.num1)
# b.test()