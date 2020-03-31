class DoublyLinkedList:
    def inner (self):
        self.head=None
        self.tail=None





def Search(self,value):
    node=self.head
    while node is not None and node.value!=value:
        node=node.next 

    return node is not None



def remove(self,node):
    if node==self.head:
        self.head=self.head.next
    if node==self.tail:
        self.tail=self.tail.prev

    if node.prev is not None:
        node.prev.next=node.next
        
    if node.next is not None:
        node.next.prev=node.prev  

    node.prev=None
    node.next=None


def RemoveNodesWithValue(self,value):
    node=self.head
    while node is not None:
        nodetoremove=node
        node=node.next
        if nodetoremove.value==value:
            self.remove(nodetoremove)



def InsertBefore(self,node,nodetoinsert):
    if nodetoinsert ==self.head and nodetoinsert == self.tail:
        return

    self.remove(nodetoinsert)

    nodetoinsert.prev=node.prev
    nodetoinsert.next=node
    if node.prev is None:
        self.head=nodetoinsert

    else:
        node.prev.next=nodetoinsert
    node.prev=nodetoinsert


def InsertAfter(self,node,nodetoinsert):
    if nodetoinsert == self.tail and nodetoinsert == self.head:
        return

    self.remove(nodetoinsert)

    nodetoinsert.prev=node
    nodetoinsert.next=node.next
    if node.next is None:
        self.tail=nodetoinsert
    else:
        node.next.prev=nodetoinsert
    node.next=nodetoinsert    



def SetHead(self,node):
    if self.head==None:
        self.head=node
        self.tail=node
        return

    self.InsertBefore(self.head,node)     



def SetTail(self,node):
    if self.tail==None:
        self.head=node
        self.tail=node
        return

    self.InsertAfter(self.head,node)         





def InsertAtPosition(self,pos,nodetoinsert):
    if pos==1:
        self.SetHead(nodetoinsert)
        return

    node=self.head

    currpos=1

    while node is not None and currpos!=pos:
        node=node.next
        currpos+=1
        if node is not None:
            self.InsertAfter(node,nodetoinsert)

        else:
            self.SetTail(nodetoinsert)            
            



            

