class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def branchSums(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums


def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return

    newRunningSum = runningSum + node.value

    print('node',node.value)
    print('runningsum',runningSum)
    print('newrunningsum',newRunningSum)
    print("         ")
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        print('sums',sums)
        return
    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)


# O(n) time  | O(n) space


root = BinaryTree(10)
root.left = BinaryTree(2)
root.right = BinaryTree(11)

root.left.left = BinaryTree(4)
root.left.right = BinaryTree(6)
root.right.left = BinaryTree(9)
root.right.right = BinaryTree(15)

print(branchSums(root))
#