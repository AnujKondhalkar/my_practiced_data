class Test:
    def __init__(self):
       pass
    def f2(self,x):
        print('hello',x)
        def f1():
            print('hi')
        f1()
t=Test()
t.f2(5)

