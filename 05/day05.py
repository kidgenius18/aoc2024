#!/usr/bin/python3
import os,sys, time, datetime
sys.path.extend(['..', '.'])
script_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(script_dir)
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 5
def get_year(): return 2024

def p1(v):
    t0 = time.time()
    chunks = v.split('\n\n')
    page_orders = get_lines(chunks[0])
    print_runs = [print_run.split(',') for print_run in get_lines(chunks[1])]

    pages = defaultdict(list)
    for page_order in page_orders:
        pg1, pg2 = page_order.split('|')
        pages[pg1].append(pg2)

    good_runs = []
    ans = 0
    for print_run in print_runs:
        bad_run = False
        for idx, page in enumerate(print_run):
            previous_pages = set(print_run[:idx])
            if any(linked_page in previous_pages for linked_page in pages[page]):
                bad_run = True
                break
        if not bad_run:
            good_runs.append(print_run)
            middle_index = len(print_run) // 2
            ans += int(print_run[middle_index])
                
    
    print(f'Time: {time.time() - t0}')
    return ans

def re_order(print_order, pages, bad_page):
    for idx, pg in enumerate(print_order):
        if pg in pages[bad_page]: #found the left-most position of where the item belongs
            print_order.remove(bad_page)
            print_order.insert(idx,bad_page)
            break
    return



def p2(v):
    t0 = time.time()
    chunks = v.split('\n\n')
    page_orders = get_lines(chunks[0])
    print_runs = [print_run.split(',') for print_run in get_lines(chunks[1])]

    pages = defaultdict(list)
    for page_order in page_orders:
        pg1, pg2 = page_order.split('|')
        pages[pg1].append(pg2)

    
    bad_runs = []
    ans = 0
    for print_run in print_runs:
        bad_run = False
        for idx, page in enumerate(print_run):
            previous_pages = set(print_run[:idx])
            if any(linked_page in previous_pages for linked_page in pages[page]):
                bad_run = True
                re_order(print_run, pages, page)
        if bad_run:
            bad_runs.append(print_run)
            middle_index = len(print_run) // 2
            ans += int(print_run[middle_index])
                
    
    print(f'Time: {time.time() - t0}')
    return ans


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
