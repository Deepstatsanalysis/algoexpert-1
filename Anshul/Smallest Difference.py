a = [-1,5,10,20,28,3]  # -1,3,5,10,20,28
b = [26,134,29,15,17] # 15,17,26,134,135

# My solution
def smallestdiff(a,b):
    a.sort()
    b.sort()
    mins=abs(a[0]-b[0])
    i = 0
    j = 0
    for _ in range(len(a)+len(b)-2):
        k=mins
        if a[i]<b[j]:
            mins=min(mins,b[j]-a[i])
            if k != mins:pair=[a[i],b[j]]
            i+=1
        else:
            mins=min(mins,a[i]-b[j])
            if k != mins:pair=[a[i],b[j]]
            j+=1
    return [pair,mins]

print(smallestdiff(a,b))