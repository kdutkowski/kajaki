from solver import Solver
import networkx as nx
import unittest


def are_eq(a, b):
    return set(a) == set(b) and len(a) == len(b)


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

    def test_should_create_GI_from_graphII(self):
        graphII = self.solver.create_graphII_from_pairs([(1, 2), (2, 3), (3, 4)])
        graphI = nx.line_graph(graphII)

        self.assertTrue(graphI.has_edge((1, 2), (2, 3)))
        self.assertTrue(graphI.has_edge((2, 3), (3, 4)))
        self.assertFalse(graphI.has_edge((4, 1), (1, 2)))
        self.assertEqual(graphI.number_of_nodes(), 3)

    def test_should_find_best_order(self):
        graph = nx.Graph()
        graph.add_edges_from([((1, 2), (2, 3)), ((2, 3), (3, 4)), ((3, 4), (4, 5))])

        compl_graph = self.solver.create_graph_from_graphI(graph)

        order = self.solver.find_best_order(compl_graph)
        a = 5


if __name__ == '__main__':
    unittest.main()
