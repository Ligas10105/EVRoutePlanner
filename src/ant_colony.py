import random
from src.objective_function import objective_function

class AntColonyOptimization:
    def __init__(self, graph, vehicle, stations, num_ants, num_iterations, evaporation_rate, alpha, beta, penalty=1000, pheromone_importance_probability=0.8):
        """
        Inicjalizacja algorytmu mrówkowego.
        :param graph: Graf trasy.
        :param vehicle: Obiekt pojazdu elektrycznego.
        :param stations: Słownik stacji ładowania.
        :param num_ants: Liczba mrówek.
        :param num_iterations: Liczba iteracji.
        :param evaporation_rate: Współczynnik ewaporacji feromonów.
        :param alpha: Waga feromonów.
        :param beta: Waga heurystyki (odległość, trudność).
        :param penalty: Kara za niedopuszczalne trasy.
        :param pheromone_importance_probability: Prawdopodobieństwo uwzględnienia feromonów.
        """
        self.graph = graph
        self.vehicle = vehicle
        self.stations = stations
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.evaporation_rate = evaporation_rate
        self.alpha = alpha
        self.beta = beta
        self.penalty = penalty
        self.pheromone_importance_probability = pheromone_importance_probability
        self.pheromones = {edge: 1.0 for edge in self.graph.edges}  # Inicjalizacja feromonów
        print(f"Algorytm mrówkowy zainicjalizowany z {num_ants} mrówkami, {num_iterations} iteracjami.")

    def _select_next_node(self, current_node, visited, current_charge):
        """
        Wybiera następny węzeł na podstawie feromonów i heurystyki z pewnym prawdopodobieństwem.
        """
        neighbors = self.graph.get_neighbors(current_node, visited, current_charge, self.vehicle)
        if not neighbors:
            return None

        if random.random() < self.pheromone_importance_probability:
            probabilities = []
            for neighbor, edge_data in neighbors.items():
                pheromone = self.pheromones.get((current_node, neighbor), 1.0)
                distance = edge_data["distance"]
                difficulty = edge_data["difficulty"]
                heuristic = 1 / (distance * difficulty)
                probabilities.append((neighbor, (pheromone ** self.alpha) * (heuristic ** self.beta)))

            total = sum(prob for _, prob in probabilities)
            probabilities = [(node, prob / total) for node, prob in probabilities]

            next_node = random.choices([node for node, _ in probabilities], [prob for _, prob in probabilities])[0]
            return next_node
        else:
            next_node = random.choice(list(neighbors.keys()))
            return next_node

    def _build_solution(self, start_node, end_node):
        """
        Buduje trasę przy pomocy jednej mrówki.
        """
        current_node = start_node
        visited = {current_node}
        route = [current_node]
        current_charge = self.vehicle.charge

        while current_node != end_node:
            next_node = self._select_next_node(current_node, visited, current_charge)
            if next_node is None:
                return None
            route.append(next_node)
            visited.add(next_node)

            distance = self.graph.edges[current_node][next_node]["distance"]
            current_charge -= distance * self.vehicle.energy_per_km

            if current_charge < 0:
                station = self.stations.get(current_node)
                if station:
                    current_charge = min(self.vehicle.battery_capacity, self.vehicle.battery_capacity)
                else:
                    return None

            current_node = next_node

        if current_node == end_node:
            return route
        else:
            return None

    def _evaporate_pheromones(self):
        """
        Redukuje ilość feromonów na wszystkich krawędziach (ewaporacja).
        """
        for edge in self.pheromones:
            self.pheromones[edge] *= (1 - self.evaporation_rate)

    def _update_pheromones(self, routes):
        """
        Aktualizuje poziom feromonów na podstawie wyników tras.
        """
        for route, score in routes:
            pheromone_contribution = 1 / score
            for i in range(len(route) - 1):
                edge = (route[i], route[i + 1])
                if edge in self.pheromones:
                    self.pheromones[edge] += pheromone_contribution

    def optimize(self, start_node, end_node):
        """
        Uruchamia optymalizację algorytmem mrówkowym.
        """
        best_route = None
        best_score = float("inf")
        iteration_scores = []

        for iteration in range(self.num_iterations):
            routes = []
            for _ in range(self.num_ants):
                route = self._build_solution(start_node, end_node)
                if route:
                    score = objective_function([route], self.vehicle, self.stations, self.graph, self.penalty)[1]
                    routes.append((route, score))

            self._evaporate_pheromones()
            self._update_pheromones(routes)

            for route, score in routes:
                if score < best_score:
                    best_route = route
                    best_score = score

            iteration_scores.append(best_score)
            print(f"Iteracja {iteration + 1}/{self.num_iterations}: Najlepszy wynik = {best_score:.2f}")

        print(f"Optymalizacja zakończona. Najlepsza trasa: {best_route} o wyniku {best_score:.2f}.")
        return best_route, best_score, iteration_scores
