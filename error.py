'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    stdin = input().split(' ')
    a = int(stdin[0])
    b = int(stdin[1])
        
    try:
        print(a//b)
        
    except TypeError as e:
        print('Error Code:',e)

    except ZeroDivisionError as e:
        print('Error Code:',e)

    except SyntaxError as e:
        print('Error Code:',e)
        
    except ValueError as e:
        print('Error Code:',e)
        
    except TypeError as e:
        print('Error Code:',e)
'''
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
       
    try:
        stdin = input().split(' ')
        a = int(stdin[0])
        b = int(stdin[1])
        print(a//b)
    except BaseException as e:
        print('Error Code:',e)

'''
