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

def check_report(levels):
    diff_matrix = [int(a) - int(b) for a, b in zip(levels, levels[1:])]
    if diff_matrix[0] != 0: #this will protect against div0 errors and is an invalid combination anyways, so we can immediately exit
        sign = diff_matrix[0] // abs(diff_matrix[0])
        result = all(item in range(sign * 1, sign * 4, sign) for item in diff_matrix)
        if result:
            return 1  # Valid combination found
    return 0

def p1(v):
    t0 = time.time()
    lns = get_lines(v)
    ans = 0

    for ln in lns:
        ans += check_report(ln.split())

    print(f'Time: {time.time() - t0}')
    return ans

def p2(v):
    t0 = time.time()
    lns = get_lines(v)
    ans = 0

    for ln in lns:
        report = ln.split()
        level_combos = [report[:i] + report[i + 1:] for i in range(len(report))]
        level_combos.insert(0, report)  # Include the original levels

        for combo in level_combos:
            result = check_report(combo)
            if result:
                ans += 1
                break

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

    print('Commands:', cmds)
    main(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
