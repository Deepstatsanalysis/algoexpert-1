class Node:
    def __init__(self, name):
        self.childern = []
        self.name = name

    def addChild(self, name):
        self.childern.append(Node(name))

    def DFS(self, array):
        array.append(self.name)
        print(array)
        for child in self.childern:
            child.DFS(array)
        return array


        

root = Node('A')
root.addChild('B')
root.addChild('D')
root.addChild('I')

root.childern[0].addChild('C')

root.childern[1].addChild('E')
root.childern[1].addChild('G')
root.childern[1].addChild('H')

root.childern[2].addChild('J')
root.childern[2].addChild('K')

root.childern[1].childern[0].addChild('F')
root.childern[2].childern[1].addChild('L')

print(root.DFS([]))


