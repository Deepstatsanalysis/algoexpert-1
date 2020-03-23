
# My Solution -> via DFS

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)

root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

root.left.left.left = BinaryTree(8)
root.left.left.right = BinaryTree(9)

def printBinary(root,array=[]):
    array.append(root.value)
    if root.left != None:
        printBinary(root.left,array)
    if root.right != None:
        printBinary(root.right,array)
    return array


# Code Starts Here : Time O(n) || Space O(log(n)) or O(d))

def invertBinary(root):
    if root.left != None : invertBinary(root.left)
    if root.right != None : invertBinary(root.right)
    root.left,root.right = root.right,root.left
    return root

print(printBinary(root,[]))
print(printBinary(invertBinary(root),[]))