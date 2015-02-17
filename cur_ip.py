#!/usr/bin/env python

#-----------------------------------------------------#
#
# simple script to get current IP addresss &
# machine ID. Should be placed in /usr/bin folder so
# it's accessable anywhere. 
#
# Option to drop '.py' extension.
#
# Created by: Jason Verly
# Date: 2014-12-04
# The MIT License (MIT)
# Copyright (c) 2014 Jason Verly
# See http://opensource.org/licenses/MIT for details
#-----------------------------------------------------#

import sys, socket

def main():
	try:
#		fqdn = socket.getfqdn()
		mach_ID = socket.getfqdn()
		ip_addr = socket.gethostbyname(mach_ID)
		print ''
		print 'Local IP Configuration:'
		print '------------------------------------'
		print '    IP Address: ' + ip_addr
		print '    Machine ID: ' + mach_ID
		print ''
		return 0
	except Exception:
		print 'No IP Addr'

if __name__ == '__main__':
	sys.exit(main())