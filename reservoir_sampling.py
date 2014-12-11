#!/usr/bin/env python

#randomly choosing a sample of k items from a list containing n items
import random
SAMPLE_COUNT = 10

# Force the value of the seed so the results are repeatable
random.seed(23456)

sample_digits = []

for index, digit in enumerate(xrange(1,2014)):
    if(index < SAMPLE_COUNT):
        sample_digits.append(digit)
    else:
        r = random.randint(0,index)
        if(r < SAMPLE_COUNT):
            sample_digits[r] = digit
print sample_digits
