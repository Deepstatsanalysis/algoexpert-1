def ValideteBST(tree):
    return isBST(tree,float("-inf"),float("inf"))


def isBST(tree,min,max):
    if tree is None:
        return True

    if tree.value<min or tree.value>max:
        return False

    return isBST(tree.left,min,tree.value) and isBST(tree.right,tree.value,max)        