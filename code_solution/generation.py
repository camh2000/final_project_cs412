import random
import string

def generate_complete_graph(n, filename):
    def generate_name(index):
        # Generate a name using letters or digits based on the index.
        return string.ascii_lowercase[index]

    with open(filename, "w") as file:
        file.write(f"{n} {n * (n - 1) // 2}\n")
        for i in range(n):
            for j in range(i + 1, n):
                weight = random.randint(1, 100)
                u = generate_name(i)
                v = generate_name(j)
                file.write(f"{u} {v} {weight}\n")

# Generating graphs with n vertices
generate_complete_graph(4, "test_cases/tsp_4.txt")
generate_complete_graph(5, "test_cases/tsp_5.txt")
generate_complete_graph(6, "test_cases/tsp_6.txt")
generate_complete_graph(7, "test_cases/tsp_7.txt")
generate_complete_graph(8, "test_cases/tsp_8.txt")
generate_complete_graph(9, "test_cases/tsp_9.txt")
generate_complete_graph(10, "test_cases/tsp_10.txt")
generate_complete_graph(15, "test_cases/tsp_15.txt")
