import sys
from simulator import Simulator

def main(args=sys.argv):
	if len(args)<3:
		print "Usage: python main.py world_file.txt N(number of aliens)"
	else:
		sim = Simulator(args[1], int(args[2]))


main()