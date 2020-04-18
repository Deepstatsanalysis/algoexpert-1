listEx = [7,6,4,-1,1,2]
n=13  


def prevCheck(arr,index, d):
    for j in range(index):
        term = arr[j]+arr[index]
        if term not in d:
            d[term] = [arr[j],arr[index]]
        else:
            d[term].append([arr[j],arr[index]])
def solve(arr,value):
    d = {}
    ans = []
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if value-(arr[i]+arr[j]) in d:
                ans.append(d[value-(arr[i]+arr[j])]+[arr[i],arr[j]])
        prevCheck(arr,i, d)
        

    return ans


print(solve(listEx,n))
    