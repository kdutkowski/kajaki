#!/usr/bin/env python

import getopt
import re
import sys
import logging
import coloredlogs
import time
import networkx as nx
import numpy as np

from solver import Solver

def main():
    logger = logging.getLogger('kajaki')
    coloredlogs.install(level=logging.DEBUG)

    reps = 20

    solver = Solver()
    sizes = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    densities = [0.25, 0.50, 0.75, 1.0, 1.25, 1.5]
    times = [[0]*len(densities) for i in range(len(sizes))]

    for densityIdx, density in enumerate(densities):
        for sizeIdx, size in enumerate(sizes):
            avgTime = 0
            for i in range(reps):
                graph = nx.dense_gnm_random_graph(size, int(size*density))
                start = time.time()
                solver.solveFromGraphII(graph)
                end = time.time()
                t = end - start
                avgTime = avgTime + t
            times[sizeIdx][densityIdx] = avgTime/reps

    npTimes = np.array(times)

    # np.apply_along_axis(np.linalg.norm, 0, npTimes)
    timesNormalized = npTimes / npTimes.max(axis=0)

    print timesNormalized

    np.savetxt("results/results.csv", timesNormalized, delimiter=",")

if __name__ == "__main__":
    main()
