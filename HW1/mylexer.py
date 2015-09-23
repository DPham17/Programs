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
	num = True
	a = 0

	#### check if this is a Hex
	if raw[len(raw)-1] is 'H' and len(raw) > 1:
		while a < len(raw)-1 and check:
			check = hexCheck(raw[a])
			a += 1
		if check:
			print "%d: Hexadecimal." % (i)
		else:
			print "%d: Invalid!" % (i)

	#### checks to see if there is a Integer
	elif raw[0] is '+' or raw[0] is '-' or raw[0].isdigit():
		if a+1 < len(raw) or raw[0].isdigit(): a += 1 # makes sure there exist something after the plus or minus
		else: check = False
		while a < len(raw) and check:
			#### check if this is a Decimal
			if raw[a] is '.':
			#{
				if a+1 < len(raw): a += 1 # makes sure there exist something after the decimal
				else: check = False
				while a < len(raw) and check:
					#### check if it is a Scientific
					if raw[a] is 'E':
						if raw[a+1] is '+' or raw[a+1] is '-' or raw[a+1].isdigit(): # checks the following E if it is a plus minus or number
							if raw[a+1].isdigit(): a += 1
							elif a+2 == len(raw):
								a = len(raw)
								check = False
							else: a += 2
							while a < len(raw) and check:
								if not raw[a].isdigit():
									a = len(raw)
									check = False
								a += 1
							if check:
								print "%d: Scientific." % (i)
								num = False
						else:
							a = len(raw)
							check = False

					elif not raw[a].isdigit():
						a = len(raw)
						check = False
					a += 1
				if check and num:
					print "%d: Decimal." % (i)
					num = False
			#}
			elif not raw[a].isdigit():
				a = len(raw)
				check = False
			a += 1

		if check and num: print "%d: Integer." % (i)
		elif not check: print "%d: Invalid!" % (i)

	# check if it is a word
	elif raw[0].isalpha():
		#### this checks if it is a Keyword in python
		if keyword.iskeyword(raw):
			print "%d: Keyword." % (i)
		else:
			#### checks if it is a Identifier
			while a < len(raw) and check:
				if raw[a].isalpha() or raw[a].isdigit() or raw[a] is '_': a += 1
				else:
					print "%d: Invalid!" % (i)
					check = False
			if check: print "%d: Identifier." % (i)

	else:
		print "%d: Invalid!" % (i)
