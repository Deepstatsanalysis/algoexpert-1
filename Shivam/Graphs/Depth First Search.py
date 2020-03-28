class Node:
    def init(self,name):
        self.children=[]
        self.name=name


    def addchild(self,name):
        self.children.append(Node(name))



    def DFS(self,array):
        array.append(self.name)
        for child in self.children:
            child.DFS(array)
        return array            
