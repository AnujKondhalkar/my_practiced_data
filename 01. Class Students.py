class student:

    def __init__(self,w,x,y,z):
        self.rollno=w
        self.name=x
        self.semester=y
        self.branch=z
    
    def f1(self):
        print('Student roll number is =',self.rollno)
        print('Student name is =',self.name)
        print('Student semester is =',self.semester)
        print('Student branch is =',self.branch)

    def f2(self,a):
        print(f'square of {a} is ',a**2,' in f2')

    def f3(self,a):
        print(f"f3 object is {a} ")
'''
a=int(input("Provide the roll number = "))
b=str(input("Provide the name of student = "))
c=int(input("Provide the semester year = "))
d=str(input("Provide the name of the branch = "))
'''
s1=student(123,'Amar',8,'EE')
s1.f1()
s1.f2(8)
l=s1.__dict__
print(l)
s2=student(456,'Samar',4,'EL')
s2.f1()
s2.f3('s2')
