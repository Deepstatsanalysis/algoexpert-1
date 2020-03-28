class BinaryTree:
    def func(self,value):
        self.value=value
        self.left=None
        self.right=None



def BranchSums(root):
    final=[]
    traverse(root,0,final)
    return final


def traverse(node,currsum,final):
    if node is None:
        return

    newsum=currsum+node.value    
    if node.left is None and node.right is None:
        final.append(newsum)
        return

    traverse(node.left,newsum,final)
    traverse(node.right,newsum,final)    