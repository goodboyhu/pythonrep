# 给对象增加属性

class Cat:
    """这是一个猫类"""

    # 类中方法 的定义格式和之前学习过的函数 几乎一样,区别在于第一个参数必须是 self
    def eat(self):
        print("%s爱吃鱼"%self.name)

    def drink(self):
        print("%s在喝水"%self.name)

tom = Cat()
# 注意：这种方式虽然简单，但是不推荐使用！
tom.name = "Tom"#可以在debug调试中看到
tom.drink()
tom.eat()

print(tom)

lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()

lazy_cat2 = lazy_cat
print(lazy_cat)
print(lazy_cat2)