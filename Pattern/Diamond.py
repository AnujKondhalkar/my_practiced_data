'''num_rows = int(input("Enter the number of rows = "));

for i in range(0, num_rows):
    for j in range(0, num_rows-i-1):
        print(end=" ")
    for j in  range(0, i+1):
        print("*", end=" ")

    print(end='\n')
  
for i in range(0, num_rows):
    for j in  range(i+1,0):
        print("*", end="*")
    for j in range(num_rows-i):
        print(end=" ")
        
'''

num_rows = int(input("Enter the number of rows"))
k = 0
for i in range(1, num_rows + 1):
    for j in range (1, (num_rows - i) + 1):
        print(end = " ")
        while k != (2 * i - 1):
            print("*", end = "")
            k = k + 1
        k = 0
        print()
        k = 2
        m = 1
        for i in range(1, num_rows):
            for j in range (1, k):
                print(end = " ")
            k = k + 1
            while m <= (2 * (num_rows - i) - 1):
                print("*", end = "")
                m = m + 1
                m = 1
                print()
