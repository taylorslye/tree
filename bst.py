#a tree by Taylor Slye, cs261


class BinarySearchTree:
    def __init__(self, value = None):
        self.value = value
        self.right = None
        self.left = None
    
    def get_right(self):
        return self.right
    
    def get_left(self):
        return self.left

    def append(self, appendee):
        if appendee.value > self.value:
            if self.right == None:
                self.right = appendee
            else:
                self.get_right().append(appendee)
        elif appendee.value < self.value:
            if self.left == None:
                self.left = appendee
            else:
                self.get_left().append(appendee)


    def preorder_search(self):
        #this goes node, left, right
        
        try:
            search
        except NameError:
            search = []
        search.append(self.value)
        print(self.value)
        if self.left != None:
            next = self.left
            next.preorder_search()
        if self.right !=  None:
            next = self.right
            next.preorder_search()
        return search

    def inorder_search(self):
        #this goes node, left, right
        
        try:
            search
        except NameError:
            search = []
        
        
        if self.left != None:
            next = self.left
            next.preorder_search()
        search.append(self.value)
        if self.right !=  None:
            next = self.right
            next.preorder_search()
        print(self.value)
        return search

    def postorder_search(self):
        #this goes 
        
        try:
            search
        except NameError:
            search = []
        
        
        if self.left != None:
            next = self.left
            next.preorder_search()
        if self.right !=  None:
            next = self.right
            next.preorder_search()
        print(self.value)
        search.append(self.value)
        return search
