#!/usr/bin/python3
import os,sys, time, datetime
sys.path.extend(['..', '.'])
script_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(script_dir)
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 11
def get_year(): return 2024





def p1(v):
    t0 = time.time()
    lns = get_lines(v)

    blinks = 25
    stones = [int(num) for num in lns[0].split()]

    #following changes would be needed to make this something that can be run efficiently:
    #   any even number of digits will break down over X steps into single numbers and we will have 9 repeatable patterns
    #   for what will happen, so we should pre-program/hash-map how a 1-9 will multiple up and break all the way back down into single digits, along
    #   with the number of steps to reach each arrangement.  For example:
    #       step 0:   1
    #       step 1:   2024
    #       step 2:   20 24
    #       step 3:   2 0 2 4
    #      
    #   at this point, we are back to all single digits, and could then use the rules on 2's, 0's, and 4's, and how those will play out.
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                stone = 1  # Replace 0 with 1
                new_stones.append(stone)
                continue

            stone_digits = len(str(stone))

            if stone_digits % 2 == 0:  # Even number of digits
                # Split into two halves
                mid = stone_digits // 2
                left = int(str(stone)[:mid])
                right = int(str(stone)[mid:])
                new_stones.append(left)
                new_stones.append(right)
            else:  # Odd number of digits
                new_stones.append(stone * 2024)

        stones = new_stones  # Update stones for the next iteration

    print(f'Time: {time.time() - t0}')
    return len(stones)

def p2(v):
    t0 = time.time()

    #solving pt2 is identical to pt1, just run 75 times instead of 25.
    print(f'Time: {time.time() - t0}')
    return p1(v)


if __name__ == '__main__':
    
    cmds = [
        #'print_stats',
        'run1',
        #'submit1',
        #'run2',
        #'submit2',
        #'run_samples',
        #'samples_only'
        ]

    main(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
