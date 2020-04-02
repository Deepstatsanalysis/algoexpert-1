list1 = [1,2,4,7,10,11,7,12,6,7,16,18,19]
list2 = [9,8,5,4,2,1,0]

# My Sol 1
def subarray(arr,count=0):
    rangeArr=[-1,-1]
    for i in range(len(arr)):
        minValue = i
        if rangeArr[0] != -1:
            break
        for j in range(i,len(arr)):
            count+=1
            if arr[minValue] > arr[j]:
                rangeArr[0] = minValue
                break
            
    for i in range(len(arr)-1,-1,-1):
        maxValue = i
        if rangeArr[1] != -1:
            break
        for j in range(i-1,-1,-1):
            count+=1
            if arr[maxValue] < arr[j]:
                rangeArr[1] = maxValue
                break
    
    return [rangeArr,'Count : ',count]
print(subarray(list1))


# Efficient one

def subarray2(arr, count=0):
    d={}
    range1=[-1,-1]
    for i in range(len(arr)-1):
        count+=1
        if arr[i+1]<arr[i]:
            d[arr[i]] = False
            d[arr[i+1]] = False
    minValue = min(list(d.keys()))
    maxValue = max(list(d.keys()))
    for j in range(len(arr)):
        count+=1
        if arr[j] > minValue:
            range1[0] = j
            break
    for j in range(len(arr)):
        count+=1
        if arr[j] > maxValue:
            range1[1] = j-1
            break
    return [range1,'Count :',count]


print(subarray2(list1))