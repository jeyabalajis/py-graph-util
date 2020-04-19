from core.Node import Node
from core.Edge import Edge


class Vertex(Node):
    _allowed_types = ['Actor', 'Movie']

    def __init__(self, *, node_type: str, edges: [Edge] = None, **kwargs):
        Node.__init__(self, **kwargs)

        if node_type not in self._allowed_types:
            raise ValueError()

        self.type = node_type
        self.edges = edges if edges else []

    def add_edge(self, edge: Edge):
        self.edges.append(edge)

    def __str__(self):
        str_edges = ""
        if self.edges:
            for edge in self.edges:
                str_edges = str_edges.join(str(edge))

        return "{} {} {}".format(self.type, self.data.get("name"), str_edges)
