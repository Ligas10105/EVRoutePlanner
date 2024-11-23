from itertools import permutations
from src.charging_station import ChargingStation
from src.graph import Graph
from src.vehicle import ElectricVehicle
from src.objective_function import objective_function


graph = Graph()
nodes = ["A", "B", "C", "D", "E", "F"]
distances = {
    ("A", "B"): 100, ("A", "C"): 150, ("A", "D"): 200, ("A", "E"): 250, ("A", "F"): 300,
    ("B", "C"): 50, ("B", "D"): 120, ("B", "E"): 150, ("B", "F"): 200,
    ("C", "D"): 80, ("C", "E"): 100, ("C", "F"): 200,
    ("D", "E"): 60, ("D", "F"): 150,
    ("E", "F"): 100,
}

for (start, end), distance in distances.items():
    graph.add_edge(start, end, distance, difficulty=1.0)
    graph.add_edge(end, start, distance, difficulty=1.0)

# Pojazd elektryczny
vehicle = ElectricVehicle(
    max_range=300,
    energy_per_km=0.2,
    battery_capacity=60,
    initial_charge=60
)

# Stacje ładowania
stations = {
    "B": ChargingStation("B", 10, 20, price_per_kwh=0.5, queue_time=0.2, max_power=50),
    "C": ChargingStation("C", 20, 30, price_per_kwh=0.6, queue_time=0.1, max_power=60),
    "D": ChargingStation("D", 30, 40, price_per_kwh=0.4, queue_time=0.3, max_power=55),
    "E": ChargingStation("E", 40, 50, price_per_kwh=0.7, queue_time=0.2, max_power=45),
}

# Generowanie tras
points = ["B", "C", "D", "E"]
routes = []
for perm in permutations(points, len(points)):
    route = ["A"] + list(perm) + ["F"]
    routes.append(route)

# Walidacja tras
valid_routes = []
for route in routes:
    if all(
        graph.edges.get(route[i], {}).get(route[i + 1]) is not None
        for i in range(len(route) - 1)
    ):
        valid_routes.append(route)
    else:
        print(f"Trasa {route} jest niemożliwa w grafie.")

# Wyznaczenie najlepszej trasy
best_route, best_score = objective_function(valid_routes, vehicle, stations, graph)
print("\nNajlepsza trasa:", best_route)
print("Najlepszy wynik (score):", best_score)