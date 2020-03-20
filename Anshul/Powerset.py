s = [1,2,3,4]


def powerset(array):
    subsets = [[]]
    for i in array:
        for j in range(len(subsets)):
            currentSubset = subsets[j]
            subsets.append(currentSubset + [i])
    return subsets

print(powerset(s))

