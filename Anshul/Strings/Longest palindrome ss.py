string = 'abaxyzzyxflwgbauufnsrkjbsichutiyatohtuhaiiahuthotayituhcamwlmfkanwgsngnabghgba'

# My Sol
def lps(string,jk = []):
    if len(string) == 2:
        if string[0]==string[1]:return string
    for i in range(len(string)-2):
        if string[i] == string[i+1]: check(string, i, i+1,jk)
        elif string[i] == string[i+2]: check(string, i, i+2,jk)
    mp=string[0]
    for i in jk:
        if len(mp)<len(i):mp=i
    return mp


def check(string, i, j,jk):
    if i == 0 : 
        jk.append(string[i:j+1])
    elif j<len(string)-1 and string[i-1] == string[j+1]:
        check(string, i-1, j+1,jk)
    else: 
        jk.append(string[i:j+1])
        return

print('Mine : ',lps(string))


# Chutiye ka Sol

def longestP(string):
    cL = [0,1]
    for i in range(1,len(string)):
        odd = getLP(string, i-1, i+1)
        even = getLP(string, i-1,i)
        longest = max(odd, even, key = lambda x:x[1]-x[0])
        cL = max(longest, cL, key = lambda x: x[1]-x[0])
    return string[cL[0]:cL[1]]


def getLP(string, lI, rI):
    while lI >=0 and rI < len(string):
        if string[lI] != string[rI]:
            break
        lI -=1
        rI +=1
    return [lI +1, rI]

print('Algo : ',longestP(string))