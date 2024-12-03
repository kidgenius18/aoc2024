#!/usr/bin/python3
import os,sys, time, datetime
sys.path.extend(['..', '.'])
script_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(script_dir)
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 23
def get_year(): return 2024

def p1(v):
    t0 = time.time()
    lns = get_lines(v)
    chunks = v.split('\n\n')
    ans = 0
    for ln in lns:
        ans += 1
    
    print(f'Time: {time.time() - t0}')
    return ans

def p2(v):
    t0 = time.time()

    print(f'Time: {time.time() - t0}')
    return p1(v)


if __name__ == '__main__':
    cmds = get_commands()
    """
    cmds = [
        #'print_stats',
        'run1',
        #'submit1',
        #'run2',
        #'submit2',
        #'run_samples',
        #'samples_only'
        ]
    """
    print('Commands:', cmds)
    main(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
