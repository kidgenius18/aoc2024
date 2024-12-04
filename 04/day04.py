#!/usr/bin/python3
import os,sys, time, datetime
from collections import defaultdict
from itertools import product
sys.path.extend(['..', '.'])
script_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(script_dir)
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 4
def get_year(): return 2024

def p1(v):
    t0 = time.time()
    lns = get_lines(v)
    puzzle = defaultdict(int)
    ans = 0
    for j,ln in enumerate(lns):
        for i,letter in enumerate(ln):
            puzzle[(i,j)] = letter

    step_directions = list(product([0, 1, -1], repeat=2))[1:]  # All directions except (0, 0)
    word = 'XMAS'
    
    for (x, y), value in puzzle.items():
        if value == 'X':
            case_tracker = [0] * 8  # Initialize tracker for each case

            # Iterate through letters in 'word' starting from the second letter (i.e., 'M', 'A', 'S')
            for step, letter in enumerate(word[1:], start=1):  # Steps 1 through 3 (M, A, S)
                for case, (dx, dy) in enumerate(step_directions):
                    x_pos, y_pos = x + step * dx, y + step * dy

                    if puzzle.get((x_pos, y_pos)) == letter:
                        case_tracker[case] += 1

            # Count valid cases where all steps match
            ans += sum(1 for count in case_tracker if count == 3)
                
    print(f'Time: {time.time() - t0}')
    return ans

def p2(v):
    t0 = time.time()
    lns = get_lines(v)
    puzzle = defaultdict(int)
    ans = 0
    for j,ln in enumerate(lns):
        for i,letter in enumerate(ln):
            puzzle[(i,j)] = letter

    step_directions = list(product([1, -1], repeat=2))
    word = 'MAS'

    for key, value in puzzle.items():
        if value == 'A': #an 'A' will always be at the center of the X of MAS, so we can just search for these and look up/down in each direction  
            case_tracker = 0
            if puzzle.get((key[0]-1, key[1]-1)) == 'M' and puzzle.get((key[0]+1, key[1]+1)) == 'S'  :
                case_tracker += 1
            if puzzle.get((key[0]-1, key[1]+1)) == 'M' and puzzle.get((key[0]+1, key[1]-1)) == 'S'  :
                case_tracker += 1
            if puzzle.get((key[0]+1, key[1]-1)) == 'M' and puzzle.get((key[0]-1, key[1]+1)) == 'S'  :
                case_tracker += 1
            if puzzle.get((key[0]+1, key[1]+1)) == 'M' and puzzle.get((key[0]-1, key[1]-1)) == 'S'  :
                case_tracker += 1
            
            if case_tracker == 2:
                ans += 1
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
    main(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
