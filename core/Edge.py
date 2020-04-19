from core.Node import Node


class Edge(Node):
    _allowed_types: str = ["acted_in", "directed"]

    def __init__(self, *, edge_type: str, vertex: Node, **kwargs):
        Node.__init__(self, **kwargs)

        if edge_type not in self._allowed_types:
            raise ValueError()

        self.type = edge_type
        self.vertex = vertex

    def __str__(self):
        return "{} {}".format(self.type, str(self.vertex))
