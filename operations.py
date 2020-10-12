import bTree


class ProductCreated:
    '''
    ProductCreated main class responsible for adding new produciton in a B-Tree
    '''

    root = None

    def __init__(self, _timestamp, _type, _id, _parent_id, _stock ):
        self.timestamp = _timestamp
        self.type = _type
        self.id = _id
        self.parent = _parent_id
        self.stock = _stock

    def run(self):
        if self.parent is None:
            ProductCreated.root = bTree.Node(self.id, self.stock)
        else:
            ProductCreated.root = ProductCreated.root.get(self.parent)
            ProductCreated.root.insert(self.id)
            ProductCreated.root.PrintTree()

    def __repr__(self):
        return self.__dict__

class ProductUpdated:
    '''
    ProductUpdated main class responsible for updating stocks
    '''

    root = None

    def __init__(self, _timestamp, _type, _id, _stock):
        self.timestamp = _timestamp
        self.type = _type
        self.id = _id
        self.stock = _stock

    def run(self):
        ProductUpdated.root = ProductCreated.root.get(self.id)
        ProductUpdated.root.update(self.stock)

        ProductUpdated.root.PrintTree()

    def __repr__(self):
        return self.__dict__

class ProductEnded:
    '''
    ProductEnded main class responsible for ending product
    '''

    def __init__(self, _timestamp, _type, _id):
        pass

    def __str__(self):
        return __class__.__name__
