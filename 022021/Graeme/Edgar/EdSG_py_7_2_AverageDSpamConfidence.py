#!/usr/bin/env python3

filename = input('Enter the filename: ')

try:
    fhand = open(filename)
except:
    print('File cannot be opened:',filename)
    exit()

line_num = 0
line_count = 0
line_sum = 0.0

for line in fhand:
    line_num += 1

    pos = line.find('X-DSPAM-Confidence: ')

    if (pos > -1):
        try :
            num = float(line[len('X-DSPAM-Confidence: ') + pos + 1:].strip())
            line_count += 1
            line_sum += num
        except:
            print('Invalid float number in line',line_num)

if (line_count > 0):
    print('Average spam confidence:',line_sum/line_count)
else:
    print('No spam confidence headers found')

