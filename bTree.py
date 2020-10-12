class Node:
    '''
    Main Node class
    '''

    def __init__(self, data, stock):
        '''
        Initialize new ProductStack
        '''

        self.left = None
        self.right = None
        self.parent = None
        self.data = data
        self.stock = stock

    def insert(self, data):
        '''
        Insert new node and link to parent
        '''

        if self.left is None:
            self.left = Node(data, self.stock)
            self.left.parent = self
            return self.left

        if self.right is None:
            self.right = Node(data, self.stock)
            self.right.parent = self
            return self.right

    def update(self, stock):
        '''
        Update node with new stock value
        '''

        self.stock = stock

        if self.stock == 0:
            if self.parent:
                self.parent.update(stock)

        if not self.stock:
            self.delete()

    def get(self, data):
        '''
        Get node by ID
        '''

        if self.data == data:
            return self

        if self.left:
            return self.left.get(data)
        else:
            self = self.parent

        if self.right:
            return self.right.get(data)

    def delete(self):
        '''
        Delete child from the Tree
        '''
        if self.parent is None:
            if self.left:
                self.left = None
            if self.right:
                self.right = None

    def PrintTree(self):
        '''
        Print Tree's state
        '''

        self.stocks[self.data] = self.stock

        if self.left:
            self.stocks[self.left.data] = self.left.stock

        if self.right:
            self.stocks[self.right.data] = self.right.stock

        print(self.stocks)


def serialize(node, s=""):
    if(not node):
        s += ""
        return s

    s += '"' + (str(node.data)+": " + str(node.stock) + ", ")
    s = serialize(node.left, s=s)
    s = serialize(node.right, s=s)
    return(s)
