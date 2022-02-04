def bonAppetit(bill, k, b):
    # Write your code here
    b_charged=b
            
    b_actual=(sum(bill)-bill[k])//2
    if (b_actual)-b_charged==0:
        print('Bon Appetit')
    else:
        print(b_charged-(b_actual))
            
        


n=4;k=1
bill=[3,10,2,9]
b=12
print(bonAppetit(bill, k, b))

print('ok')

n=4;k=1
bill=[3,10,2,9]
b=7
print(bonAppetit(bill, k, b))
