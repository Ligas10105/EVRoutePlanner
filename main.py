from src.graph import Graph
from src.vehicle import ElectricVehicle
from src.charging_station import ChargingStation
from src.ant_colony import AntColonyOptimization

# Definicja grafu
graph = Graph()
nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
distances = {
    ("A", "B"): 50, ("A", "C"): 100, ("A", "D"): 150,
    ("B", "E"): 70, ("B", "F"): 90,
    ("C", "F"): 60, ("C", "G"): 110, ("C", "H"): 120,
    ("D", "H"): 80, ("D", "I"): 100,
    ("E", "J"): 50, ("E", "K"): 90,
    ("F", "K"): 70, ("F", "L"): 85, ("F", "M"): 120,
    ("G", "M"): 65, ("G", "N"): 95,
    ("H", "N"): 75, ("H", "O"): 110,
    ("I", "O"): 85, ("I", "P"): 100,
    ("J", "Q"): 60, ("J", "R"): 80,
    ("K", "R"): 70, ("K", "S"): 110,
    ("L", "S"): 90, ("L", "T"): 115,
    ("M", "T"): 100, ("N", "T"): 70,
    ("O", "S"): 95, ("P", "T"): 85,
}


difficulty = {
    ("A", "B"): 1.0, ("A", "C"): 1.2, ("A", "D"): 1.5,
    ("B", "E"): 1.1, ("B", "F"): 1.3,
    ("C", "F"): 1.0, ("C", "G"): 1.4, ("C", "H"): 1.5,
    ("D", "H"): 1.2, ("D", "I"): 1.6,
    ("E", "J"): 1.0, ("E", "K"): 1.4,
    ("F", "K"): 1.2, ("F", "L"): 1.5, ("F", "M"): 1.3,
    ("G", "M"): 1.1, ("G", "N"): 1.6,
    ("H", "N"): 1.3, ("H", "O"): 1.4,
    ("I", "O"): 1.2, ("I", "P"): 1.6,
    ("J", "Q"): 1.0, ("J", "R"): 1.2,
    ("K", "R"): 1.3, ("K", "S"): 1.5,
    ("L", "S"): 1.4, ("L", "T"): 1.5,
    ("M", "T"): 1.2, ("N", "T"): 1.1,
    ("O", "S"): 1.3, ("P", "T"): 1.5,
}

# Dodawanie krawędzi do grafu
for (start, end), distance in distances.items():
    graph.add_edge(start, end, distance, difficulty=difficulty[(start, end)])
    graph.add_edge(end, start, distance, difficulty=difficulty[(start, end)])

# Pojazd elektryczny
vehicle = ElectricVehicle(
    energy_per_km=0.2,      # Zużycie energii na kilometr (kWh)
    battery_capacity=60,    # Pojemność baterii (kWh)
    initial_charge=50       # Początkowy poziom baterii (kWh)
)

# Stacje ładowania
stations = {
    "B": ChargingStation("B", 10, 20, price_per_kwh=0.5, queue_time=0.2, max_power=50),
    "H": ChargingStation("H", 20, 30, price_per_kwh=0.6, queue_time=0.1, max_power=60),
    "K": ChargingStation("K", 30, 40, price_per_kwh=0.4, queue_time=0.3, max_power=55),
    "N": ChargingStation("N", 40, 50, price_per_kwh=0.7, queue_time=0.2, max_power=45),
    "T": ChargingStation("T", 50, 60, price_per_kwh=0.5, queue_time=0.3, max_power=50),
}


# # Parametry algorytmu mrówkowego
# aco = AntColonyOptimization(
#     graph=graph,
#     vehicle=vehicle,
#     stations=stations,
#     num_ants=10,            # Liczba mrówek
#     num_iterations=1,     # Liczba iteracji
#     evaporation_rate=0.5,   # Szybkość ewaporacji feromonów
#     alpha=1,                # Waga feromonów
#     beta=2,                 # Waga heurystyki
#     penalty=10            # Kara za niedopuszczalne trasy
# )

# # Uruchomienie optymalizacji
# best_route, best_score = aco.optimize(start_node="A", end_node="F")

# # Wyświetlenie wyników
# print("\nNajlepsza trasa:", best_route)
# print("Najlepszy wynik (score):", best_score)

parameter_sets = [
    {"alpha": 1, "beta": 5, "evaporation_rate": 0.5, "penalty": 100},
    {"alpha": 2, "beta": 3, "evaporation_rate": 0.7, "penalty": 500},
    {"alpha": 1.5, "beta": 4, "evaporation_rate": 0.6, "penalty": 300},
]

best_overall_score = float("inf")
best_params = None

for params in parameter_sets:
    print(f"Testing parameters: {params}")
    aco = AntColonyOptimization(
        graph=graph,
        vehicle=vehicle,
        stations=stations,
        num_ants=10,
        num_iterations=10,
        evaporation_rate=params["evaporation_rate"],
        alpha=params["alpha"],
        beta=params["beta"],
        penalty=params["penalty"],
    )
    best_route, best_score = aco.optimize(start_node="A", end_node="F")
    print(f"Best score for parameters {params}: {best_score}")

    if best_score < best_overall_score:
        best_overall_score = best_score
        best_params = params

print(f"\nBest overall parameters: {best_params}")
print(f"Best overall score: {best_overall_score}")

print("\n\nSłabe parametry")
poor_parameter_sets = [
    {"alpha": 0, "beta": 10, "evaporation_rate": 0.1, "penalty": 10},
    {"alpha": 10, "beta": 0.5, "evaporation_rate": 0.9, "penalty": 10000},
    {"alpha": 5, "beta": 0.1, "evaporation_rate": 1.0, "penalty": 0},
]

for params in poor_parameter_sets:
    print(f"Testing poor parameters: {params}")
    aco = AntColonyOptimization(
        graph=graph,
        vehicle=vehicle,
        stations=stations,
        num_ants=1,
        num_iterations=5,
        evaporation_rate=params["evaporation_rate"],
        alpha=params["alpha"],
        beta=params["beta"],
        penalty=params["penalty"],
    )
    best_route, best_score = aco.optimize(start_node="I", end_node="Q")
    print(f"Result for poor parameters {params}: {best_score}\n")
