import pytest
from core.Vertex import Vertex
from core.Edge import Edge


class TestVertex:
    def test_vertex(self):
        actor_node_data = {"name": "Tom Hanks"}
        actor_vertex = Vertex(node_type="Actor", edges=None, **actor_node_data)
        assert actor_vertex.data.get("name") == actor_node_data.get("name")

        movie_node_data = {"name": "Sleepless in Seattle"}

        movie_vertex = Vertex(node_type="Movie", edges=None, **movie_node_data)

        edge_data = {"year": 1996}
        actor_movie_edge = Edge(edge_type="acted_in", vertex=movie_vertex, **edge_data)

        actor_vertex.add_edge(actor_movie_edge)
        assert "acted_in" in str(actor_vertex) and "Sleepless in Seattle" in str(actor_vertex)


if __name__ == '__main__':
    test_vertex = TestVertex()
    test_vertex.test_vertex()
