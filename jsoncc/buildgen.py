#-----------------------------------------------------------------
# jsoncc: buildgen.py
#
# jsoncc generator pickling for faster run.
# Work in progress, really just a internal development tool
#  
# Copyright (C) 2014, wvi
# License: GPLv3
#-----------------------------------------------------------------
from jsngen import JsonCCGen
import cPickle as pickle

def main():
    g = JsonCCGen()
    with open("jsonccgen", "w") as f:
        pickle.dump(g, f, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    main()
