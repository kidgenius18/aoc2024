#!/usr/bin/python3
import os,sys, time, datetime
sys.path.extend(['..', '.'])
script_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(script_dir)
from collections import *
from runner import main, get_commands
from utils import *
import re
import numpy as np
def get_day(): return 13
def get_year(): return 2024

def p1(v):
    t0 = time.time()
    chunks = v.split('\n\n')
    ans = 0
    ans2 = 0
    for chunk in chunks:
        lns = get_lines(chunk)
        x = []
        y = []
        for ln in lns:
            numbers = list(map(int, re.findall(r'\d+', ln)))
            x.append(numbers[0])
            y.append(numbers[1])

        denominator = (-x[0] * y[1]) + (x[1] * y[0])
        numerator = (x[2] * y[0]) - (x[0] * y[2])

        # Only proceed if the denominator is non-zero
        if denominator != 0:
            b = numerator / denominator
            # Check if b is an integer
            if b.is_integer():
                a = (y[2] - b * y[1]) / y[0]
                cost = a * 3 + b
                ans += cost

    print(f'Time: {time.time() - t0}')
    return int(ans)

def p2(v):
    t0 = time.time()
    chunks = v.split('\n\n')
    ans = 0
    for chunk in chunks:
        lns = get_lines(chunk)
        x = []
        y = []
        for ln in lns:
            numbers = list(map(int, re.findall(r'\d+', ln)))
            x.append(numbers[0])
            y.append(numbers[1])

        x[2] += 10000000000000
        y[2] += 10000000000000
        # Compute denominator and numerator
        denominator = (-x[0] * y[1]) + (x[1] * y[0])
        numerator = (x[2] * y[0]) - (x[0] * y[2])

        # Only proceed if the denominator is non-zero
        if denominator != 0:
            b = numerator / denominator
            # Check if b is an integer
            if b.is_integer():
                a = (y[2] - b * y[1]) / y[0]
                cost = a * 3 + b
                ans += cost
        
    print(f'Time: {time.time() - t0}')
    return int(ans)


if __name__ == '__main__':

    cmds = [
        #'print_stats',
        'run1',
        #'submit1',
        'run2',
        #'submit2',
        #'run_samples',
        #'samples_only'
        ]

    main(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
