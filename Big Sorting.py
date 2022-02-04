def bigSorting(unsorted):
    # Write your code here
    #ls=[int(i) for i in unsorted]
    #ls_s=[str(i) for i in unsorted]
    #ls_s=sorted(ls)
    unsorted.sort(key = lambda x:(len(x),x))
    return(unsorted)
    
unsorted=['11','42','2','13','5','6','7','2','8','9']
print(bigSorting(unsorted))

    
