def productsums(arr,m=1):
    sum=0
    for i in arr:
        if type(i) is list:
            sum=productsums(i,m+1) 
        else:
            sum+=i
    return m*sum            