def ClosestValueInBST(tree,target):                              # This solution is recursive.
    return Recurcive(tree,target,float("inf"))


def Recurcive(tree,target,closest):
    if tree is None:
        return closest


    if abs(target-closest)>abs(target-tree.value):
        closest=tree.value


    if target<tree.value:
        return Recurcive(tree.left,target,closest)

    elif target>tree.value:
        return Recurcive(tree.right,target,closest)


    else:
        return closest






# Iterative Solution.


def Sol2(tree,target):
    closest=float("inf")
    currentnode=tree
    while currentnode is not None:
        if abs(target-closest)>abs(target-currentnode.value):
            closest=currentnode.value


        if target<currentnode.value:
            currentnode=currentnode.left

        elif target>currentnode.value:
            currentnode=currentnode.right


        else:
            break

    return closest    
