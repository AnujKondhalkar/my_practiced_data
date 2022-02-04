'''
a=5
for i in range(1,a+1):
    print(i)
    k=1
    for j in range(1,(2*i)):
        if (j>=(a+1-i) and j<=(a-1+i) and k):
            print('*',end='')
            k=0
        else:
            print(' ',end='')
            k=1
    print("")
input()     
'''
# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern triangle
def triangle(n):
	
	# number of spaces
	k = n - 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# inner loop to handle number spaces
		# values changing acc. to requirement
		for j in range(0, k):
			print(end=" ")
	
		# decrementing k after each loop
		k = k - 1
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("* ", end="")
	
		# ending line after each row
		print("\r")

# Driver Code
n = 55
triangle(n)
