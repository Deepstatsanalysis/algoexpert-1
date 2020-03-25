class BST:
    def cons(self,value):
        self.value=value
        self.left=None
        self.right=None



    def insert(self,value):
        currentnode=self
        while True:
            if value<currentnode.value:
                if currentnode.left is None:
                    currentnode.left=BST(value)
                    break

                else:
                    currentnode=currentnode.left


            else:
                if currentnode.right is None:
                    currentnode.right=BST(value)
                    break

                else:
                    currentnode=currentnode.right


        return self




    def Search(self,value):
        currentnode=self
        while currentnode is not None:
            if value< currentnode.value:
                currentnode=currentnode.left
            elif currentnode>currentnode.value:
                currentnode=currentnode.right

            else:
                return True


        return False


    def Delete(self,value,parentnode=None):
        currentnode=self

        while currentnode is not None:
            if value<currentnode.value:
                parentnode=currentnode
                currentnode=currentnode.left

            elif value>currentnode.value:
                parentnode=currentnode
                currentnode=currentnode.right

            else:
                if currentnode.left is not None and currentnode.right is not None:
                    currentnode.value=currentnode.right.getminvalue()
                    currentnode.right.remove(currentnode.value,currentnode)

                elif parentnode is None:
                    if currentnode.left is not None:
                        currentnode.value=currentnode.left.value
                        currentnode.right=currentnode.left.right
                        currentnode.left=currentnode.left.left

                    elif currentnode.right is not None:
                        currentnode.value=currentnode.right.value
                        currentnode.left=currentnode.right.left
                        currentnode.right=currentnode.right.right

                    else:
                        currentnode.value=None            


                elif parentnode.left==currentnode:
                    parentnode.left=currentnode.left if currentnode.left is not None else currentnode.right

                elif parentnode.right==currentnode:
                    parentnode.right= currentnode.left if currentnode.left is not None else currentnode.right


                break



        return self



    def getminvalue(self):
        currentnode=self
        while currentnode.left is not None:
            currentnode=currentnode.left


        return currentnode.value    


