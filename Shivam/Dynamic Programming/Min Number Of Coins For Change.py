def MinNoOfCoins(n,denoms):
    numofcoins=[float("inf") for amount in range(n+1)]
    numofcoins[0]=0
    for denom in denoms:
        for amount in range(len(numofcoins)):
            if denom<=amount:
                numofcoins[amount]=min(numofcoins[amount],1+numofcoins[amount-denom])
    return numofcoins[n] if numofcoins[n]!=float("inf") else -1





print(MinNoOfCoins(6,[1,2,4]))                 