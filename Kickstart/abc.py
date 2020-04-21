testCase = int(input())

for d in range(testCase):
    n=list(map(int,input().split()))
    k=list(map(int,input().split()))   
    b=n[1]    


    for i in reversed(range(len(k))):
        
            prev=b

            b=b%k[i] 
            c=prev-b
            b=c
        #else: n[1]%k[i]==0
    

    


    print("Case #{}: {}".format(d+1,b))



