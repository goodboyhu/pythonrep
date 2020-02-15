# 方法一： 覆盖父类的方法
class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")

class Dog(Animal):
    def bark(self):
        print("汪汪叫")

class XiaoTianQuan(Dog):
    def fly(self):
        print("我会飞")
        # 具体的实现方式，就相当于在子类中定义了一个和父类同名的方法并且实现
        # 重写之后，在运行时，只会调用子类中重写的方法，而不再会调用父类封装的方法
    def bark(self):
        print("叫的和神一样....")

xtq = XiaoTianQuan()
xtq.bark()

