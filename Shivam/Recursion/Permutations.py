def Permutation(arr):
    perm=[]
    getperm(0,arr,perm)
    return perm


def getperm(i,arr,perm):
    if i==len(arr)-1:
        perm.append(arr[:])

    else:
        for j in range(i,len(arr)):
            swap(arr,i,j)
            getperm(i+1,arr,perm)
            swap(arr,i,j)

def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]



print(Permutation([1,2,3,4]))