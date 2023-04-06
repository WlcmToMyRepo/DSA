class Tree:
    def __init__(self, data = None, left= None, right = None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def search(self,data):
        if self.data == data:
            return True
        elif data < self.data and self.left:
            return self.left.search(data)
        elif self.right:
            return self.right.search(data)
        else:
            return False

    def insert(self,data):
        if data <= self.data:
            if self.left == None:
                self.left = Tree(data)
            else:
                self.left.insert(data)
        else:
            if self.right == None:
                self.right = Tree(data)
            else:
                self.right.insert(data)
        
    def inorder(self):
        if self.left:
            self.left.inorder()
        print("\\")
        print(self.data)
        print("/")
        if self.right:
            self.right.inorder()
        print("------------")
t = Tree(100,Tree(98),Tree(110,Tree(105),Tree(115)))
t.inorder()


