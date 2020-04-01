brackets = '{(([]()([])){})}'
# sol 1
def solve(arr, stack=[]):
    d = {']':'[','}':'{',')':'('}
    for i in arr:
        if i not in d:
            stack.append(i)
        else:
            if stack == []:
                return False
            elif d[i] == stack[-1]:
                print(stack)
                stack.pop()

    if len(stack) !=0 :
        print(stack)
        return False
    return True

print(solve(brackets))