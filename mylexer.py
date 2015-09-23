#!/usr/bin/env python
# Dzu Pham
# My Lexer: To test different inputs to see they belong to certin tokens

import sys
import keyword

#first number of the file to see how many test there are
num = input()

def hexCheck(raw):
	check = False
	if raw is 'A': check = True
	elif raw is 'B': check = True
	elif raw is 'C': check = True
	elif raw is 'D': check = True
	elif raw is 'E': check = True
	elif raw is 'F': check = True
	elif raw.isdigit(): check = True
	return check


for i in range(1,num+1):
	raw = raw_input()
	check = True
	a = 0

	#check if this is a Hex
	if raw[len(raw)-1] is 'H' and len(raw) > 1:
		while a < len(raw)-1 and check:
			check = hexCheck(raw[a])
			a += 1
		if check:
			print "%d: Hexadecimal." % (i)
		else:
			print "%d: Invalid!" % (i)

	# checks to see if there is a numeric
	elif raw[0] is '+' or raw[0] is '-' or raw[0].isdigit():
		while a < len(raw) and not raw[a].isalpha():
			if raw[a] is '.': # check if this is a decimal
				if a+1 < len(raw): a += 1
				else:
					print "%d: Invalid!" % (i)
					check = False
				while a < len(raw):
					if raw[a] is 'E': # check if it is a Scientific
						if raw[a+1] is '+' or raw[a+1] is '-' or raw[a+1].isdigit():
							if raw[a+1].isdigit():
								a += 1
							elif a+2 == len(raw):
								a = len(raw)
								print "%d: Invalid!" % (i)
								check = False
							else:
								a += 2
							while a < len(raw):
								if not raw[a].isdigit():
									a = len(raw)
									print "%d: Invalid!" % (i)
									check = False
								a += 1
							if check:
								print "%d: Scientific." % (i)
								check = False
						else:
							a = len(raw)
					elif not raw[a].isdigit():
						a = len(raw)
						print "%d: Invalid!" % (i)
						check = False
					a += 1
				if check:
					print "%d: Decimal." % (i)
					check = False

			a += 1
			if a == len(raw):
				print "%d: Integer." % (i)
				check = False
		if check:
			print "%d: Invalid!" % (i)

	# check if it is a word
	elif raw[0].isalpha():
		if keyword.iskeyword(raw): # this checks if it is a keyword in python
			print "%d: Keyword." % (i)
		else:
			while a < len(raw) and check:
				if not raw[a].isalpha() or not raw[a].isdigit() or not raw[a] is '_':
					check = True
					a += 1
				else:
					a = len(raw)
					print "%d: Invalid!" % (i)
					check = False
			if check: print "%d: Identifier." % (i)

	else:
		print "%d: Invalid!" % (i)
