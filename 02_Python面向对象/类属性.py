# 类属性 就是给 类对象 中定义的 属性
# 通常用来记录 与这个类相关 的特征
# 类属性 不会用于记录 具体对象的特征

class Tool(object):

    # 使用赋值语句，定义类属性，记录创建工具对象的总数
    count = 0

    def __init__(self, name):
        self.name = name

        # 针对类属性做一个计数+1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("铁锹")

# 知道使用 Tool 类到底创建了多少个对象?
# 要访问类属性有两种方式：
# （1）类名.类属性
print("（通过类名访问）现在创建了 %d 个工具" % Tool.count)
# （2）对象.类属性 （不推荐）
print("（通过对象访问）现在创建了 %d 个工具" % tool1.count)
print("（通过对象访问）现在创建了 %d 个工具" % tool2.count)
print("（通过对象访问）现在创建了 %d 个工具" % tool3.count)
# 如果使用 对象.类属性 = 值 赋值语句，只会 给对象添加一个属性，而不会影响到 类属性的值
tool3.count = 99
print("（通过对象访问）现在创建了 %d 个工具" % tool3.count)
print("（通过类名访问）现在创建了 %d 个工具" % Tool.count)



