def Powerset(arr):
    subset=[[]]
    for ele in arr:
        for i in range(len(subset)):
            currsubset=subset[i]
            subset.append(currsubset+[ele])

    return subset



print(Powerset([1,2,3,4,5,6,7,8,9]))    
