from models.NodeModel import Node


class Edge(Node):
    from models import VertexModel
    _allowed_types: str = ["acted_in", "directed"]

    def __init__(self, *, edge_type: str, vertex: VertexModel, **kwargs):
        from models.VertexModel import Vertex

        Node.__init__(self, **kwargs)

        if edge_type not in self._allowed_types:
            raise ValueError()

        self.type = edge_type

        if type(vertex) is not Vertex:
            raise ValueError

        self.vertex = vertex

    def __str__(self):
        return "{} {}".format(self.type, str(self.vertex))
