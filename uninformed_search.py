"""
Artificial Intelligence Assignment
Topic: Problem Solving by Search - Uninformed (Blind) Search
Algorithms: BFS, DFS, DLS, IDDFS, UCS
"""

from collections import deque
import heapq

# ---------------- Input: Tree (Unweighted) ----------------
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
    'F': [],
    'G': [],
    'H': [],
    'I': [],
}

# ---------------- Input: Graph (Weighted, for UCS) ----------------
weighted_graph = {
    'A': [('B', 1), ('C', 5)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 2), ('G', 2)],
    'D': [('H', 4)],
    'E': [('I', 6)],
    'F': [],
    'G': [],
    'H': [],
    'I': [],
}


# ---------------- 1. BFS ----------------
def bfs(graph, start, goal):
    visited = []
    queue = deque([[start]])          # queue of paths
    while queue:
        path = queue.popleft()        # FIFO
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return visited, path
        for neighbor in graph[node]:
            queue.append(path + [neighbor])
    return visited, None


# ---------------- 2. DFS ----------------
def dfs(graph, start, goal):
    visited = []
    stack = [[start]]                 # stack of paths
    while stack:
        path = stack.pop()            # LIFO
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return visited, path
        for neighbor in reversed(graph[node]):   # keep left-to-right order
            stack.append(path + [neighbor])
    return visited, None


# ---------------- 3. DLS (Depth Limited Search) ----------------
def dls(graph, start, goal, limit):
    visited = []

    def recurse(node, depth, path):
        visited.append(node)
        if node == goal:
            return path
        if depth == limit:            # cutoff
            return None
        for neighbor in graph[node]:
            result = recurse(neighbor, depth + 1, path + [neighbor])
            if result:
                return result
        return None

    return visited, recurse(start, 0, [start])


# ---------------- 4. IDDFS ----------------
def iddfs(graph, start, goal, max_depth=10):
    for depth in range(max_depth + 1):
        visited, path = dls(graph, start, goal, depth)
        print(f"   Depth {depth}: {visited}")
        if path:
            return depth, path
    return None, None


# ---------------- 5. UCS (Uniform Cost Search) ----------------
def ucs(graph, start, goal):
    visited = []
    pq = [(0, [start])]               # (cost, path) - min-heap
    while pq:
        cost, path = heapq.heappop(pq)
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return visited, path, cost
        for neighbor, weight in graph[node]:
            heapq.heappush(pq, (cost + weight, path + [neighbor]))
    return visited, None, float('inf')


# ---------------- Output ----------------
if __name__ == "__main__":
    start, goal = 'A', 'I'
    print(f"Start = {start}, Goal = {goal}\n")

    v, p = bfs(graph, start, goal)
    print("1. BFS")
    print("   Traversal:", v)
    print("   Path     :", p, "\n")

    v, p = dfs(graph, start, goal)
    print("2. DFS")
    print("   Traversal:", v)
    print("   Path     :", p, "\n")

    v, p = dls(graph, start, goal, limit=2)
    print("3. DLS (limit = 2)")
    print("   Traversal:", v)
    print("   Path     :", p if p else "Not found within limit", "\n")

    v, p = dls(graph, start, goal, limit=3)
    print("   DLS (limit = 3)")
    print("   Traversal:", v)
    print("   Path     :", p, "\n")

    print("4. IDDFS")
    d, p = iddfs(graph, start, goal)
    print("   Found at depth:", d)
    print("   Path          :", p, "\n")

    v, p, c = ucs(weighted_graph, start, goal)
    print("5. UCS")
    print("   Traversal:", v)
    print("   Path     :", p)
    print("   Total Cost:", c)
