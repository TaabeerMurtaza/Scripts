#!/usr/bin/python3

''' This script logs newtork status to /home/taabeer/logs/network/ '''

import os, time
from subprocess import DEVNULL, STDOUT, check_call, CalledProcessError
from datetime import datetime as dt

log_folder = os.path.join('/home', 'taabeer', 'logs', 'network')

def check_folders(home='/home/taabeer'):
	folder = os.path.join(home, 'logs', 'network')
	if not os.path.isdir(folder):
		os.makedirs(folder, exist_ok=True)

def get_now():
	now = dt.now()
	
	D = now.day
	M = now.month
	Y = now.year

	h = now.hour
	m = now.minute
	s = now.second

	data = {
		'D' : D,
		'M' : M,
		'Y' : Y,
		'h' : h,
		'm' : m,
		's' : s,
	}
	return data

def checknet():
	try:
		c = check_call(['/usr/bin/ping', '-c',  '1', 'google.com'], stdout=DEVNULL, stderr=DEVNULL)
	except CalledProcessError:
		return 1

	return c
	# return os.system('ping -c 1 google.com')

def log(status):
	n = get_now()
	file = os.path.join(log_folder, '{}-{}-{}'.format(n['D'], n['M'], n['Y']))
	data = 'log: {}-{}-{} _{}:{}_ \t\tSTATUS={}\n'.format(n["D"], n["M"], n["Y"], n["h"], n["m"], status)
	# print(data)
	if os.path.isfile(file):
		with open(file, 'r') as f:
			text = f.read()
			try:
				last = text.split('log: ')[-1].split('_')[1].split(':')
				minute = int(last[1])
				hour = int(last[0])
				if int(n['h']) == hour and int(n['m']) == minute:
					return 'Skipped'
			except:
				print('Error checking last record')

		difference = int(n['h']) - hour
		if difference > 0:
			data = '\n' * difference + data
	
	try:
		with open(file, 'a') as f:
			f.write(data)
			return data
	except:
		print('Error loggin file...')

def start():
	check_folders()
	while True:
		exitstatus = checknet()
		print(exitstatus)
		if exitstatus == 0: # checknet returns exit status which is 0 for success in bash
			b = log('Connected')
			if b: print(b)
			else: print('Error logging...')
		else:
			b = log('Disconnected')
			if b: print(b)
			else: print('Error logging...b ', b)

		time.sleep(10)

start()