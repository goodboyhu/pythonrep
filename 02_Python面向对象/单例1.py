# 非单例模式：
class MusicPlayer2(object):
    pass

# 创建多个对象
player1 = MusicPlayer2()
print(player1)

player2 = MusicPlayer2()
print(player2)

# 单例模式
# 单例 —— 让 类 创建的对象，在系统中 只有 唯一的一个实例
# 定义一个 类属性，初始值是 None，用于记录 单例对象的引用
# 重写 __new__ 方法：如果 类属性 is None，调用父类方法分配空间，并在类属性中记录结果，返回 类属性 中记录的 对象引用
class MusicPlayer(object):

    # 定义类属性记录单例对象引用
    instance = None

    def __new__(cls, *args, **kwargs):

        # 1. 判断类属性是否已经被赋值
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        # 2. 返回类属性的单例引用
        return cls.instance

    def __init__(self):
        print("初始化音乐播放对象")

# 创建多个对象
player3 = MusicPlayer()
print(player3)

player4 = MusicPlayer()
print(player4)