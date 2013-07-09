#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys,argparse

parser = argparse.ArgumentParser()
parser.add_argument('source',nargs=1,metavar='Source',help='Source File Path')
parser.add_argument('destination',nargs=1,metavar='Destination',help='Destination File')

options = parser.parse_args()

if len(sys.argv) < 2:
    print parser.print_help()
    sys.exit()

source = options.source[0]
destination = options.destination[0]
content = ''
newContent = ''

if os.path.isfile(source):
	with open(source) as f:
		content = f.readlines()
else:
	print 'Your given path has no file !'
	sys.exit()
file.closed

destination = os.path.join(os.getcwd()+'/'+destination)
file=open(destination,'w+')

for c in content:
	newContent = newContent + c.strip()

print 'Starting minimizing .... '
print '....'
file.writelines(newContent)
print 'Your minimized file is at ' + destination
file.closed
