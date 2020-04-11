import math as mt
def factors(a):
    MAX = 1000001
    factor = [0]*(MAX + 1)
    def calculateNoOFactors(n):
        if (n == 1):
            return 1
        ans = 1
        dup = factor[n]
        c = 1
        j = int(n / factor[n])
        while (j > 1):
            if (factor[j] == dup):
                c += 1
            else:
                dup = factor[j]
                ans = ans * (c + 1)
                c = 1
            j = int(j / factor[j])
        ans = ans * (c + 1)
        return ans

    factor[1] = 1
    for i in range(2, MAX):
        factor[i] = i
    for i in range(4, MAX, 2):
        factor[i] = 2
    i = 3
    while(i * i < MAX):
        if (factor[i] == i):
            j = i * i
            while(j < MAX):
                if (factor[j] == j):
                    factor[j] = i
                j += i
        i += 1
    return calculateNoOFactors(a)


def getFactorization(x): #Prime
    MAXN = 1000001
    spf = [0 for i in range(MAXN)]
    spf[1] = 1
    for i in range(2, MAXN):                                                          
        spf[i] = i                           
    for i in range(4, MAXN, 2): 
        spf[i] = 2
    for i in range(3, mt.ceil(mt.sqrt(MAXN))):                       
        if (spf[i] == i):
            for j in range(i * i, MAXN, i):                      
                if (spf[j] == j): 
                    spf[j] = i 
    ret = list() 
    while (x != 1): 
        ret.append(spf[x]) 
        x = x // spf[x]
    return ret 




print(getFactorization(900000000))