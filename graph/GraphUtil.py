from models.VertexModel import Vertex


class GraphUtil:
    def __init__(self, *, vertices: [Vertex]):
        if not vertices:
            raise ValueError

        for vertex in vertices:
            if type(vertex) is not Vertex:
                raise ValueError()

        self.vertices = vertices
        # TODO: Organize the vertices as a dictionary of vertex key, followed by their neighbour vertices

    def find_path(self, *, from_vertex: Vertex, to_vertex: Vertex):
        pass
