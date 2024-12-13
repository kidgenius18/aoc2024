#!/usr/bin/python3
import os,sys, time, datetime
sys.path.extend(['..', '.'])
script_dir = os.path.dirname(os.path.abspath(__file__))

os.chdir(script_dir)
from collections import *
from runner import main, get_commands
from utils import *
def get_day(): return 12
def get_year(): return 2024

def dfs_grid(grid):
    rows, cols = len(grid), len(grid[0])
    all_positions = {(x, y) for x in range(rows) for y in range(cols)}
    visited = set()
    clusters = {}  # Maps cluster ID to list of nodes
    node_to_cluster = {}  # Maps each node to its cluster ID
    cluster_id = 0  # Unique ID for each cluster
    touch_counts = {}

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    def dfs(x, y, start_value, cluster):
        # If the node is out of bounds or already visited, return
        if (x < 0 or x >= rows or y < 0 or y >= cols or 
                (x, y) in visited or grid[x][y] != start_value):
            return
        
        # Mark the current node as visited
        visited.add((x, y))
        clusters[cluster_id].append((x, y))
        node_to_cluster[(x, y)] = cluster_id
        touch_count = 0

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == start_value:
                touch_count += 1
                dfs(nx, ny, start_value, cluster)

        touch_counts[(x, y)] = touch_count


    # Process all positions
    while all_positions:
        start = next(iter(all_positions))  # Get an arbitrary starting point
        start_value = grid[start[0]][start[1]]
        clusters[cluster_id] = []
        dfs(start[0], start[1], start_value, cluster_id)
        
        all_positions -= visited
        cluster_id += 1

    return clusters, touch_counts

from collections import deque

def find_edges(grid, nodes):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right
    edges = set()
    boundary_nodes = set()

    # Identify boundary nodes
    for node in nodes:
        x, y = node
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)
            if neighbor not in nodes:  # Edge exists if neighbor is outside the area
                boundary_nodes.add(node)
                break
    
    # Group boundary nodes
    def get_neighbors(node):
        x, y = node
        neighbors = []
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)
            if neighbor in boundary_nodes:
                neighbors.append(neighbor)
        return neighbors

    visited = set()
    boundary_groups = []

    for node in boundary_nodes:
        if node not in visited:
            # BFS to find all connected nodes in this boundary group
            queue = deque([node])
            group = set()

            while queue:
                current = queue.popleft()
                if current not in visited:
                    visited.add(current)
                    group.add(current)
                    queue.extend(get_neighbors(current))

            boundary_groups.append(group)

    for group in boundary_groups:
        sorted_group = sorted(group)  # Optional: Sort nodes logically for structured edges
        for i, node in enumerate(sorted_group):
            for j in range(i + 1, len(sorted_group)):  # Check all pairs
                neighbor = sorted_group[j]
                edges.add(tuple(sorted((node, neighbor))))  # Add unique edges

    return edges


def p1(v):
    t0 = time.time()
    lns = get_lines(v)
    chunks = v.split('\n\n')
    ans = 0

    grid = [[col for col in row] for row in lns]

    clusters, touch_counts = dfs_grid(grid)

    for _, cluster in clusters.items():
        row, col = cluster[0]
        perimeter = 0
        for node in cluster:
            perimeter += (4 - touch_counts[node])
        print(f'{grid[row][col]}: {len(cluster)}, {perimeter}')

        ans += (perimeter * len(cluster))
    
    print(f'Time: {time.time() - t0}')
    return ans

def p2(v):
    t0 = time.time()
    lns = get_lines(v)
    chunks = v.split('\n\n')
    ans = 0

    grid = [[col for col in row] for row in lns]

    clusters, touch_counts = dfs_grid(grid)

    for id, cluster in clusters.items():
        row, col = cluster[0]
        boundary_nodes = []
        for node in cluster:
            if touch_counts[node] < 4:
                boundary_nodes.append(node)

        edges = find_edges(grid, cluster)

        print(f'{grid[row][col]}: {len(cluster)}, {edges}')

        ans += (edges * len(cluster))
    
    print(f'Time: {time.time() - t0}')
    return ans


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
