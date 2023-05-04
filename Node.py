class Node:
    # def __init__(self, data, distance=None):
    #     self.data = data  # Data is usually a list containg [row, col]
    #     self.children = []  # List of n children
    #     self.parent = None  # The parent of this node
    #     if distance:
    #         print("distance: {distance}")
    #         self.distance = distance

    def __init__(self, *args):
        self.data = [args[0], args[1]]
        self.children = []
        self.parent = None
        self.depth = 0
        if len(args) > 2:
            self.distance = args[2]

    def add_child(self, child):  # Adds one child to current node and sets it as its parent
        child.parent = self
        child.depth = self.depth + 1
        self.children.append(child)

    def get_depth(self):  # Returns depth (int)
        return self.depth

    def get_children(self):  # Returns list of children
        return self.children

    def get_data(self):  # Returns list of data
        return self.data

    def get_distance(self):  # Returns distance
        return self.distance

    def set_distance(self, distance):  # Returns distance
        self.distance = distance

    def get_parent(self):  # Returns parent node
        return self.parent
