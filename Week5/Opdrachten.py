class myqueue(list):
    def __init__(self, a=[]):
        list.__init__(self, a)

    def dequeue(self):
        return self.pop(0)

    def enqueue(self, x):
        self.append(x)


class Vertex:
    def __init__(self, data):
        self.data = data

    def __repr__(self):  # voor afdrukken
        return str(self.data)

    def __lt__(self, other):  # voor sorteren
        return self.data < other.data


import math

INFINITY = math.inf  # float("inf")


def vertices(G):
    return sorted(G)


def edges(G):
    return [(u, v) for u in vertices(G) for v in G[u]]

def clear(G):
    for v in vertices(G):
        k = [e for e in vars(v) if e != 'data']
        for e in k:
            delattr(v, e)


def BFS(G, s):
    V = vertices(G)
    s.predecessor = None
    s.distance = 0
    for v in V:
        if v != s:
            v.distance = INFINITY  # v krijgt het attribuut 'distance'
    q = myqueue()
    q.enqueue(s)
    #    print("q:", q)
    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance == INFINITY:  # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u  # v krijgt het attribuut 'predecessor'
                q.enqueue(v)

def show_tree_info(G):
    print('tree:', end=' ')
    for v in vertices(G):
        print('(' + str(v), end='')
        if hasattr(v, 'distance'):
            print(',d:' + str(v.distance), end='')
        if hasattr(v, 'predecessor'):
            print(',p:' + str(v.predecessor), end='')
        print(')', end=' ')
    print()

def show_sorted_tree_info(G):
    print('sorted tree:')
    V = vertices(G)
    #    V = [v for v in V if hasattr(v,'distance') and hasattr(v,'predecessor')]
    V.sort(key=lambda x: (x.distance, x.predecessor))
    d = 0
    for v in V:
        if v.distance > d:
            print()
            d += 1
        print('(' + str(v) + ',d:' + str(v.distance) + ',p:'
              + str(v.predecessor), end='')
        print(')', end=' ')
    print()

def path_BFS(G, u, v):
    BFS(G, u)
    a = []
    if hasattr(v, 'predecessor'):
        current = v
        while current:
            a.append(current)
            current = current.predecessor
        a.reverse()
    return a

#################################################################

def is_connected(G):
    V = vertices(G)
    BFS(G, V[0])
    for v in G:
        if v.distance == INFINITY:
            return False
    return True

def no_cycles(G):
    V = vertices(G)
    current_node = V[0]
    current_node.predecessor = None
    current_node.distance = 0
    for v in V:
        if v != current_node:
            v.distance = INFINITY
    q = myqueue()
    q.enqueue(current_node)
    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance == INFINITY:
                v.distance = u.distance + 1
                v.predecessor = u
                q.enqueue(v)
            elif u.predecessor != v:
                return False
    return True

def get_bridges(G):
    bridges = []
    for u in vertices(G):
        G[u] = sorted(G[u])
        for v in G[u]:
            G[u].remove(v)
            clear(G)
            BFS(G, u)
            if v.distance is INFINITY:
                if (u,v) not in bridges:
                    bridges.append((u,v))
            G[u].append(v)
            G[u] = sorted(G[u])
    return bridges

def is_strongly_connected(G):
    V = vertices(G)
    s = V[0]
    BFS(G,s)
    for node in G:
        if node.distance is INFINITY:
            return False
    G2 = G
    for vertex in edges(G2):
        G2[vertex[0]].remove(vertex[1])
        G2[vertex[1]].append(vertex[0])
    BFS(G2,s)
    for node in G2:
        if node.distance is INFINITY:
            return False
    return True

def is_euler_graph(G):
    for node in G:
        if not len(G[node]) % 2 == 0:
            return False
    return True

def get_euler_circuit(G,start):
    euler_circuit =[start]
    bridges = get_bridges(G)
    list_of_edges = edges(G)
    current = start
    next_node = None;
    only_bridges = True

    while list_of_edges != []:
        for neighbor in G[current]:
            if (current,neighbor) not in bridges:
                next_node = neighbor
                only_bridges = False
                break

        if only_bridges == True:
            next_node = G[current][0]

        only_bridges = True

        G[current].remove(next_node)
        G[next_node].remove(current)

        list_of_edges = edges(G)
        bridges = get_bridges(G)

        current = next_node
        euler_circuit.append(current)

    return euler_circuit

v = [Vertex(i) for i in range(8)]

