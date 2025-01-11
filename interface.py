import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.graph import Graph
from src.vehicle import ElectricVehicle
from src.charging_station import ChargingStation
from src.ant_colony import AntColonyOptimization

# Stała definicja distances
distances = {
    ("A", "B"): 100, ("A", "C"): 150, ("A", "D"): 200, ("A", "E"): 250, ("A", "F"): 300,
    ("B", "C"): 50, ("B", "D"): 120, ("B", "E"): 150, ("B", "F"): 200,
    ("C", "D"): 80, ("C", "E"): 100, ("C", "F"): 200,
    ("D", "E"): 60, ("D", "F"): 150,
    ("E", "F"): 100,
}

def run_interface():
    # Inicjalizacja głównego okna
    root = tk.Tk()
    root.geometry("1200x800")
    root.title("Electronic Vehicle Route Planner")

    # Konfiguracja siatki dla głównego okna
    root.grid_rowconfigure(0, weight=1)  # Sekcja wyników
    root.grid_rowconfigure(1, weight=4)  # Sekcja grafu
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=3)

    # Ramka na lewą część (parametry)
    left_frame = tk.Frame(root, bg="lightgray", padx=5, pady=5)
    left_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")  # Rozciągnięcie na dwie sekcje

    # Ramka na wyniki
    results_frame = tk.Frame(root, bg="white")
    results_frame.grid(row=0, column=1, sticky="nsew")

    # Ramka na graf
    graph_frame = tk.Frame(root, bg="white")
    graph_frame.grid(row=1, column=1, sticky="nsew")

    # Etykieta wyników w ramce „Wyniki”
    result_label = tk.Label(results_frame, text="Wyniki pojawią się tutaj", bg="white", font=("Helvetica", 14))
    result_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Funkcja do tworzenia pola wprowadzania z etykietą
    def create_entry_field(parent, label_text, row, width=10):
        label = tk.Label(parent, text=label_text, bg="lightgray")
        label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
        entry = ttk.Entry(parent, width=width)
        entry.grid(row=row, column=1, sticky="ew", padx=5, pady=5)
        return entry

    # Konfiguracja siatki dla ramki po lewej stronie
    for i in range(12):  # Ustal ilość wierszy w grid
        left_frame.grid_rowconfigure(i, weight=1)
    left_frame.grid_columnconfigure(0, weight=1)
    left_frame.grid_columnconfigure(1, weight=1)

    # Parametry pojazdu
    energy_consumption_entry = create_entry_field(left_frame, "Zużycie energii na km:", row=1)
    battery_capacity_entry = create_entry_field(left_frame, "Pojemność baterii:", row=2)
    initial_charge_entry = create_entry_field(left_frame, "Początkowy poziom baterii:", row=3)

    # Parametry algorytmu mrówkowego
    num_ants_entry = create_entry_field(left_frame, "Liczba mrówek:", row=4)
    iterations_entry = create_entry_field(left_frame, "Liczba iteracji:", row=5)
    evaporation_rate_entry = create_entry_field(left_frame, "Szybkość ewaporacji:", row=6)
    alpha_entry = create_entry_field(left_frame, "Waga feromonów:", row=7)
    beta_entry = create_entry_field(left_frame, "Waga heurystyki:", row=8)
    penalty_entry = create_entry_field(left_frame, "Kara za niedopuszczalne trasy:", row=9)

    # Funkcja do wizualizacji grafu
    def show_graph():
        graph = Graph()
        for (start, end), distance in distances.items():
            graph.add_edge(start, end, distance)
            graph.add_edge(end, start, distance)

        G = nx.Graph()
        for node1 in graph.edges:
            for node2, edge_data in graph.edges[node1].items():
                G.add_edge(node1, node2, weight=edge_data["distance"])

        pos = nx.spring_layout(G, seed=42)
        fig, ax = plt.subplots(figsize=(6, 4))

        nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue",
                font_size=10, font_weight="bold", edge_color="gray", ax=ax)
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,
                                     font_color="red", font_size=8, ax=ax)

        # Wyświetlenie grafu
        for widget in graph_frame.winfo_children():
            widget.destroy()
        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        canvas.draw()

    # Funkcja do uruchamiania optymalizacji
    def run_optimization():
        energy_per_km = float(energy_consumption_entry.get())
        battery_capacity = float(battery_capacity_entry.get())
        initial_charge = float(initial_charge_entry.get())
        num_ants = int(num_ants_entry.get())
        num_iterations = int(iterations_entry.get())
        evaporation_rate = float(evaporation_rate_entry.get())
        alpha = float(alpha_entry.get())
        beta = float(beta_entry.get())
        penalty = float(penalty_entry.get())

        vehicle = ElectricVehicle(energy_per_km, battery_capacity, initial_charge)
        graph = Graph()
        for (start, end), distance in distances.items():
            graph.add_edge(start, end, distance)

        stations = {
            "B": ChargingStation("B", 10, 20, 0.5, 0.2, 50),
            "C": ChargingStation("C", 20, 30, 0.6, 0.1, 60),
            "D": ChargingStation("D", 30, 40, 0.4, 0.3, 55),
            "E": ChargingStation("E", 40, 50, 0.7, 0.2, 45),
        }

        aco = AntColonyOptimization(graph, vehicle, stations, num_ants, num_iterations,
                                     evaporation_rate, alpha, beta, penalty)
        best_route, best_score = aco.optimize(start_node="A", end_node="F")

        result_label.config(text=f"Najlepsza trasa: {best_route}\nNajlepszy wynik: {best_score:.2f}")

    # Przyciski
    graph_button = tk.Button(left_frame, text="Pokaż graf", command=show_graph)
    graph_button.grid(row=10, column=0, columnspan=2, pady=10, sticky="ew")

    optimize_button = tk.Button(left_frame, text="Uruchom optymalizację", command=run_optimization)
    optimize_button.grid(row=11, column=0, columnspan=2, pady=10, sticky="ew")

    root.mainloop()
