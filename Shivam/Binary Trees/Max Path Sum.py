def MPS(Node):

    _,maxsum=FindmaxSum(Node)
    return maxsum



def FindmaxSum(Node):
    if Node is None:
        return 0,0


    leftmaxasbranch,maxpathleft=FindmaxSum(Node.left)
    rightmaxasbranch,maxpathright=FindmaxSum(Node.right)
    maxchildsumasbranch=max(leftmaxasbranch,rightmaxasbranch)

    value=Node.value
    maxsumasbranch=max(value,maxchildsumasbranch+value)
    maxchildsumasrootnode=max(maxchildsumasbranch,leftmaxasbranch+rightmaxasbranch+value)
    maxpathsum=max(maxpathleft,maxpathright,maxchildsumasrootnode)

    return(maxsumasbranch,maxpathsum)
