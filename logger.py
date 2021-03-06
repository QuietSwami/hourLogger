#!/usr/bin/env python

import datetime
import time
import os
import sys
import tabulate
import optparse


def help():
	print "Log hours to a subject. To write a subject use only a word, of several words seprated by a underscore..."

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
		file.write(i + " " + dic[i] + "\n")
	file.close()

def start(subject, dic):
	if subject not in dic:
		dic[subject] = datetime.time(0,0,0).strftime("%H:%M:%S")
	dic["started"] = subject + "@" + time.strftime("%H:%M:%M")
	return dic


def listing(dic):
	if len(dic) == 0:
		print "You haven't log any hours yet!!"
	else:
		table = []
		for i in dic:
			if i != "started":
				table.append((i, dic[i]))
			if "started" in dic:
				table.append(("started", dic["started"]))
		table = sorted(table, lambda p: p[1], reverse=True)
		print tabulate.tabulate(table, headers=["Subject", "Hours"])
	

def stop(subject, dic):
	if "started" not in dic:
		print "You can't stop what you din't start!"
		return dic
	else:
		sub = dic["started"].split("@")
		if subject != sub[0]:
			print "You din't start that subject! You started ", sub[0]
			return dic
		else:
			print dic
			sub_time = dic[subject].split(":")
			sub_time = [int(x) for x in sub_time]
			now = time.strftime("%H:%M:%S").split(":")
			begin = sub[1].split(":")
			hours = int(now[0]) - int(begin[0])
			minutes = int(now[1]) - int(begin[1])
			seconds = int(now[2]) - int(begin[2])
			if seconds >= 60:
				print "yolo"
				minutes += 1
				seconds = seconds - 60
			elif minutes >= 60:
				hours += 1
				minutes = minutes - 60
			sub_time = [sub_time[0] + hours, sub_time[1] + minutes, sub_time[2] + seconds]
			sub_time = str(sub_time[0]).zfill(2) +":"+ str(sub_time[1]).zfill(2) + ":" + str(sub_time[2]).zfill(2)
			dic[subject] = sub_time
			del dic["started"]
			return dic


def remove(subject, dic):
	if subject not in dic:
		print "Unable to remove " + subject + ", "+ subeject + " does not exist!"
	else:
		print "Removed " + subject + "..."
		del dic[subject]
		return dic


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

	if len(args) > 1: #We only want one subject to be running at the time, so we limit the number of arguments the program can take
		print "Invalid number of arguments. Only one is allowed"
		sys.exit()
	elif options.list and len(args) > 0:
		print "Invalida number of arguments. With --list no argument is permited."
	elif options.list:
		listing(dic)
	elif options.start != None:
		string = options.start
		dic = start(string, dic)
		dic_to_file(dic)
	elif options.stop != None:
		string = options.stop
		dic = stop(string, dic)
		dic_to_file(dic)



