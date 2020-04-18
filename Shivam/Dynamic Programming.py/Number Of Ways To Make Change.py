def NOWTMC(n,array):
    amount=[0 for price in range(n+1)]
    amount[0]=1
    for arr in array:
        for price in range(1,n+1):
            if arr<=price:
                amount[price]+=amount[price-arr]

    return amount[n]     


