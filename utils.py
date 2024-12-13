import re
from collections import *
# String parsing

def exact_match(pattern, s):
    return re.match('^' + pattern + '$', s) != None

def get_chunks(v):
    return [ch.split('\n') for ch in v.split('\n\n')]

def get_ints(v):
    return [int(x) for x in v.split()]

def get_lines(data):
    return data.strip('\n').split('\n')

def multi_split(s, schars):
    out = []
    curr = ''
    for c in s:
        if c in schars:
            if curr:
                out.append(curr)
                curr = ''
        else:
            curr += c
    if curr: out.append(curr)
    return out

def get_map(data, symbol):
    #takes data that is in 'lines'
    symbol_dict = defaultdict(list)
    for j, chars in enumerate(data):
        for i, char in enumerate(chars):
            if char == symbol:
                symbol_dict[(i,j)] = []
    return symbol_dict


def lazy_ints(arr):
    out = []
    for v in arr:
        if is_int(v):
            out.append(int(v))
        else:
            out.append(v)
    return out

# VM
class VM:
    def __init__(self, reg, prog, instr_fn):
        self.reg = reg
        self.prog = prog
        self.instr_fn = instr_fn

        self.i = 0
        self.seen = set()
        self.running = True

    def err(self, tag, *strs):
        print('[VM: {}]'.format(tag), *strs)

    def still_running(self):
        i = self.i
        if i >= len(self.prog):
            self.running = False
        if i < 0:
            self.err('state', 'i < 0: {}'.format(i))
            self.running = False
        return self.running

    def step(self):
        if not self.running:
            self.err('step', 'calling step after termination')
            return
        if not self.still_running():
            return
        i = self.i
        instr = self.prog[i]
        self.i += self.instr_fn(self, instr)
        self.seen.add(i)

    def exec(self):
        while self.running:
            self.step()



# Grids
def grid4n(r, c):
    return [(r-1, c), (r, c-1), (r, c+1), (r+1, c)]
def grid8n(r, c):
    o = []
    for rr in range(r-1, r+2):
        for cc in range(c-1, c+2):
            if (rr, cc) != (r, c):
                o.append((rr, cc))
    return o

def filter_coords(coords, R, C):
    out = []
    for r, c in coords:
        if r < 0 or r >= R:
            continue
        if c < 0 or c >= C:
            continue
        out.append((r, c))
    return out

def grid4nf(r, c, R, C):
    return filter_coords(grid4n(r, c), R, C)
def grid8nf(r, c, R, C):
    return filter_coords(grid8n(r, c), R, C)

def is_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def print_stats(v):
    lines = get_lines(v)
    print('INPUT[:10]:')
    for line in lines[:10]:
        print('> ' + line)
    if len(lines) > 10:
        print('...')
    tot_tokens = 0
    int_tokens = 0
    for line in lines:
        for tok in line.split():
            tot_tokens += 1
            if is_int(tok):
                int_tokens += 1
    print('lines: {}, tokens: {}, int_tokens: {}'.format(
        len(lines), tot_tokens, int_tokens))


# Python3 implementation to find the
# shortest path in a directed
# graph from source vertex to
# the destination vertex
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
infi = 1000000000;
   
# Class of the node
class Node:
   
    # Adjacency list that shows the
    # vertexNumber of child vertex
    # and the weight of the edge   
    def __init__(self, vertexNumber):       
        self.vertexNumber = vertexNumber
        self.children = []
   
    # Function to add the child for
    # the given node
    def Add_child(self, vNumber, length):   
        p = Pair(vNumber, length);
        self.children.append(p);
       
# Function to find the distance of
# the node from the given source
# vertex to the destination vertex
def dijkstraDist(g, s, path):
       
    # Stores distance of each
    # vertex from source vertex
    dist = [infi for i in range(len(g))]
   
    # bool array that shows
    # whether the vertex 'i'
    # is visited or not
    visited = [False for i in range(len(g))]
     
    for i in range(len(g)):       
        path[i] = -1
    dist[s] = 0;
    path[s] = -1;
    current = s;
   
    # Set of vertices that has
    # a parent (one or more)
    # marked as visited
    sett = set()    
    while (True):
           
        # Mark current as visited
        visited[current] = True;
        for i in range(len(g[current].children)): 
            v = g[current].children[i].first;           
            if (visited[v]):
                continue;
   
            # Inserting into the
            # visited vertex
            sett.add(v);
            alt = dist[current] + g[current].children[i].second;
   
            # Condition to check the distance
            # is correct and update it
            # if it is minimum from the previous
            # computed distance
            if (alt < dist[v]):      
                dist[v] = alt;
                path[v] = current;       
        if current in sett:           
            sett.remove(current);       
        if (len(sett) == 0):
            break;
   
        # The new current
        minDist = infi;
        index = 0;
   
        # Loop to update the distance
        # of the vertices of the graph
        for a in sett:       
            if (dist[a] < minDist):          
                minDist = dist[a];
                index = a;          
        current = index;  
    return dist;
   
# Function to print the path
# from the source vertex to
# the destination vertex
def printPath(path, i, s):
    #vertex = ''
    if (i != s):
           
        # Condition to check if
        # there is no path between
        # the vertices
        if (path[i] == -1):       
            print("Path not found!!");
            return;       
        vertex = f'{path[i]}, {printPath(path, path[i], s)}'
        #print(str(path[i]) + " ");
        return vertex
# Driver Code
if __name__=='__main__':
     
    v = []
    n = 4
    s = 0;
   
    # Loop to create the nodes
    for i in range(n):
        a = Node(i);
        v.append(a);
   
    # Creating directed
    # weighted edges
    v[0].Add_child(1, 1);
    v[0].Add_child(2, 4);
    v[1].Add_child(2, 2);
    v[1].Add_child(3, 6);
    v[2].Add_child(3, 3);
    path = [0 for i in range(len(v))];
    dist = dijkstraDist(v, s, path);
   
    # Loop to print the distance of
    # every node from source vertex
    for i in range(len(dist)):
        if (dist[i] == infi):
         
            print("{0} and {1} are not " +
                              "connected".format(i, s));
            continue;       
        print("Distance of {}th vertex from source vertex {} is: {}".format(
                          i, s, dist[i]));
     
    # This code is contributed by pratham76