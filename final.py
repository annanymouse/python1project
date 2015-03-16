#!/usr/bin/env python3
'''finding word length and frequency of word length'''

import sys
import math

x = "***"
o = "   "

def cleanup(myInput):
    freq = {}
    for punc in ".,!?:;'-":
        myInput = myInput.replace(punc, "")
    words = myInput.lower().split()
    wordlen = [len(word) for word in words]
    MAXCT = int(max(wordlen))
    for i in wordlen:
        freq[i] = freq.get(i,0)+1
    print("Length Count")
    for i in sorted(freq.keys()):
        print("{0: >6} {1: >5}".format(i, freq[i]))
    return freq

def main(infile):
    freq = cleanup(infile)
    max_count = max(freq.keys())
    print(x*20)
    MAXVAL = int(math.ceil((max(freq.values()))/100))*100
    while MAXVAL > 0:
        row = [x if freq.get(i,0) > MAXVAL else o for i in range(0,max_count+1)]
        print("{0: >4} {1}".format(MAXVAL,'  '.join(row)))
        MAXVAL -= 20
    labels = ["{0: ^3} ".format(i) for i in range(0,max_count+1)]
    print("     {0}".format(' '.join(labels)))

if __name__ == '__main__':
    infile = open(sys.argv[1],'r').read()
    main(infile)
