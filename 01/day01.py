#!/usr/bin/python3
import os,sys, time, datetime
from collections import Counter, defaultdict
sys.path.extend(['..', '.'])
script_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(script_dir)
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 1
def get_year(): return 2024


def create_lists(lns):
    lns1, lns2 = [],[]
    for ln in lns:
        col1, col2 = map(int, ln.split())
        lns1.append(col1)
        lns2.append(col2)
    lns1.sort()
    lns2.sort()
    return lns1, lns2

def p1(v):
    t0 = time.time()
    lns = get_lines(v)
    lns1, lns2 = create_lists(lns)

    ans = sum(abs(a - b) for a, b in zip(lns1, lns2))

    return ans

def p2(v):
    t0 = time.time()
    lns = get_lines(v)

    lns1, lns2 = create_lists(lns)
    
    first_col = defaultdict(int,Counter(lns1))
    second_col = defaultdict(int,Counter(lns2))

    ans = sum((value * key * second_col[key]) for key,value in first_col.items())

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
