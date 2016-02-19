#!/usr/bin/env python

import datetime
import os
import sys
import tabulate
import optparse


def start(subject):
	os.chdir(os.path.expanduser('~'))
	file = open("save.txt", "w")
	for i in file.readlines():
		i = i.split(" ")
		if subject in i:
			


def listing():
	filename = "save.txt"
	base = os.path.expanduser('~')
	file_path = base + "/" + filename
	print file_path
	if not os.path.exists(file_path):
		os.chdir(base)
		file = open(filename, 'w')
		file.close()
	else:
		os.chdir(base)
		file = open(filename, 'r')
		lines = file.readlines()
		listing = [[x.strip().split(" ")] for x in lines]
		print tabulate.tabulate(listing)
	

if __name__ == '__main__':
	listing()

	# group = optparse.OptionParser(description='Process some integers.')
	# group.add_option('-s', '--start', action="store", nargs=1, help='Start the logger')
	# group.add_option('-p', '--stop', action="store", nargs=1, help='Stop the logger')
	# group.add_option('-l', '--list', action="store_true", help='List all the subjects you are working in, with the hours worked')
	# group.add_option('-r', '--remove', action="store", nargs=1, help='Removes the subject')
	# (options, args) = group.parse_args()
	# if options.start and options.stop: #you cant start and stop at the same time...
	# 	group.error("Options -s and -p are exclusive")
	# elif options.remove and options.start or options.remove and options.stop or options.remove and options.list:
	# 	group.error("Option -r is used alone, with the name of the subject")
	# elif options.list and options.start or options.list and options.stop or options.list and options.remove:
	# 	group.error("Option -l is used aloneoptions	print args")

	# #print (options, args) #this tuple has a object options, and a list arguments.

	# if len(args) > 1: #We only want one subject to be running at the time, so we limit the number of arguments the program can take
	# 	print "Invalid number of arguments. Only one is allowed"
	# 	sys.exit()
	# elif options.list and len(args) > 0:
	# 	print "Invalida number of arguments. With --list no argument is permited."
	# elif options.list:
	# 	listing()


