testCase = int(input())
for d in range(testCase):
    n = list(map(int,input().split()))
    ans = []
    count = 0
    A = []
    B = []
    for j in range(n[1]):
        for k in range(n[0],0,-1):
            ans.append(k)
    count = n[0]
    
    for m in range(n[0],0,-1):
        temp=count
        value = m
        iop=ans.index(m)
        while count>0:
            for i in range(iop+1,len(ans)-1):
                if ans[i] == value:
                    arr1 = ans[i:]
                    arr2 = ans[iop+1:i]
                    if len(arr2) == 0 or len(arr1) == 0: break
                    A.append(len(arr1))
                    B.append(len(arr2))
                    ans = ans[:iop+1]+arr1+arr2
                    iop+=1
            count-=1
        count=temp
    print("Case #{}: {}".format(d+1,len(A)))
    for i,j in zip(A,B):
        print(i,j)

    
    