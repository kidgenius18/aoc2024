#!/usr/bin/python3
import os,sys, time, datetime
sys.path.extend(['..', '.'])
script_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(script_dir)
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 10
def get_year(): return 2024

import heapq

def build_tree_for_dijkstra(grid):
    """
    Builds a graph compatible with Dijkstra's algorithm from a grid of integers.
    A valid connection exists if the difference between one cell and its neighbor is an increase of exactly 1.

    :param grid: A list of lists, where each inner list represents a row of integers.
    :return: A dictionary representing the graph as an adjacency list for Dijkstra's algorithm.
    """
    rows, cols = len(grid), len(grid[0])
    graph = {}

    # Helper function to get valid neighbors
    def get_neighbors(x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == grid[x][y] + 1:
                neighbors.append((nx, ny))  # Neighbor position
        return neighbors

    # Build the adjacency list
    for x in range(rows):
        for y in range(cols):
            graph[(x, y)] = get_neighbors(x, y)
    
    return graph

def dijkstra(graph, start, end):
    """
    Dijkstra's algorithm to find the shortest path in a weighted graph.

    :param graph: A dictionary where keys are nodes and values are lists of (neighbor, cost).
    :param start: The starting node (x, y).
    :param end: The ending node (x, y).
    :return: The shortest path as a list of nodes and the total cost.
    """
    pq = [(0, start)]  # Priority queue of (cost, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node == end:
            break

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph[current_node]:
            distance = current_distance + 1  # Cost of each step is 1
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    # Reconstruct the path
    path = []
    current = end
    while current:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()

    return path, distances[end]    

def find_start_and_end(grid, start_value=0, end_value=9):
    """
    Finds the start and end positions in the grid based on the given values.

    :param grid: A list of lists representing the grid.
    :param start_value: The value to identify the starting node.
    :param end_value: The value to identify the ending node.
    :return: A tuple (start, end) representing the positions of the start and end nodes.
    """
    start, end = [], []
    for x, row in enumerate(grid):
        for y, value in enumerate(row):
            if value == start_value:
                start.append((x, y))
            if value == end_value:
                end.append((x, y))
    return start, end

def find_all_paths(grid, start, end):
    """
    Finds all paths from start to end in the grid where valid moves follow the constraint
    that the value in the neighbor is exactly 1 greater than the current node's value.

    :param grid: A 2D list representing the grid of numbers.
    :param start: The starting node as a tuple (x, y).
    :param end: The ending node as a tuple (x, y).
    :return: A list of all valid paths, each path being a list of nodes.
    """
    rows, cols = len(grid), len(grid[0])
    all_paths = []

    def dfs(path, current):
        if current == end:
            all_paths.append(path[:])  # Add a copy of the current path
            return

        x, y = current
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == grid[x][y] + 1:
                path.append((nx, ny))
                dfs(path, (nx, ny))
                path.pop()  # Backtrack

    # Start DFS from the start node
    dfs([start], start)

    return all_paths

def p1(v):
    t0 = time.time()
    lns = get_lines(v)
    
    grid = [[int(col) for col in row] for row in lns]
    starting_nodes, ending_nodes = find_start_and_end(grid)

    graph = build_tree_for_dijkstra(grid)
    
    total_paths = 0
    for start in starting_nodes:
        for end in ending_nodes:
            path, cost = dijkstra(graph, start, end)
            if path[0] != end:
                total_paths += 1
       
    print(f'Time: {time.time() - t0}')
    return total_paths

def p2(v):
    t0 = time.time()
    lns = get_lines(v)
    
    grid = [[int(col) for col in row] for row in lns]
    starting_nodes, ending_nodes = find_start_and_end(grid)

    total_paths = 0
    for start in starting_nodes:
        for end in ending_nodes:
            paths = find_all_paths(grid, start, end)
            total_paths += len(paths)

    print(f'Time: {time.time() - t0}')
    return total_paths


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
