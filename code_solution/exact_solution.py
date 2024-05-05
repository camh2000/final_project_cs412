import sys
import itertools
import math
import time
from collections import defaultdict

# TSP Exact Solution using Held-Karp
def held_karp_tsp(graph):
    n = len(graph)
    C = {}

    # Initialize base cases
    for k in range(1, n):
        C[(1 << k, k)] = (graph[0][k], [0, k])

    # Fill in the remaining subproblems
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit
            for k in subset:
                prev = bits & ~(1 << k)
                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + graph[m][k], C[(prev, m)][1] + [k]))
                C[(bits, k)] = min(res)

    # Now, consider the subset that contains all the vertices, except 0, ending with any vertex
    res = []
    bits = (2**n - 1) - 1
    for k in range(1, n):
        res.append((C[(bits, k)][0] + graph[k][0], C[(bits, k)][1] + [0]))
    opt, path = min(res)
    return opt, path

def parse_input(input_file):
    with open(input_file, "r") as file:
        lines = file.readlines()
        
    n, m = map(int, lines[0].split())
    graph = defaultdict(list)
    
    for line in lines[1:]:
        u, v, w = line.strip().split()
        graph[u].append((v, int(w)))
        graph[v].append((u, int(w)))
        
    return n, m, graph

def solve_tsp(input_file):
    n, m, graph = parse_input(input_file)
    vertices = list(graph.keys())
    vertex_to_idx = {vertices[i]: i for i in range(n)}
    adj_matrix = [[math.inf] * n for _ in range(n)]
    
    for u in graph:
        for v, w in graph[u]:
            adj_matrix[vertex_to_idx[u]][vertex_to_idx[v]] = w
            adj_matrix[vertex_to_idx[v]][vertex_to_idx[u]] = w
            
    start_time = time.perf_counter_ns()
    opt, path = held_karp_tsp(adj_matrix)
    end_time = time.perf_counter_ns()
    result = f"{opt}\n{' '.join(vertices[i] for i in path)}"
    return result, end_time - start_time

if __name__ == "__main__":
    input_file = sys.argv[1]
    problem_type = sys.argv[2]
    if problem_type == "tsp":
        result, execution_time = solve_tsp(input_file)
    else:
        raise ValueError("Unknown problem type")
    print(result)
    print(f"Execution Time: {execution_time} nanoseconds")
