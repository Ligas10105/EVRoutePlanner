import random
from src.objective_function import objective_function
import time

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
        self.pheromone_importance_probability = pheromone_importance_probability
        self.penalty = penalty
        
        self.pheromones = {edge: 1.0 for edge in self.graph.edges}  # Inicjalizacja feromonów
        # print(f"Algorytm mrówkowy zainicjalizowany z {num_ants} mrówkami, {num_iterations} iteracjami.")

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
        current_node = start_node
        visited = {current_node}
        route = [current_node]
        current_charge = self.vehicle.charge
        total_distance = 0  # Dodanie zmiennej do przechowywania całkowitej długości

        while current_node != end_node:
            next_node = self._select_next_node(current_node, visited, current_charge)
            if next_node is None:
                return None, None  # Zwracamy również brak długości
            route.append(next_node)
            visited.add(next_node)

            distance = self.graph.edges[current_node][next_node]["distance"]
            total_distance += distance  # Dodawanie długości krawędzi
            current_charge -= distance * self.vehicle.energy_per_km

            if current_charge < 0:
                station = self.stations.get(current_node)
                if station:
                    current_charge = min(self.vehicle.battery_capacity, self.vehicle.battery_capacity)
                else:
                    return None, None

            current_node = next_node

        if current_node == end_node:
            return route, total_distance  # Zwracamy trasę i jej długość
        else:
            return None, None


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
        best_route = None
        best_score = float("inf")
        best_distance = float("inf")
        iteration_scores = []
        iteration_times = []
        unique_paths_per_iteration = []  # Lista do przechowywania unikalnych tras w każdej iteracji
        average_scores_per_iteration = []  # Lista średnich wyników w każdej iteracji
        score_differences = []  # Lista różnic między średnią a najlepszym wynikiem
        unique_paths = set()  # Zestaw do przechowywania unikalnych tras w bieżącej iteracji

        for iteration in range(self.num_iterations):
            start_time = time.time()
            routes = []
            total_score = 0  # Do obliczenia średniego wyniku w iteracji
            valid_routes = 0  # Licznik tras z wynikiem większym niż 0

            for _ in range(self.num_ants):
                route, total_distance = self._build_solution(start_node, end_node)
                if route:
                    score = objective_function([route], self.vehicle, self.stations, self.graph, self.penalty)[1]
                    
                    # Tylko dodajemy trasy z wynikiem większym niż 0
                    if score > 0:
                        routes.append((route, score, total_distance))
                        unique_paths.add(tuple(route))  # Dodajemy trasę jako krotkę (tupla) do zestawu
                        total_score += score  # Sumujemy wyniki dla obliczenia średniej
                        valid_routes += 1  # Zwiększamy licznik ważnych tras

            self._evaporate_pheromones()
            self._update_pheromones([(route, score) for route, score, _ in routes])

            for route, score, total_distance in routes:
                if score < best_score:
                    best_route = route
                    best_score = score
                    best_distance = total_distance

            # Obliczenie średniej w tej iteracji tylko z ważnych tras
            average_score = total_score / valid_routes if valid_routes > 0 else 100
            
            # Obliczenie różnicy między najlepszym wynikiem a średnim wynikiem
            if valid_routes > 0:
                score_difference = best_score - average_score
            else:
                score_difference = 0  # Jeśli brak tras z wynikiem > 0, różnica jest 0

            end_time = time.time()
            iteration_scores.append(best_score)
            iteration_times.append(end_time - start_time)
            average_scores_per_iteration.append(average_score)
            score_differences.append(score_difference)

            # Dodanie liczby unikalnych tras do listy
            unique_paths_per_iteration.append(len(unique_paths))

        # Obliczenie średniego czasu dla wszystkich iteracji
        avg_time_per_iteration = sum(iteration_times) / self.num_iterations if self.num_iterations > 0 else 0

        # Dodanie liczby unikalnych ścieżek (zestaw zawiera tylko unikalne ścieżki)
        total_unique_paths = len(unique_paths)

        return best_route, best_score, iteration_scores, iteration_times, best_distance, unique_paths_per_iteration, average_scores_per_iteration, score_differences, avg_time_per_iteration, total_unique_paths
