#!/bin/bash

echo "Running Exact Solution for TSP"
for input_file in test_cases/*.txt; do
    echo "Running on $input_file"
    python3 exact_solution.py "$input_file" tsp
    echo
done

echo "Running Approximation Solution for TSP"
for input_file in test_cases/*.txt; do
    echo "Running on $input_file"
    python3 approximation_solution.py "$input_file" tsp
    echo
done

