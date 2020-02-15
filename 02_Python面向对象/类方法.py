class Tool(object):

    # 使用赋值语句，定义类属性，记录创建工具对象的总数
    count = 0
    # 类方法的第一个参数应该是cls
    # 由哪一个类调用的方法，方法内的cls就是哪一个类的引用，这个参数和实例方法的第一个参数是self 类似，提示，使用其他名称也可以，不过习惯使用cls
    @classmethod
    def show_tool_count(cls):
        """显示工具对象的总数"""
        print("工具对象的总数 %d" % cls.count)

    def __init__(self, name):
        self.name = name

        # 针对类属性做一个计数+1
        Tool.count += 1

tool1 = Tool("斧头")
tool2 = Tool("榔头")
Tool.show_tool_count()