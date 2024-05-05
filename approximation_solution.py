import sys
import time
import math
from collections import defaultdict

# TSP Approximation using Nearest Neighbor Heuristic
def nearest_neighbor_tsp(graph):
    n = len(graph)
    visited = [False] * n
    current = 0
    path = [0]
    total_weight = 0
    visited[current] = True
    
    for _ in range(n - 1):
        next_node = min((w, v) for v, w in enumerate(graph[current]) if not visited[v])[1]
        total_weight += graph[current][next_node]
        visited[next_node] = True
        path.append(next_node)
        current = next_node
        
    total_weight += graph[path[-1]][0]
    path.append(0)
    return total_weight, path


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
    opt, path = nearest_neighbor_tsp(adj_matrix)
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
