class Node:
    def __init__(self, name):
        self.childern = []
        self.name = name

    def addChild(self, name):
        self.childern.append(Node(name))

    def BFS(self, array):
        queue= [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.childern:
                queue.append(child)
        return array




root = Node('A')
root.addChild('B')
root.addChild('C')
root.addChild('D')


root.childern[0].addChild('E')
root.childern[0].addChild('F')

root.childern[2].addChild('G')
root.childern[2].addChild('H')

root.childern[0].childern[0].addChild('I')
root.childern[0].childern[1].addChild('J')
root.childern[2].childern[0].addChild('K')

#[ABCDEFGHIJK]


print(root.BFS([]))