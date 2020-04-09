def InvertBinaryTree(Node):
    queue=[Node]

    while len(queue):
        curr=queue.pop(0)
        if curr is None:
            continue
        swapchildren(curr)
        queue.append(curr.left)
        queue.append(curr.right)


def swapchildren(Node):
    Node.left,Node.right=Node.right,Node.left






#Sol2

def IBT(Tree):
    if Tree is None:
        return

    swap(Tree)
    IBT(Tree.left)
    IBT(Tree.right)

def swap(Tree):
    Tree.left,Tree.right=Tree.right,Tree.left

