#!/usr/bin/env python

import datetime
import time
import os
import sys
import tabulate
import optparse


def start(subject):
	empty = datetime.time(0,0,0)
	os.chdir(os.path.expanduser('~'))
	if not os.path.isfile("save.txt"): #create a new file if it doesn't exist
		print "Saving file did not exist... Created one. You can now start logging those hours!"
		file = open("save.txt", "w")
		file.write(subject + " " + empty.strftime("%H:%M:%S") + "\n") #create a new subject
		file.write("started " + subject + "@" + time.strftime("%H:%M:%S") +"\n") # start the log
		file.close()
	else:
		file = open("save.txt", "r")
		lista = file.readlines()
		file.close() 
		file = open("save.txt", "w")
		lista = [x.strip().split(" ") for x in lista]
		occ = False #occ checks if the subject already exists
		for i in lista:
			print i
			if subject in i: #if the subject exists
				num_of_oc = True
			elif "started" in  i:
				if not occ:
					file.write(subject + " " + empty.strftime("%H:%M:%S") + "\n") #if the subject doesn't exist creates it
				file.write("started " + str(subject) + "@" + time.strftime("%H:%M:%S") + "\n")
			file.write(i[0] + " " +i[1]) # re-writes the subjects
		file.close()

def listing():
	filename = "save.txt"
	base = os.path.expanduser('~')
	file_path = base + "/" + filename
	print file_path
	if not os.path.exists(file_path):
		os.chdir(base)
		print "Saving file did not exist... Created one. You can now start logging those hours!"
		file = open(filename, 'w')
		file.close()
	else:
		os.chdir(base)
		file = open(filename, 'r')
		lines = file.readlines()
		listing = [[x.strip().split(" ")] for x in lines]
		print tabulate.tabulate(listing)
	

if __name__ == '__main__':

	group = optparse.OptionParser(description='Process some integers.')
	group.add_option('-s', '--start', action="store", nargs=1, help='Start the logger')
	group.add_option('-p', '--stop', action="store", nargs=1, help='Stop the logger')
	group.add_option('-l', '--list', action="store_true", help='List all the subjects you are working in, with the hours worked')
	group.add_option('-r', '--remove', action="store", nargs=1, help='Removes the subject')
	(options, args) = group.parse_args()
	if options.start and options.stop: #you cant start and stop at the same time...
		group.error("Options -s and -p are exclusive")
	elif options.remove and options.start or options.remove and options.stop or options.remove and options.list:
		group.error("Option -r is used alone, with the name of the subject")
	elif options.list and options.start or options.list and options.stop or options.list and options.remove:
		group.error("Option -l is used aloneoptions	print args")

	print (options, args) #this tuple has a object options, and a list arguments.

	if len(args) > 1: #We only want one subject to be running at the time, so we limit the number of arguments the program can take
		print "Invalid number of arguments. Only one is allowed"
		sys.exit()
	elif options.list and len(args) > 0:
		print "Invalida number of arguments. With --list no argument is permited."
	elif options.list:
		listing()
	elif options.start != None:
		string = options.start
		start(string)


