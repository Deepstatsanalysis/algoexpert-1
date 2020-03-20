list = [5,2,[7,-1],3,[6,[-13,8],4]]

def solve(arr):
    n=0
    for i in arr:
        if type(i)==int:
            n+=i
        else:
            n+=solve(i)
    return n


print(solve(list))