class say():
    def hello(self):
        print('hello')

    def hi(self):
        self.hello()
        print('hi')

    def hey(self):
        self.hi()
        print('hey')

a=say().hey()

