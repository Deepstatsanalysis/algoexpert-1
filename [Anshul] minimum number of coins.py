def minimumnumberofcoins(value,coins):
    dict = {}
    dict[0] = 0
    for i in range(1, value+1):
        dict[i] = value
        for j in coins:
           if j <= i:
               dict[i] = min( dict[i] , dict[i-j] + 1)
    return dict[value] 

print(minimumnumberofcoins(63,[1,2,10]))