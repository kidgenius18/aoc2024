#!/usr/bin/python3
import os,sys, time, datetime
sys.path.extend(['..', '.'])
script_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(script_dir)
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 9
def get_year(): return 2024
from dataclasses import dataclass

@dataclass
class FileInfo:
    file_id: str
    block_size: int
    free_blocks: int
    remapped: bool

def p1(v):
    t0 = time.time()
    lns = get_lines(v)

    disk_map = [
    FileInfo(
        file_id=file_id,
        block_size=int(block_size),
        free_blocks=int(lns[0][file_id * 2 + 1]) if file_id * 2 + 1 < len(lns[0]) else 0
    )
    for file_id, block_size in enumerate(lns[0][::2])
    ]
    
    i = 0
    ans = 0

    # Precompute the last non-zero block_size item
    last_non_zero_block = next(
        (item for item in reversed(disk_map) if item.block_size != 0), 
        None
    )

    for item in disk_map:
        # Process block_size for the current item
        for block in range(item.block_size):
            ans += i * item.file_id
            i += 1

        # Process free_blocks for the current item
        for block in range(item.free_blocks):
            if last_non_zero_block == item:
                return ans

            ans += i * last_non_zero_block.file_id
            i += 1
            last_non_zero_block.block_size -= 1

            # Update the last_non_zero_block if its block_size becomes zero
            if last_non_zero_block.block_size == 0:
                last_non_zero_block = next(
                    (item for item in reversed(disk_map) if item.block_size != 0), 
                    None
                )
    
    print(f'Time: {time.time() - t0}')
    return ans

def p2(v):
    t0 = time.time()
    lns = get_lines(v)

    disk_map = [
    FileInfo(
        file_id=file_id,
        block_size=int(block_size),
        free_blocks=int(lns[0][file_id * 2 + 1]) if file_id * 2 + 1 < len(lns[0]) else 0,
        remapped = False
    )
    for file_id, block_size in enumerate(lns[0][::2])
    ]
    
    i = 0
    ans = 0
    new_disk_map = [disk_map[0]]

    #the below is a general approach that will move each of the items around, but needs recleaning up

    for item in reversed(disk_map):
        for free_item in disk_map:
            if item.block_size < free_item.free_blocks:
                new_disk_map.append(item)
                free_item.free_blocks -= item.block_size
                item.remapped = False
                break

    print(f'Time: {time.time() - t0}')
    return p1(v)


if __name__ == '__main__':

    cmds = [
        #'print_stats',
        #'run1',
        #'submit1',
        'run2',
        #'submit2',
        'run_samples',
        'samples_only'
        ]

    main(get_year(), get_day(), p1, p2, cmds, FILE=__file__)
