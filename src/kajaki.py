#!/usr/bin/env python

import getopt
import sys
import logging
import coloredlogs


def main():
    opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    logger = logging.getLogger('kajaki')
    coloredlogs.install(level=logging.DEBUG)
    logger.info("kajaki run %d %d" % (5, 4))

if __name__ == "__main__":
    main()
