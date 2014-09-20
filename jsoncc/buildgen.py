from jsngen import JsonCCGen
import cPickle as pickle

def main():
    g = JsonCCGen()
    with open("jsonccgen", "w") as f:
        pickle.dump(g, f, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    main()
