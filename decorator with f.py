def f1(f):
    print("hi")
    def yy():
        print("in '''  in")
@f1.yy()
def f2(f):
    print('yo')
