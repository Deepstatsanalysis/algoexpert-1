
# Solution 1 {Hashing Table}
def solve(arr,value):
    dict = {}
    for i in arr :
        if (value - i) in dict:
            return [value-i,i]
        dict[i] = True


# Solution 2 
def solve2(arr,value):
    arr.sort()
    a=0
    b=len(arr)-1
    while arr[a]+arr[b] != value:
        if arr[a]+arr[b] > value:
            b -= 1
        else:
            a += 1
    return [arr[b],arr[a]]


print(solve2([3,5,-4,8,11,1,-1,6,5],10))
