# 如果 不同的父类 中存在 同名的方法，子类对象 在调用方法时，会调用 哪一个父类中的方法呢？
# 提示：开发时，应该尽量避免这种容易产生混淆的情况！ —— 如果 父类之间 存在 同名的属性或者方法，应该 尽量避免 使用多继承
class A:
    def test(self):
        print("A---test方法")
    def demo(self):
        print("A---demo方法")
class B:
    def test(self):
        print("B---test方法")
    def demo(self):
        print("B---demo方法")
# 先继承的A，则调用的都是A的继承方法
# class C(A,B):
# 先继承的B，则调用的都是B的继承方法
class C(B, A):
    pass

c=C()
c.test()
c.demo()
