class Cat:
    """这是一个猫类"""

    # 类中方法 的定义格式和之前学习过的函数 几乎一样,区别在于第一个参数必须是 self
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫在喝水")

tom = Cat()
tom.drink()
tom.eat()

print(tom)

lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()

lazy_cat2 = lazy_cat
print(lazy_cat)
print(lazy_cat2)