#!/usr/bin/python3
import os,sys, time, datetime
sys.path.extend(['..', '.'])
script_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(script_dir)
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 2
def get_year(): return 2024

def check_level(levels):
    total_levels = len(levels)

    numr = int(levels[0]) - int(levels[1])
    denom = abs(numr)
    if denom == 0:
        return 0
    sign_bit = int(numr/denom)

    i = 1
    while i < total_levels:
        prev_level = int(levels[i-1])
        level = int(levels[i])
        diff = prev_level - level
        if diff not in range(sign_bit * 1, sign_bit * 4, sign_bit):
            return 0
        
        i+=1
    
    return 1
         
def check_level_2(levels, recr):
    if recr > 1:
        return 0
    
    total_levels = len(levels)
    numr = int(levels[0]) - int(levels[1])
    denom = abs(numr)
    if denom == 0:
        new_levels = levels[1:].copy()
        safe = check_level_2(new_levels, recr + 1)
        if safe == 0:
            return 0
        else:
            return 1
    sign_bit = int(numr/denom)

    i = 1
    while i < total_levels:
        prev_level = int(levels[i-1])
        level = int(levels[i])
        diff = prev_level - level
        if diff not in range(sign_bit * 1, sign_bit * 4, sign_bit):
            new_levels = levels[:].copy()
            new_levels.pop(i)
            safe = check_level_2(new_levels, recr + 1)
            if safe == 0:
                if recr == 0:
                    new_levels = levels[:].copy()
                    new_levels.pop(0)
                    safe = check_level_2(new_levels, recr + 1)
                    if safe == 0:
                        return 0
                    else:
                        return 1
                return 0
            else:
                return 1
        i+=1
    
    return 1

def p1(v):
    lns = get_lines(v)

    ans = 0
    for ln in lns:
        ans += check_level(ln.split())
    return ans

def p2(v):
    lns = get_lines(v)

    ans = 0
    for ln in lns:
        ans += check_level_2(ln.split(),0)
    return ans


if __name__ == '__main__':
    cmds = get_commands()
    
    cmds = [
        #'print_stats',
        #'run1',
        #'submit1',
        'run2',
        #'submit2',
        #'run_samples',
        #'samples_only'
        ]

    print('Commands:', cmds)
    main(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
