import logging
import networkx as nx


class Solver:
    def __init__(self):
        self.logger = logging.getLogger('kajaki.solver')

    def solve(self, pairs):
        self.graphII = self.create_graphII_from_pairs(pairs)

    def create_graphII_from_pairs(self, pairs):
        graph = nx.Graph()
        graph.add_edges_from(pairs)
        return graph

