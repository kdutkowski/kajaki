import logging
import networkx as nx


class Solver:
    def __init__(self):
        self.logger = logging.getLogger('kajaki.solver')

    def solve(self, pairs):
        graphII = self.create_graphII_from_pairs(pairs)
        graphI = self.create_graphI_from_graphII(graphII)
        graph = self.create_graph_from_graphI(graphI)
        return self.find_best_order(graph)

    def create_graphII_from_pairs(self, pairs):
        graph = nx.Graph()
        graph.add_edges_from(pairs)
        return graph

    def create_graphI_from_graphII(self, graphII):
        graph = nx.line_graph(graphII)
        return graph

    def create_graph_from_graphI(self, graphI):
        graph = nx.complement(graphI)
        return graph

    def find_best_order(self, graph):
        order = []
        matching = nx.maximal_matching(graph)
        while len(matching) > 0:
            for turn in matching:
                order.append(turn)
                for pair in turn:
                    graph.remove_node(pair)
            matching = nx.maximal_matching(graph)

        for node in graph.nodes_iter():
            order.append((node, ()))

        return order
