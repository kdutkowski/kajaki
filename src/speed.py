import timeit


def main():

    for n in range(2, 20):
        s = """\
import networkx as nx
from solver import Solver
solver = Solver()"""
        setup_complete = "\ngraph = nx.complete_graph(%s)""" % n
        t = timeit.timeit('solver.solve_graph(graph)', setup=s+setup_complete, number=100)
        print "%d,%f" % (n,t)


if __name__ == "__main__":
    main()
