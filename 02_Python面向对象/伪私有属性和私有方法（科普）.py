# 私有属性 就是 对象 不希望公开的 属性
# 私有方法 就是 对象 不希望公开的 方法
# 在 定义属性或方法时，在 属性名或者方法名前 增加 两个下划线，定义的就是 私有 属性或方法
class Women:

    def __init__(self, name):

        self.name = name
        # 不要问女生的年龄
        self.__age = 18

    # 对象方法内部可以访问私有属性
    def __secret(self):
        print("%s 的年龄是 %d" % (self.name,self.__age))



xiaofang = Women("小美")

# 提示：在日常开发中，不要使用这种方式，访问对象的 私有属性 或 私有方法
# Python 中，并没有 真正意义 的 私有
# 在给 私有属性、方法 命名时，实际是对 名称 做了一些特殊处理，使得外界无法访问到
# 处理方式：在 名称 前面加上 _类名 => _类名__名称
print(xiaofang._Women__age)
xiaofang._Women__secret()
# 私有属性，外部不能直接访问
# print(xiaofang.__age)
#
# 私有方法，外部不能直接调用
# xiaofang.__secret()