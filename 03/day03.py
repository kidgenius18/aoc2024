#!/usr/bin/python3
import os,sys, time, datetime
import re
sys.path.extend(['..', '.'])
script_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(script_dir)
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 3
def get_year(): return 2024

def p1(v):
    t0 = time.time()

    chunks = v.split('\n\n')
    pattern = r"mul\((\d+),(\d+)\)"
    ans = 0
    
    matches = re.findall(pattern, chunks[0])
    for match in matches:
        ans+= int(match[0]) * int(match[1])

    print(f'Time: {time.time() - t0}')
    return ans

def p2(v):
    t0 = time.time()

    chunks = v.split('\n\n')
    pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"

    ans = 0
    do = True 

    for match in re.finditer(pattern, chunks[0]):
        if match.group(0) == "do()":
            do = True
        elif match.group(0) == "don't()":
            do = False
        elif match.group(1) and match.group(2):
            if do:
                ans += int(match.group(1)) * int(match.group(2))

    print(f'Time: {time.time() - t0}')
    return ans

if __name__ == '__main__':
    cmds = get_commands()

    cmds = [
        #'print_stats',
        'run1',
        #'submit1',
        'run2',
        #'submit2',
        #'run_samples',
        #'samples_only'
        ]
    #print('Commands:', cmds)
    main(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
