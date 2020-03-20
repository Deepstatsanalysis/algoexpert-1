list = [5,2,[7,-1],3,[6,[-13,8],4]]

def solve(arr,call=1):
    n=0
    for i in arr:
        if type(i)==int:
            n+=i
        else:
            call+=1
            n+=solve(i,call)
            call-=1
    return n*call

print(solve(list))