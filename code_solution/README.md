# Weighted Graph Problems (TSP)

## Overview

This solution provides both exact and approximate algorithms for solving the Traveling Salesman Problem (TSP) on weighted graphs. The solution is implemented in Python.

## Files

- `exact_solution.py`: Contains the exact solution algorithm.
- `approximation_solution.py`: Contains the approximation solution algorithm.
- `generation.py`: Test case generator for creating complete weighted graphs.
- `test_cases/`: Contains given and generated test cases.
- `run.sh`: A shell script for running all test cases.

## Running the Programs

### Exact Solution

To run the exact solution for TSP, use the following command:

```bash
python3 exact_solution.py <input_file> tsp
```

### Approximate Solution

To run the approximate solution for TSP, use the following command:

```bash
python3 approximation_solution.py <input_file> tsp