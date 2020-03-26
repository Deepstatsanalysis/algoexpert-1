# BST Construction
# Not Complete

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, value):
        currentNode = self
        while True:   # Neither low nor high ?
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BinaryTree(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BinaryTree(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    def getMinvalue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value

    def search(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
                break
            else:
                currentNode = currentNode.right
        return self                       # Not self.value ?


    def delete(self, value, parentNode=None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinvalue()
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.right = currentNode.right.right
                        currentNode.left = currentNode.right.left
                    else:
                        currentNode.value = None
                elif parentNode.left==currentNode:
                    parentNode.left=currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right==currentNode:
                    parentNode.right= currentNode.left if currentNode.left is not None else currentNode.right
                break


        return self




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


print(root.delete(10))
