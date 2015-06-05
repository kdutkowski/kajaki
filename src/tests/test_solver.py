from solver import Solver
import networkx as nx
import unittest


class SolverTest(unittest.TestCase):
    def setUp(self):
        self.solver = Solver()

    def test_should_create_GII_from_edges_list(self):
        edges_expected = [(1, 3), (2, 3), (4, 5)]
        graph = self.solver.create_graphII_from_pairs(edges_expected)

        edges_actual = graph.edges()

        self.assertTrue(are_eq(edges_actual, edges_expected))
        self.assertFalse(graph.is_directed())
        self.assertEqual(graph.number_of_nodes(), 5)
        self.assertFalse(graph.is_multigraph())


def are_eq(a, b):
    return set(a) == set(b) and len(a) == len(b)


if __name__ == '__main__':
    unittest.main()
