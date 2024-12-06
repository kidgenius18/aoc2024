#!/usr/bin/python3
import os,sys, time, datetime
sys.path.extend(['..', '.'])
script_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(script_dir)
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 6
def get_year(): return 2024

def p1(v):
    t0 = time.time()
    lines = get_lines(v)
    obstructions = get_map(lines, '#')
    x, y = list(get_map(lines, '^').keys())[0]
    x_max = len(lines[0])
    y_max = len(lines)
    visited = defaultdict(int)

    dir_map = [['up',(0,-1)],['right',(1,0)],['down',(0,1)],['left',(-1,0)]]
    dir_tracker = 0
    while x in range(x_max) and y in range(y_max):
        dx, dy = dir_map[dir_tracker][1]
        if obstructions.get((x + dx, y + dy)) is not None:  #obstruction exists at our current location
            dir_tracker = (dir_tracker + 1) % len(dir_map) 
        else:
            #take a step
            x, y = x + dx, y + dy
            visited[(x,y)] += 1

    print(f'Time: {time.time() - t0}')
    return len(visited)

def p2(v):
    t0 = time.time()
    lines = get_lines(v)
    obstructions = get_map(lines, '#')
    x, y = list(get_map(lines, '^').keys())[0]
    x_max = len(lines[0])
    y_max = len(lines)
    visited = defaultdict(list)
    loops = defaultdict(int)

    dir_map = [['up',(0,-1)],['right',(1,0)],['down',(0,1)],['left',(-1,0)]]
    dir_tracker = 0
    steps_taken = 0
    while x in range(x_max) and y in range(y_max):
        dx, dy = dir_map[dir_tracker][1]
        if obstructions.get((x + dx, y + dy)) is not None:  #obstruction exists at our current location
            obstructions[(x + dx, y + dy)].append((x,y))
            dir_tracker = (dir_tracker + 1) % len(dir_map) 
        else:
            #take a step
            x, y = x + dx, y + dy
            visited[(x,y)].append((dx, dy))
            steps_taken += 1



            #what we need to do....
            #put down a obstruction in front of us, then look in the direction until we hit the next obstruction, 
            #if we've seen that obstruction before (from the same step we we are before), we would be in a loop
            #if there was now an obstruction in front of me, would placing it cause the spot to the right to increase by 1?
            sub_dir_tracker = (dir_tracker + 1) % len(dir_map)
            sub_dx, sub_dy = dir_map[sub_dir_tracker][1]
            possible_revisit = visited.get((x + sub_dx, y + sub_dy))
            if possible_revisit and (sub_dx,sub_dy) in possible_revisit: #we've been to this spot heading in the smae direction as before, so we are in a loop
                    loops[(x+dx, y+dy)] = 1



    print(f'Time: {time.time() - t0}')
    return len(visited)


if __name__ == '__main__':


    cmds = [
        #'print_stats',
        #'run1',
        #'submit1',
        'run2',
        #'submit2',
        #'run_samples',
        #'samples_only'
        ]

    main(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
