def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    count=0
    n_flag=1
    l_flag=1
    u_flag=1
    sc_flag=1
    for i in range(n):
        if password[i] in numbers:
            n_flag=0
        if password[i] in lower_case:
            l_flag=0
        if password[i] in upper_case:
            u_flag=0
        if password[i] in special_characters:
            sc_flag=0
    extra_char=n_flag+l_flag+u_flag+sc_flag
    if n>=6:
        return extra_char
    elif n+extra_char>=6:
        return extra_char 
    elif n+extra_char<6:
        return 6-n
    
if __name__=="__main__":
    password='SQZPA'
    n=len(password)
    print(minimumNumber(n, password))
