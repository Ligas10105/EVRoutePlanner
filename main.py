from src.graph import Graph
from src.vehicle import ElectricVehicle
from src.charging_station import ChargingStation
from src.ant_colony import AntColonyOptimization

# Definicja grafu
graph = Graph()
nodes = ["A", "B", "C", "D", "E", "F"]
distances = {
    ("A", "B"): 100, ("A", "C"): 150, ("A", "D"): 200, ("A", "E"): 250, ("A", "F"): 300,
    ("B", "C"): 50, ("B", "D"): 120, ("B", "E"): 150, ("B", "F"): 200,
    ("C", "D"): 80, ("C", "E"): 100, ("C", "F"): 200,
    ("D", "E"): 60, ("D", "F"): 150,
    ("E", "F"): 100,
}

# Dodawanie krawędzi do grafu
for (start, end), distance in distances.items():
    graph.add_edge(start, end, distance, difficulty=1.0)
    graph.add_edge(end, start, distance, difficulty=1.0)

# Pojazd elektryczny
vehicle = ElectricVehicle(
    energy_per_km=0.2,      # Zużycie energii na kilometr (kWh)
    battery_capacity=60,    # Pojemność baterii (kWh)
    initial_charge=50       # Początkowy poziom baterii (kWh)
)

# Stacje ładowania
stations = {
    "B": ChargingStation("B", 10, 20, price_per_kwh=0.5, queue_time=0.2, max_power=50),
    "C": ChargingStation("C", 20, 30, price_per_kwh=0.6, queue_time=0.1, max_power=60),
    "D": ChargingStation("D", 30, 40, price_per_kwh=0.4, queue_time=0.3, max_power=55),
    "E": ChargingStation("E", 40, 50, price_per_kwh=0.7, queue_time=0.2, max_power=45),
}

# Parametry algorytmu mrówkowego
aco = AntColonyOptimization(
    graph=graph,
    vehicle=vehicle,
    stations=stations,
    num_ants=10,            # Liczba mrówek
<<<<<<< HEAD
    num_iterations=10,     # Liczba iteracji
    evaporation_rate=0.3,   # Szybkość ewaporacji feromonów
=======
    num_iterations=1,     # Liczba iteracji
    evaporation_rate=0.5,   # Szybkość ewaporacji feromonów
>>>>>>> 03dee4790cc56488c3e80c2f936a3d2c56e631ee
    alpha=1,                # Waga feromonów
    beta=2,                 # Waga heurystyki
    penalty=10            # Kara za niedopuszczalne trasy
)

# Uruchomienie optymalizacji
best_route, best_score = aco.optimize(start_node="A", end_node="F")

# Wyświetlenie wyników
print("\nNajlepsza trasa:", best_route)
print("Najlepszy wynik (score):", best_score)