G1 = {v[0]: [v[1], v[2]],
      v[1]: [v[0]],
      v[2]: [v[0]]}

G2 = {v[0]: [v[1], v[3]],
      v[1]: [v[0]],
      v[2]: [v[0]],
      v[3]: [v[4]],
      v[4]: [v[3]]}

G3 = {v[0]: [v[1], v[4]],
      v[1]: [v[0], v[5]],
      v[2]: [v[3], v[5]],
      v[3]: [v[2], v[6]],
      v[4]: [v[0]],
      v[5]: [v[1], v[2]],
      v[6]: [v[3], v[7]],
      v[7]: [v[6]]}

G4 = {v[0]: [v[1], v[4]],
      v[1]: [v[0], v[5]],
      v[2]: [v[3], v[5]],
      v[3]: [v[2], v[6]],
      v[4]: [v[0], v[5]],
      v[5]: [v[1], v[2], v[4]],
      v[6]: [v[3], v[7]],
      v[7]: [v[6]]}

G5 = {v[0]: [v[1], v[3]],
      v[1]: [v[0], v[2]],
      v[2]: [v[1], v[3], v[4]],
      v[3]: [v[0], v[2]],
      v[4]: [v[2], v[5], v[6]],
      v[5]: [v[4], v[6]],
      v[6]: [v[4], v[5], v[7]],
      v[7]: [v[6]]}

v1 = [Vertex(i) for i in range(3)]

G6 = {v1[0]: [v1[1]],
      v1[1]: [v1[2]],
      v1[2]: [v1[0]]}

G7 = {v1[0]: [v1[1]],
      v1[1]: [],
      v1[2]: [v1[0], v1[1]]}

v3 = [Vertex(i) for i in range(6)]

G8 = {v3[0]: [v3[1]],
      v3[1]: [v3[2]],
      v3[2]: [v3[0], v3[3]],
      v3[3]: [v3[4]],
      v3[4]: [v3[5]],
      v3[5]: [v3[4]]}

G9 = {v3[0]: [v3[3], v3[4]],
       v3[1]: [v3[3], v3[5]],
       v3[2]: [v3[4], v3[5]],
       v3[3]: [v3[0], v3[1]],
       v3[4]: [v3[0], v3[2]],
       v3[5]: [v3[1], v3[2]]}

v4 = [Vertex(i) for i in range(8)]

G10 = {v4[0]: [v4[1], v4[3]],
      v4[1]: [v4[0], v4[2]],
      v4[2]: [v4[1], v4[3], v4[4]],
      v4[3]: [v4[0], v4[2]],
      v4[4]: [v4[2], v4[5], v4[6]],
      v4[5]: [v4[4], v4[6]],
      v4[6]: [v4[4], v4[5], v4[7]],
      v4[7]: [v4[6]]}

G11 ={ v4[0]: [v4[1], v4[2]],
       v4[1]: [v4[0], v4[3]],
       v4[2]: [v4[0], v4[3]],
       v4[3]: [v4[1], v4[2], v4[4], v4[6]],
       v4[4]: [v4[3], v4[5], v4[6], v4[7]],
       v4[5]: [v4[4], v4[6]],
       v4[6]: [v4[3], v4[4], v4[5], v4[7]],
       v4[7]: [v4[4], v4[6]]}

G12 = {key: value[:] for key, value in G11.items()}
G13 = {key: value[:] for key, value in G11.items()}
G14 = {key: value[:] for key, value in G11.items()}

print("Is connected should be True:", is_connected(G1))
print("Is connected should be False:", is_connected(G2))
print("No cycles should be True:", no_cycles(G3))
print("No cycles should be False:", no_cycles(G4))
print("Get bridges should be [(2, 4), (4, 2), (6, 7), (7, 6)]:", get_bridges(G5))
print("Is strongly connected should be True:", is_strongly_connected(G6))
print("Is strongly connected should be False:", is_strongly_connected(G7))
print("Is strongly connected should be False:", is_strongly_connected(G8))
print("Is euler graph should be True:", is_euler_graph(G9))
print("Is euler graph should be False:", is_euler_graph(G10))
print("Euler circuit when starting at node [4]:", get_euler_circuit(G11, v4[4]))
print("Euler circuit when starting at node [5]:", get_euler_circuit(G12, v4[5]))
print("Euler circuit when starting at node [6]:", get_euler_circuit(G13, v4[6]))
print("Euler circuit when starting at node [0]:", get_euler_circuit(G14, v4[0]))