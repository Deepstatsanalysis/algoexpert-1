# 3
# 2 2
# 3 2
# 2 3

  
# Case #1: 1
# 2 1
# Case #2: 2
# 3 2
# 2 1
# Case #3: 2

def standard_input():
    yield 1
    yield '2 3'


def swap(ans,index,count,A,B):
    temp=count
    value = ans[index]
    while count>0:
        for i in range(index+1,len(ans)-1):
            if ans[i] == value:
                arr1 = ans[i:]
                arr2 = ans[index+1:i]
                print(ans)
                A.append(len(arr1))
                B.append(len(arr2))
                ans = ans[:index+1]+arr1+arr2
        index+=1
        count-=1
    count=temp
    return ans




testCase = int(input())
for i in range(testCase):
    n = list(map(int,input().split()))
    ans = []
    count = 0
    A = []
    B = []
    for j in range(n[1]):
        for k in range(n[0],0,-1):
            ans.append(k)
        count+=1
    for m in range(n[0],0,-1):
        temp=count
        value = m
        iop=ans.index(m)
        while count>0:
            for i in range(iop+1,len(ans)-1):
                if ans[i] == value:
                    arr1 = ans[i:]
                    arr2 = ans[iop+1:i]
                    A.append(len(arr1))
                    B.append(len(arr2))
                    ans = ans[:iop+1]+arr1+arr2
            iop+=1
            count-=1
        count=temp
    print(A,B)

    
    