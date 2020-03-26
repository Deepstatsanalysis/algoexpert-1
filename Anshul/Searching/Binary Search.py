# My Solution

list = [0,1,21,33,24,34,62,73,87,91]

binarysearch = lambda a, key, low, high : False if (low>high) else( True if (key == a[((low+high)//2)]) else( binarysearch(a,key,low,((low+high)//2)-1) if(key<a[((low+high)//2)]) else binarysearch(a,key,((low+high)//2)+1,high)))


print(binarysearch(list,73,0,9))
print(binarysearch(list,74,0,9))