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
root.right.left = BinaryTree(13)
root.right.right = BinaryTree(22)

root.left.left.left = BinaryTree(1)
root.right.left.left = BinaryTree(12)
root.right.left.right = BinaryTree(14)

# Time : O(log(n)) || Space : O(log(n))

def findClosesttarget(root, target, closest):
    if root is None : return closest
    if abs(target - closest) > abs(target - root.value): closest = root.value
    if target < root.value : return findClosesttarget(root.left, target, closest)
    elif target > root.value : return findClosesttarget(root.right, target, closest)
    else: return closest




print(findClosesttarget(root, 19,float("inf") ))