# 方法二： 扩展父类的方法

# 如果在开发中，子类的方法实现 中 包含 父类的方法实现，父类原本封装的方法实现 是 子类方法的一部分，就可以使用 扩展 的方式
# 在子类中 重写 父类的方法，在需要的位置使用 super().父类方法 来调用父类方法的执行，代码其他的位置针对子类的需求，编写 子类特有的代码实现

# 关于 super
# 在 Python 中 super 是一个 特殊的类
# super() 就是使用 super 类创建出来的对象
# 最常 使用的场景就是在 重写父类方法时，调用 在父类中封装的方法实现
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
        # 使用super()调用之前父类中的bark方法
        super().bark()
        print("！@！#！@#@")

xtq = XiaoTianQuan()
xtq.bark()
