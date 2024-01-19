from aco_algorithm import AntColonyOptimizer
import numpy as np
import time

def read_graph_from_txt(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        nodes = []
        edges = {}

        mode = None
        for line in lines:
            line = line.strip()
            if line == 'Nodos:':
                mode = 'nodes'
            elif line == 'Aristas (con pesos):':
                mode = 'edges'
            elif mode == 'nodes' and line:
                nodes.append(int(line))
            elif mode == 'edges' and line:
                parts = line.split()
                edge = (int(parts[0]), int(parts[2]))
                weight = int(parts[4].strip('()'))
                edges[edge] = weight

        max_node = max(nodes)
        distances = [[float('inf') if i != j else 0 for j in range(max_node + 1)] for i in range(max_node + 1)]
        for (n1, n2), w in edges.items():
            distances[n1][n2] = w
            distances[n2][n1] = w  # Assuming undirected graph

        distances = np.array(distances, dtype=float)
    return distances

def find_route(distances, start=None, end=None):
    # Parámetros del algoritmo ACO (pueden ser ajustados)
    n_ants = 5
    n_best = 2
    n_iterations = 100
    decay = 0.5
    alpha = 1
    beta = 2

    aco = AntColonyOptimizer(distances, n_ants, n_best, n_iterations, decay, alpha, beta)
    
    if start is not None and end is not None:
        route, route_length = aco.run_specific_route(start, end)
    else:
        route, route_length = aco.run()
    
    return route, route_length

def process_graph(file_name, output_file):
    distances = read_graph_from_txt(file_name)
    start_time = time.time()
    route, route_length = find_route(distances)
    end_time = time.time()

    with open(output_file, 'w') as f:
        f.write(f"Ruta encontrada: {route}\n")
        f.write(f"Longitud de la ruta: {route_length}\n")
        f.write(f"Tiempo de resolución: {end_time - start_time} segundos\n")


def main():
    file_name = input("Por favor, ingresa el nombre del archivo TXT con la estructura del grafo: ")
    distances = read_graph_from_txt(file_name)

    choice = input("¿Quieres calcular la ruta por default (D) o una ruta específica de un punto A a un punto B (E)? [D/E]: ").strip().lower()

    if choice == 'e':
        start = int(input("Punto de inicio (A): "))
        end = int(input("Punto final (B): "))
    else:
        start, end = None, None

    start_time = time.time()
    route, route_length = find_route(distances, start, end)
    end_time = time.time()

    print(f"Ruta encontrada: {route} con longitud: {route_length}")
    print(f"Tiempo de resolución: {end_time - start_time} segundos")

if __name__ == "__main__":
    main()
