class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

root = BinaryTree(10)
root.left = BinaryTree(5)
root.right = BinaryTree(15)
root.left.left = BinaryTree(2)
root.left.right = BinaryTree(5)
root.right.right = BinaryTree(22)
root.left.left.left = BinaryTree(1)

# My Sol : Inorder
def inorder(tree, array=[]):
    if tree.left != None : inorder(tree.left, array)
    array.append(tree.value)
    if tree.right != None : inorder(tree.right, array)
    return array

print("Inorder : ", inorder(root))

def preorder(tree, array=[]):
    array.append(tree.value)
    if tree.left != None : preorder(tree.left, array)
    if tree.right != None : preorder(tree.right, array)
    return array

print("Preorder : ", preorder(root))

def postorder(tree, array=[]):
    if tree.left != None : postorder(tree.left, array)
    if tree.right != None : postorder(tree.right, array)
    array.append(tree.value)
    return array

print("Postorder : ", postorder(root))