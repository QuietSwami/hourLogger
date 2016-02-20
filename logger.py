#!/usr/bin/env python

import datetime
import time
import os
import sys
import tabulate
import optparse


def file_to_dic():
	dic = {}
	os.chdir(os.path.expanduser("~"))
	if not os.path.isfile("save.txt"):
		print "Saving file not created. Created a new one! You can now start logging those hours!"
		file = open("save.txt", "w")
		file.close()
	else:
		file = open("save.txt", "r")
		lines = file.readlines()
		lines = [x.strip().split(" ") for x in lines]
		for i in lines:
			dic[i[0]] = i[1]
	return dic 

def dic_to_file(dic):
	file = open("save.txt", "w")
	file.truncate()
	for i in dic:
		file.write(i + " " + dic[i])
	file.close()

def start(subject, dic):
	dic["started"] = subject + "@" + time.strftime("%H:%M:%M")
	return dic


def listing(dic):
	if len(dic) == 0:
		print "You haven't log any hours yet!!"
	else:
		table = []
		for i in dic:
			table.append([i, dic[i]])
		print tabulate.tabulate(table, headers=["Subject", "Hours"])
	


if __name__ == '__main__':
	dic = file_to_dic()
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
		listing(dic)
	elif options.start != None:
		string = options.start
		dic = start(options.start, dic)


