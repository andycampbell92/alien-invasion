import sys
from simulator import Simulator

def main(args=sys.argv):
	sim = Simulator(args[1], int(args[2]))


main()