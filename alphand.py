'''
In the first line, print True if s has any alphanumeric characters. Otherwise, print False.
In the second line, print True if s has any alphabetical characters. Otherwise, print False.
In the third line, print True if s has any digits. Otherwise, print False.
In the fourth line, print True if s has any lowercase characters. Otherwise, print False.
In the fifth line, print True if s has any uppercase characters. Otherwise, print False.
'''

if __name__ == '__main__':
    
    s = input()




    
    for i in range(len(s)):
        if s[i].isalnum()==True:
            a = True
        else:
            b = False
    m=(a or b)
    print(m)
    for i in range(len(s)):
        if s[i].isalpha()==True:
            a = True
        else:
            b = False
    
    m=(a or b)
    print(m)
    for i in range(len(s)):
        if s[i].isdigit()==True:
            a = True
        else:
            b = False
    m=(a or b)
    print(m)
    for i in range(len(s)):
        if s[i].islower()==True:
            a = True
        else:
            b = False
    m=(a or b)
    print(m)
    for i in range(len(s)):
        if s[i].isupper()==True:
            a = True
        else:
            b = False
    m=(a or b)
    print(m) 
    
    '''
    A=print(True) if s.isalnum()== True else print(False)
    B=print(True) if s.isalpha()== True else print(False)
    C=print(True) if s.isdigit()== True else print(False)
    D=print(True) if s.islower()== True else print(False)
    E=print(True) if s.isupper()== True else print(False)
    '''
