n = int(input())
testCase = []
for i in range(n):
    testCase.append(str(input())

def bracket(n):
    if len(n) == 1: return '('*int(n)+n+')'*int(n)
    tempString = ''
    list1 = []
    for i in n:
        list1.append(int(i))
    for i in range(len(list1)):
        if tempString == '':
            tempString = '('*(list1[i])+str(list1[i])
        elif list1[i-1] < list1[i]:
            tempString  += '('*abs(list1[i-1]-list1[i])+str(list1[i])
        else:
            tempString += ')'*abs(list1[i-1]-list1[i])+str(list1[i])
    tempString += ')'*list[-1]
    return tempString
for i,e in enumerate(testCase):
    print('Case #'+str(i)+':',bracket(e))