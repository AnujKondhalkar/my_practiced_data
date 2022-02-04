class base:
    x=11
    def __init__(self):
        self.a=10
    def f1():
         print(base.x)

class Derived(base):
    def __init__(self):
        super().__init__()
    def f2(self):
        base.f1()



obj=Derived()
obj.f2()
