class A:
    def test(self):
        print("test方法")
class B:
    def demo(self):
        print("demo方法")
class C(A,B):
    pass

c=C()
c.test()
c.demo()
