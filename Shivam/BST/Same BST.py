def SameBST(array1,array2):                        #Sol1
    if array1[0]!=array2[0]:
        return False

    if len(array1)!=len(array2):
        return False

    if len(array1)==0 :
        return True


    left1 = getsmaller(array1)
    left2 = getsmaller(array2)
    right1 = getbigger(array1)
    right2 = getbigger(array2)

    return SameBST(left1,left2) and SameBST(right1,right2)


def getsmaller(arr):
    smaller=[]
    for i in range(1,len(arr)):
        if arr[i]<arr[0]:
            smaller.append(arr[i])

    return smaller

def getbigger(arr):
    bigger=[]
    for i in range(1,len(arr)):
        if arr[i]>=arr[0]:
            bigger.append(arr[i])

    return bigger                    





#Sol2

def SameBST1(arr1,arr2):
    return check(arr1,arr2,0,0,float("-inf"),float("inf"))


def check(arr1,arr2,rootind1,rootind2,min1,max1):
    if rootind1==-1 or rootind2==-1:
        return rootind1==rootind2


    if arr1[rootind1]!=arr2[rootind2]:
        return False


    leftrootind1 = getsmallerindx(arr1,rootind1,min1)
    leftrootind2 = getsmallerindx(arr2,rootind2,min1)
    rightrootind1 = getbiggerindx(arr1,rootind1,max1)
    rightrootind2 = getbiggerindx(arr2,rootind2,max1)

    currvalue=arr2[rootind2]

    leftaresame=check(arr1,arr2,leftrootind1,leftrootind2,min1,currvalue)
    rightaresame=check(arr1,arr2,rightrootind1,rightrootind2,currvalue,max1)

    return leftaresame and rightaresame










def getsmallerindx(arr1,startingindx,min1):
    for i in range(startingindx+1,len(arr1)):
        if arr1[i]<arr1[startingindx] and arr1[i]>=min1:
            return i

    return -1

def getbiggerindx(arr2,startingindx,max1):
    for i in range(startingindx+1,len(arr2)):
        if arr2[i]>startingindx and arr2[i]<=max1:
            return i

    return -1                    
