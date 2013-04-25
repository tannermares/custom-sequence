#!/home/tmares/bin/python
#!/usr/bin/python

import argparse
import sys
import string
import signal

signal.signal( signal.SIGPIPE, signal.SIG_DFL )

base = '/work/scripts/'

def list(s):
	try:
		return s.split(',')
	except:
		raise argparse.ArgumentTypeError("Must be a comma separated list of characters")
	
def replace( index, oldValue, newValue ):
	valueList = []
	for i in oldValue:
		valueList.append(i)
	valueList[index] = newValue
	s = "".join(valueList)
	return s

def toList( string ):
	list = []
	for i in string:
		list.append(i)
	return list

def parseArgs():
	parser = argparse.ArgumentParser(description='Print a sequence of numbers with a custom range.', add_help=False, formatter_class=argparse.RawTextHelpFormatter)

	info = parser.add_argument_group('Program Info')
	info.add_argument('-h', '--help', action='help', help='show this help message and exit')
	info.add_argument('-v', '--version', action='version', version='1.0.0')

	required = parser.add_argument_group('Required arguments')

	optional = parser.add_argument_group('Optional arguments')
	optional.add_argument('first', nargs='?', default=False, help='first number in sequence')
	optional.add_argument('last', nargs='?', default=False, help='last number in sequence')
	optional.add_argument('-r', '--range', metavar='LIST', type=list, default='0,1,2,3,4,5,6,7,8,9', help='comma separated list you wish to sequence.')
	optional.add_argument('-s', '--separator', metavar='STRING', default='\n', help='use STRING to separate numbers (default:\\n)')
	
	a = parser.parse_args()
	print ("first "+ a.first)
	print ("last "+ a.last)
	print ("range ")
	print  (a.range)
	if not a.first == False and not a.last == False:
		pass
	elif a.last == False and not a.first == False:
		a.last = a.first
		a.first = a.range[0]
		for x in range(0,len(a.last)-1):
			a.first += a.range[0]
	else:
		a.first = a.range[0]
		a.last = a.range[len(a.range)-1] + a.range[len(a.range)-1] + a.range[len(a.range)-1] + a.range[len(a.range)-1]
		for x in range(0,len(a.last)-1):
			a.first += a.range[0]
	return a

def iterate( args ):
	iterations = []
	while not args.first == args.last:
		iterations.append(args.first)
		for i in reversed(range(0,len(args.last))):
			charAt = toList(args.first)[i]
			x = args.range.index(charAt)
			x += 1
			x = x % len(args.range)
			args.first = replace(i,args.first,args.range[x])
			if not (x == 0):
				break
	iterations.append(args.last)
	print (args.separator.join(iterations))
if __name__ == "__main__":
	args = parseArgs()
	iterate(args)
