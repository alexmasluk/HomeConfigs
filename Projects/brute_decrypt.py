#!/usr/bin/python3
import sys
import string

alphabet = string.ascii_lowercase

if not len(sys.argv) == 2:
	exit(1)

ctxt = sys.argv[1]

def rot( n, c ):
        if (int(n) >= 0):
                return alphabet[ (ord(c) - ord('a') + int(n)) % 26 ]
        else:
                newval = ord(c) - ord('a') + int(n)
                if (newval < 0):
                        newval += 26
                return alphabet[newval]
ptxts = []
for x in range(1,26):
	ptxt = ""
	for letter in ctxt:
		if letter in alphabet:
			ptxt += rot(x, letter)
		else:
			ptxt += letter
	ptxts.append(ptxt)
with open('ptexts.txt', 'w') as f:
	for txt in ptxts:
		print(txt, file = f, end = '\n')

