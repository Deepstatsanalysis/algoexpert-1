def inorder(tree,array):
    if tree is not None:
        inorder(tree.left,array)
        array.append(tree.value)
        inorder(tree.right,array)
    return array    




def preorder(tree,array):
    if tree is not None:
        array.append(tree.value)
        preorder(tree.left,array)
        
        preorder(tree.right,array)
    return array    



def postorder(tree,array):
    if tree is not None:
        postorder(tree.left,array)
        
        postorder(tree.right,array)
        array.append(tree.value)
    return array            