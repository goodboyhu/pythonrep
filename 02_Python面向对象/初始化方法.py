class Cat:

    def __init__(self,name):
        print("这是一个初始化方法")

        # 定义用 Cat 类创建的猫对象都有一个 name 的属性
        self.name = name

    def eat(self):
        print("%s 爱吃鱼" % self.name)


# 使用类名()创建对象的时候，会自动调用初始化方法 __init__
tom = Cat("Tom")
print(tom.name)
tom.eat()
lazy_cat = Cat("大懒猫")
lazy_cat.eat()