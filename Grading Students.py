def gradingStudents(grades):
    # Write your code here
    ls=[]
    for i in grades:
        
        p=(i%5)-5
        r=i>37
        
        if (p>-3 and r):
            ls.append(i+(-p))
            
        elif (p>2 and r):

            ls.append(i+(p))
        else:
            
            ls.append(i)
    return ls

'''
for _ in range(int(input())):
    x = int(input())
    x = x-x%5+5 if x%5>2 and x>=38 else x
    print(x)
'''


if __name__ == '__main__':
    grades = [73,67,38,33,37,70]
    result = gradingStudents(grades)
    for item in result:
        print(item)
