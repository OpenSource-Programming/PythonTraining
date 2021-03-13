#!/usr/bin/env python3

# str = 'X-DSPAM-Confidence: 0.8475'
str = input("Test input: ")

sppos = str.find(':')

num = None

if (sppos < 0) :
    print('Invalid input')
else :
    try :
        num = float(str[sppos + 1:])
    except:
        print('Invalid float number')

if (num is not None) :
    print(num)

