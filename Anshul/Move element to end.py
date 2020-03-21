list,value = [2,1,2,2,2,3,4,2],2
print(list)

# My Solution 1

def solve(arr,value,count=0):
    i=0
    j=len(arr)-1
    while j>i:
        if arr[i] == value:
            while arr[j] == value:
                j -= 1
                count+=1
            arr[i],arr[j] = arr[j],arr[i]
        count+=1
        i+=1
    return [arr,'Count',count]

print(solve(list,value))

# My Solution 2   Time : O(n) || Space O(1)

def solve2(arr,value,count=0):
    i=0
    j=len(arr)-1
    while j>i:
        count+=1
        if arr[i] == value and arr[j] == value:
            j-=1
        if arr[i] == value and arr[j] != value:
            arr[i],arr[j] = arr[j],arr[i] 
            i+=1
            j-=1
        if arr[i] != value and arr[j] == value:
            j-=1
        if arr[i] != value and arr[j] != value:
            i+=1
    return [arr,'Count',count]
        

print(solve2(list,value))

