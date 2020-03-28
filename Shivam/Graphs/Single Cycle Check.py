def SCC(array):
    visited=0
    currindx=0
    while visited<len(array):
        if visited>0 and currindx==0:
            return False

        visited+=1
        jump=array[currindx]
        nectindx=(currindx+jump) % len(array)
        currindx=nectindx if nectindx>=0 else nectindx +len(array)
    return currindx==0