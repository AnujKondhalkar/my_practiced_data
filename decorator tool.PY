def dec1(f1):
    print('here we go')
    f1()
    print('here we stop')


@dec1
def d1():
    print('so in d1')


@dec1
def d2():
    print('so in d2')
