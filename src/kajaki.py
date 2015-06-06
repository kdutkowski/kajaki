#!/usr/bin/env python

import getopt
import re
import sys
import logging
import coloredlogs
from solver import Solver


def main():
    opts, args = getopt.getopt(sys.argv[1:], "i", ["input"])
    logger = logging.getLogger('kajaki')
    coloredlogs.install(level=logging.DEBUG)

    input_path = args[0]
    logger.info("reading input data from %s" % (input_path))
    pairs = read_pairs_from_input(input_path)
    logger.info("read %d pairs" % len(pairs))

    solver = Solver()
    order = solver.solve(pairs)

    logger.info("Found order of length %d:\n%s", len(order), "\n".join(map(str, order)))


def read_pairs_from_input(input_path):
    pairs = []
    with open(input_path) as f:
        for line in f:
            pairs.append(parse_line_to_tuple(line))
    return pairs


def parse_line_to_tuple(line):
    mo = re.match("^(\d+) (\d+)$", line)
    if mo:
        return tuple(map(lambda x: int(x), mo.groups()))


if __name__ == "__main__":
    main()
