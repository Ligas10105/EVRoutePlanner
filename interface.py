import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from main import distances, nodes

# Inicjalizacja głównego okna
root = tk.Tk()
root.geometry("1200x600")
root.title("Ant Colony Optimization")

# Funkcja do ustawienia proporcji okien
def configure_grid_weights():
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=2)

# Ramka na lewą część (parametry)
left_frame = tk.Frame(root, bg="lightgray", padx=5, pady=5)
left_frame.grid(row=0, column=0, sticky="nsew")

# Ramka na prawą część (do wyświetlania grafu)
right_frame = tk.Frame(root, bg="white")
right_frame.grid(row=0, column=1, sticky="nsew")

# Etykieta tytułu
title_label = tk.Label(left_frame, text="Electronic Vehicle Route Planner", font=("Helvetica", 14), bg="lightgray")
title_label.grid(row=0, column=0, columnspan=2, pady=5)

# Funkcja do tworzenia pola wprowadzania z etykietą
def create_entry_field(parent, label_text, row, width=10):
    label = tk.Label(parent, text=label_text, bg="lightgray")
    label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
    entry = ttk.Entry(parent, width=width)
    entry.grid(row=row, column=1, padx=5, pady=5, sticky="w")
    return entry

# Parametry auta
car_params_label = tk.Label(left_frame, text="Parametry auta", font=("Helvetica", 12, "bold"), bg="lightgray")
car_params_label.grid(row=1, column=0, columnspan=2, sticky="w", pady=(10, 5))

energy_consumption_entry = create_entry_field(left_frame, "Zużycie energii na km:", row=2)
battery_capacity_entry = create_entry_field(left_frame, "Pojemność baterii:", row=3)
initial_battery_entry = create_entry_field(left_frame, "Początkowy poziom baterii:", row=4)

# Parametry grafu
graph_params_label = tk.Label(left_frame, text="Parametry grafu", font=("Helvetica", 12, "bold"), bg="lightgray")
graph_params_label.grid(row=5, column=0, columnspan=2, sticky="w", pady=(10, 5))

vertices_entry = create_entry_field(left_frame, "Ilość wierzchołków do wygenerowania:", row=6)
stations_entry = create_entry_field(left_frame, "Ilość stacji w grafie:", row=7)

# Parametry mrówek
ant_params_label = tk.Label(left_frame, text="Parametry mrówek", font=("Helvetica", 12, "bold"), bg="lightgray")
ant_params_label.grid(row=8, column=0, columnspan=2, sticky="w", pady=(10, 5))

num_ants_entry = create_entry_field(left_frame, "Ilość mrówek:", row=9)
iterations_entry = create_entry_field(left_frame, "Ilość iteracji:", row=10)
evaporation_entry = create_entry_field(left_frame, "Szybkość ewaporacji feromonów:", row=11)
pheromone_weight_entry = create_entry_field(left_frame, "Waga feromonów:", row=12)
heuristic_weight_entry = create_entry_field(left_frame, "Waga heurystyki:", row=13)
penalty_entry = create_entry_field(left_frame, "Kara za niedopuszczalne trasy:", row=14)

# Przyciski
buttons_frame = tk.Frame(left_frame, bg="lightgray", pady=10)
buttons_frame.grid(row=15, column=0, columnspan=2, pady=(20, 0))

show_graph_button = tk.Button(buttons_frame, text="Pokaż graf", bg="white", font=("Helvetica", 10), width=15)
show_graph_button.pack(side="left", padx=10)

test_button = tk.Button(buttons_frame, text="Test", bg="white", font=("Helvetica", 10), width=15)
test_button.pack(side="left", padx=10)

# Funkcja do wyświetlania grafu
def show_graph():
    # Sprawdzamy, czy graf już został wyświetlony
    for widget in right_frame.winfo_children():
        widget.destroy()  # Usuwamy poprzedni graf, jeśli istnieje

    G = nx.Graph()
    G.add_nodes_from(nodes)
    for (node1, node2), distance in distances.items():
        G.add_edge(node1, node2, weight=distance)

    edge_labels = nx.get_edge_attributes(G, "weight")
    
    pos = nx.spring_layout(G, seed=42)  # Układ wierzchołków
    fig, ax = plt.subplots(figsize=(6, 4))  # Tworzymy wykres

    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold", edge_color="gray", ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red", font_size=8, ax=ax)

    # Osadzanie wykresu na canvasie Tkinter
    canvas = FigureCanvasTkAgg(fig, master=right_frame)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    canvas.draw()

# Funkcja do konfiguracji siatki
configure_grid_weights()

# Łączenie funkcji do przycisku
show_graph_button.config(command=show_graph)

# Uruchomienie pętli aplikacji
root.mainloop()
