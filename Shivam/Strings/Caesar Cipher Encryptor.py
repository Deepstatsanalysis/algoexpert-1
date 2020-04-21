def cce(string,key):
    array=[]
    newkey=key%26
    for i in string:
        array.append(getletter(i,newkey))
    return "".join(array)

def getletter(i,newkey):
    newcode=ord(i)+newkey
    return chr(newcode) if newcode <=122 else chr(96+newcode%122)

print(cce('xyz',54))            