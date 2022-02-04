num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    #print(digit)
    print(reversed_num)
    reversed_num = reversed_num * 10 + digit
    print(reversed_num)
    num //= 10

print("Reversed Number: " + str(reversed_num))
