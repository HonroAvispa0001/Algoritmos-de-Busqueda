import numpy as np
from numpy.random import choice as np_choice

class AntColonyOptimizer:
    def __init__(self, distances, n_ants, n_best, n_iterations, decay, alpha=1, beta=1):
        """
        Inicializa el optimizador de colonia de hormigas.
        """
        self.distances = np.array(distances)
        self.pheromone = np.ones(self.distances.shape) / len(distances)
        self.all_inds = range(len(distances))
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta
        #print("Matriz de Distancias Inicial:")
        #print(self.distances)

    def _route_length(self, route):
        """
        Calcula la longitud de una ruta.
        """
        total_length = 0
        for i in range(len(route) - 1):
            total_length += self.distances[route[i]][route[i + 1]]
        return total_length
    
    

    def _choose_next_node(self, current_node, visited):
        """
        Elige el siguiente nodo para una hormiga.
        """
        probabilities = []
        pheromone = self.pheromone[current_node, :]
        for i in self.all_inds:
            if i not in visited and self.distances[current_node][i] != float('inf'):
                prob = (pheromone[i] ** self.alpha) * ((1.0 / self.distances[current_node][i]) ** self.beta)
                probabilities.append(prob)
            else:
                probabilities.append(0)

        sum_probabilities = np.sum(probabilities)
        if sum_probabilities == 0:
            # Distribuir uniformemente entre los nodos no visitados
            probabilities = [1.0 / (len(self.all_inds) - len(visited)) if i not in visited else 0 for i in self.all_inds]
        else:
            probabilities = np.array(probabilities) / sum_probabilities

        next_node = np_choice(self.all_inds, 1, p=probabilities)[0]
        #print(f"Probabilidades desde el nodo {current_node}: {probabilities}")
        #print(f"Nodo elegido: {next_node}")
        return next_node
    
    def run_specific_route(self, start, end):
        """
        Ejecuta el algoritmo ACO para encontrar una ruta específica de un punto A a un punto B.
        """
        shortest_route = None
        shortest_route_length = float('inf')

        for _ in range(self.n_iterations):
            all_routes = [self._simulate_ant_specific_route(start, end) for _ in range(self.n_ants)]
            all_routes = sorted(all_routes, key=self._route_length)
            best_routes = all_routes[:self.n_best]

            self._update_pheromone(best_routes)

            if self._route_length(best_routes[0]) < shortest_route_length:
                shortest_route = best_routes[0]
                shortest_route_length = self._route_length(shortest_route)

        return shortest_route, shortest_route_length

    def _simulate_ant_specific_route(self, start, end):
        """
        Simula el camino de una hormiga desde un nodo inicial hasta un nodo final.
        """
        route = [start]
        current_node = start
        visited = set([current_node])

        while current_node != end:
            current_node = self._choose_next_node(current_node, visited)
            route.append(current_node)
            visited.add(current_node)

        #print(f"Ruta generada por la hormiga: {route}")
        return route


    def _simulate_ant(self):
        """
        Simula el camino de una hormiga.
        """
        route = []
        current_node = np.random.choice(self.all_inds)  # Comienza en un nodo aleatorio
        route.append(current_node)
        visited = set([current_node])

        while len(route) < len(self.distances):
            current_node = route[-1]
            next_node = self._choose_next_node(current_node, visited)
            route.append(next_node)
            visited.add(next_node)

        return route
    
    

    def _update_pheromone(self, best_routes):
        """
        Actualiza la matriz de feromonas.
        """
        self.pheromone *= (1 - self.decay)  # Evaporación de feromonas
        for route in best_routes:
            route_length = self._route_length(route)
            for i in range(len(route) - 1):
                self.pheromone[route[i], route[i+1]] += 1.0 / route_length
        #print("Actualización de feromonas:")
        #print(self.pheromone)

    def run(self):
        """
        Ejecuta el algoritmo ACO.
        """
        shortest_route = None
        shortest_route_length = float('inf')

        for _ in range(self.n_iterations):
            all_routes = [self._simulate_ant() for _ in range(self.n_ants)]
            all_routes = sorted(all_routes, key=self._route_length)
            best_routes = all_routes[:self.n_best]

            self._update_pheromone(best_routes)

            if self._route_length(best_routes[0]) < shortest_route_length:
                shortest_route = best_routes[0]
                shortest_route_length = self._route_length(shortest_route)

        return shortest_route, shortest_route_length
