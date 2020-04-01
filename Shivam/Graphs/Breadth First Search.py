class Node:
    def init(self,name):
        self.children=[]
        self.name=name

    def addchild(self,name):
        self.children.append(Node(name))




    def BFS(self,array):
        queue=[self]

        while len(queue)>0:
            curr=queue.pop(0)

            array.append(curr.name) 
            for child in curr.children:
                queue.append(child)
        return array             