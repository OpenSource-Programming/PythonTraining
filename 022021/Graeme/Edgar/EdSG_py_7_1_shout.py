#!/usr/bin/env python3

filename = input('Enter the filename: ')

try:
    fhand = open(filename)
except:
    print('File cannot be opened:',filename)
    exit()

for line in fhand:
    print(line.rstrip().upper())

