class Gun:

    def __init__(self, model):
        # 枪的型号
        self.model = model
        # 子弹数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 判断是否还有子弹
        if self.bullet_count <= 0:
            print("没有子弹了...")

            return

        # 发射一颗子弹
        self.bullet_count -= 1

        print("%s 发射子弹[%d]..." % (self.model, self.bullet_count))



# 在定义属性时，如果 不知道设置什么初始值，可以设置为 None
# None 关键字 表示 什么都没有,表示一个 空对象，没有方法和属性，是一个特殊的常量
# 可以将 None 赋值给任何一个变量
class Soldier:

    def __init__(self, name):

        # 姓名
        self.name = name
        # 枪，士兵初始没有枪 None 关键字表示什么都没有
        self.gun = None

    def fire(self):

        # 1. 判断士兵是否有枪
        # if self.gun == None:
        # 身份运算符用于比较两个对象的内存地址是否一致 —— 是否是对同一个对象的引用
        # 在Python中针对None比较时，建议使用 is 判断
        if self.gun is None:
            print("[%s] 还没有枪..." % self.name)

            return

        # 2. 高喊口号
        print("冲啊...[%s]" % self.name)

        # 3. 让枪装填子弹
        self.gun.add_bullet(50)

        # 4. 让枪发射子弹
        self.gun.shoot()

# 创建枪对象
ak47 = Gun("ak47")
# ak47.add_bullet(50)
# ak47.shoot()

xusanduo = Soldier("许三多")
xusanduo.gun = ak47
xusanduo.fire()
print(xusanduo.gun)