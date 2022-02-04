def migratoryBirds(arr):
    # Write your code here
    l_k=[]
    l_v=[]
    id_count=dict()
    for i in arr:
        if i in id_count:
            pass
        else:
            id_count[i]=arr.count(i)
    #print(id_count)
    sort_dict=(sorted(id_count.items(), key =lambda kv:(kv[1], kv[0])))   

    for key,value in sort_dict:
        l_k.append(key)
        l_v.append(value)
    #print(l_k)    
    #print((l_v))
    ind=l_v.index(max(l_v))
    return(l_k[ind])

     
# main function calling
if __name__=="__main__":     
    arr=[1,4,4,4,5,3]
    arr.sort()
    result=migratoryBirds(arr)
    print(result)
