def YCA(rootnode,descendant1,descendant2):
    depth1=getdepth(descendant1,rootnode)
    depth2=getdepth(descendant2,rootnode)
    if depth1>depth2:
        return upside(descendant1,descendant2,depth1-depth2)

    else:
        return upside(descendant2,descendant1,descendant2-descendant1)

def getdepth(descendant,rootnode):
    depth=0
    while descendant!=rootnode:
        depth+=1
        descendant=descendant.ancestor
    return depth


def upside(lowerdescendant,higherdescendent,diff):
    while diff>0:
        lowerdescendant=lowerdescendant.ancestor
        diff-=1

    while lowerdescendant!=higherdescendent:
        lowerdescendant=lowerdescendant.ancestor
        higherdescendent=higherdescendent.ancestor
    return higherdescendent                            