# 单例设计模式:目的 —— 让 类 创建的对象，在系统中 只有 唯一的一个实例,每一次执行 类名() 返回的对象，内存地址是相同的
# 单例设计模式的应用场景:音乐播放 对象,回收站 对象,打印机 对象

# 使用 类名 () 创建对象时，Python 的解释器 首先 会 调用 __new__ 方法为对象 分配空间
# __new__ 是一个 由 object 基类提供的 内置的静态方法，主要作用有两个：1) 在内存中为对象 分配空间,2) 返回 对象的引用
# Python 的解释器获得对象的 引用 后，将引用作为 第一个参数，传递给 __init__ 方法
# 重写 __new__ 方法 的代码非常固定！
# 重写 __new__ 方法 一定要 return super().__new__(cls)
# 否则 Python 的解释器 得不到 分配了空间的 对象引用，就不会调用对象的初始化方法
# 注意：__new__ 是一个静态方法，在调用时需要 主动传递 cls 参数

class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        print("创建对象，分配空间")
        # 第一步：为对象分配空间
        instance = super().__new__(cls)
        # 第二步：给__init__方法返回对象的引用
        return instance

    def __init__(self):
        print("初始化音乐播放对象")

player = MusicPlayer()

print(player)