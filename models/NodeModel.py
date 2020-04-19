class Node:
    def __init__(self, **kwargs):
        if type(self) == "models.Vertex.Vertex" and "name" not in kwargs:
            raise ValueError()
        self.data = kwargs
