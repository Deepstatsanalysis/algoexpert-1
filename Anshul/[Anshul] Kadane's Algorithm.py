list = [3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4] 


def solve(arr):
    a = arr[0]
    b = arr[0]
    for i in arr[1:len(arr)]:
        a = max(i,a+i)
        b = max(a,b)
        
    return b

print(solve(list))


