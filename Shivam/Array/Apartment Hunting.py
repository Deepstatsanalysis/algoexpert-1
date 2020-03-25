def ApartmentHunting(array,reqs):
    mindistance=list(map(lambda a:getmindistance(array,a),reqs))
    maxdistance= getmaxlist(array,mindistance)
    return Finalarray(maxdistance)





def getmindistance(array,a):
    array1=[0 for arrays in array ]
    b=float("inf")
    for i in range(len(array)):
        if array[i][a]:
            b=i
        array1[i]=abs(i-b)


    for i in range(len(array)-1,-1,-1):
        print(array[i],a)
        if array[i][a]:
            b=i
        array1[i]=min(abs(i-b),array1[i])


    return array1



def getmaxlist(array,mindistance):
    maxdistance=[0 for arr in array]
    for i in range(0,len(array)-1):
        mindisblock=list(map(lambda ab:ab[1],mindistance ))
        maxdistance[i]=max(mindisblock)


    return maxdistance



def Finalarray(abc):
    minvalue=float("inf")
    indexmin=0
    for i in range(len(abc)-1):
        if abc[i]<minvalue:
            minvalue=abc[i]
            indexmin=i



    return indexmin



print(ApartmentHunting([{'sc':True,'st':False,'g':False},{'g':True,'sc':False,'st':False},{'g':True,'sc':True,'st':False},{'sc':True,'st':False,'g':False},{'sc':True,'st':True,'g':False}],['g','sc','st']))