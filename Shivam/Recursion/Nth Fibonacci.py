def fib(n,dic={1:0,2:1}):
    if n in dic:
        return dic[n]

    else:
        dic[n]=fib(n-1,dic)+fib(n-2,dic)

    return dic[n]



def fibb(n):
    arr=[0,1]
    count=3
    while count<=n:
        nextfib=arr[0]+arr[1]
        arr[0]=arr[1]
        arr[1]=nextfib
        count+=1

    return arr[1] if n>1 else arr[0]                    