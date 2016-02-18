#!/usr/bin/env python

import datetime
import os
import sys
import tabulate
import optparse



if __name__ == '__main__':
	group = optparse.OptionParser(description='Process some integers.')
	group.add_option('-s', '--start', action="store", nargs=1, help='Start the logger')
	group.add_option('-p', '--stop', action="store", nargs=1, help='Stop the logger')
	group.add_option('-l', '--list', action="store_true", help='List all the subjects you are working in, with the hours worked')
	group.add_option('-r', '--remove', action="store", nargs=1, help='Removes the subject')
	(options, args) = group.parse_args()
	if options.start and options.stop:
		group.error("Options -s and -p are exclusive")
	elif options.remove and options.start or options.remove and options.stop or options.remove and options.list:
		group.error("Option -r is used alone, with the name of the subject")
	elif options.list and options.start or options.list and options.stop or options.list and options.remove:
		group.error("Option -l is used aloneoptions	print args")

	#print (options, args) #this tuple has a object options, and a list arguments.

	if len(args) > 1: #We only want one subject to be running at the time, so we limit the number of arguments the program can take
		print "Invalid number of arguments. Only one is allowed"
		sys.exit()

	