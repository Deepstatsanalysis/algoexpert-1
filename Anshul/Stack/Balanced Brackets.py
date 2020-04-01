brackets = '(([]()()){})'
# sol 1
def solve(arr, stack=[]):
    d = {'[':']','{':'}','(':')'}
    d2 = {']':'[','}':'{',')':'('}
    for i in arr:
        if i in d:
            stack.append(i)
        else:
            if d2[i] == stack[-1]:
                print(stack)
                stack.pop()

    if len(stack) !=0 :
        print(stack)
        return False
    return True

print(solve(brackets))