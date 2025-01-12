import tkinter as tk
from tkinter import ttk, filedialog
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from generated_graph import distances, nodes, stations
from src.ant_colony import AntColonyOptimization
from src.vehicle import ElectricVehicle
from src.graph import Graph
from src.ant_colony import AntColonyOptimization as aco

def main_window():
    root = tk.Tk()
    root.geometry("1200x800")
    root.title("Electric Vehicle Route Planner")

    # Create main layout frames
    left_frame = ttk.Frame(root, width=300, padding=10)
    left_frame.pack(side=tk.LEFT, fill=tk.Y)

    right_frame = ttk.Frame(root, padding=10)
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Create notebook for tabs in the left frame
    notebook = ttk.Notebook(left_frame)
    notebook.pack(fill=tk.BOTH, expand=True)

    # Tab 1: Graph Generation
    graph_tab = ttk.Frame(notebook)
    notebook.add(graph_tab, text="Graph Generation")

    # Tab 2: Optimization
    optimization_tab = ttk.Frame(notebook)
    notebook.add(optimization_tab, text="Optimization")

    # --- Right Panel for Graph and Results ---
    graph_and_results_frame = ttk.LabelFrame(right_frame, text="Graph and Results", padding=10)
    graph_and_results_frame.pack(fill=tk.BOTH, expand=True)

    def show_graph(G, route=None, pos=None):
        if pos is None:
            pos = nx.spring_layout(G, weight="distance", seed=42)

        # Tworzenie figury i osi
        fig, ax = plt.subplots(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold", edge_color="gray", ax=ax)

        if route:
            route_edges = list(zip(route[:-1], route[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=route_edges, edge_color="red", width=2.5, ax=ax)

        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red", font_size=8, ax=ax)

        for widget in graph_and_results_frame.winfo_children():
            widget.destroy()

        # Dodanie ramki przycisków u góry
        button_frame = ttk.Frame(graph_and_results_frame)
        button_frame.pack(side=tk.TOP, fill=tk.X, pady=5)

        # Dodanie przycisków ze strzałkami do przesuwania i przybliżania/oddalania
        ttk.Button(button_frame, text="←", command=lambda: move_view("left")).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="→", command=lambda: move_view("right")).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="↑", command=lambda: move_view("up")).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="↓", command=lambda: move_view("down")).pack(side=tk.LEFT, padx=5)

        ttk.Button(button_frame, text="Przybliż", command=lambda: zoom(0.8)).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Oddal", command=lambda: zoom(1.2)).pack(side=tk.LEFT, padx=5)

        canvas = FigureCanvasTkAgg(fig, master=graph_and_results_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)
        canvas.draw()

        # Funkcje do przesuwania widoku
        def move_view(direction):
            step_x = (ax.get_xlim()[1] - ax.get_xlim()[0]) * 0.1
            step_y = (ax.get_ylim()[1] - ax.get_ylim()[0]) * 0.1
            cur_xlim = ax.get_xlim()
            cur_ylim = ax.get_ylim()

            if direction == "up":
                ax.set_ylim([cur_ylim[0] + step_y, cur_ylim[1] + step_y])
            elif direction == "down":
                ax.set_ylim([cur_ylim[0] - step_y, cur_ylim[1] - step_y])
            elif direction == "left":
                ax.set_xlim([cur_xlim[0] - step_x, cur_xlim[1] - step_x])
            elif direction == "right":
                ax.set_xlim([cur_xlim[0] + step_x, cur_xlim[1] + step_x])

            canvas.draw()

        # Funkcja obsługująca przybliżanie i centrowanie grafu
        def zoom(scale_factor):
            cur_xlim = ax.get_xlim()
            cur_ylim = ax.get_ylim()

            # Wyliczanie nowej szerokości i wysokości
            new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
            new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor

            center_x = (cur_xlim[0] + cur_xlim[1]) / 2
            center_y = (cur_ylim[0] + cur_ylim[1]) / 2

            ax.set_xlim([center_x - new_width / 2, center_x + new_width / 2])
            ax.set_ylim([center_y - new_height / 2, center_y + new_height / 2])
            canvas.draw()

    def show_iteration_plot(iteration_scores, iteration_times, num_iterations, best_route, best_score, best_distance, unique_paths_per_iteration, average_scores_per_iteration, score_differences):
        new_window = tk.Toplevel()
        new_window.title("Optimization Progress")
        new_window.geometry("800x600")

        fig, ax = plt.subplots(4, 1, figsize=(8, 10))  # Dodajemy jeden wykres więcej

        # Wykres wyników
        ax[0].plot(range(1, len(iteration_scores) + 1), iteration_scores, marker='o', label="Best Score")
        ax[0].set_xlim(1, num_iterations)
        ax[0].set_title("Optimization Progress (Scores)")
        ax[0].set_xlabel("Iteration")
        ax[0].set_ylabel("Best Score")
        ax[0].grid(True)
        ax[0].legend()

        # Wykres czasów iteracji
        ax[1].plot(range(1, len(iteration_times) + 1), iteration_times, marker='o', color='orange', label="Iteration Time (s)")
        ax[1].set_xlim(1, num_iterations)
        ax[1].set_title("Iteration Times")
        ax[1].set_xlabel("Iteration")
        ax[1].set_ylabel("Time (s)")
        ax[1].grid(True)
        ax[1].legend()

        # Wykres liczby unikalnych tras
        ax[2].plot(range(1, len(unique_paths_per_iteration) + 1), unique_paths_per_iteration, marker='o', color='green', label="Unique Paths")
        ax[2].set_xlim(1, num_iterations)
        ax[2].set_title("Unique Paths per Iteration")
        ax[2].set_xlabel("Iteration")
        ax[2].set_ylabel("Unique Paths")
        ax[2].grid(True)
        ax[2].legend()

        # Wykres różnicy między średnim a najlepszym wynikiem
        ax[3].plot(range(1, len(score_differences) + 1), score_differences, marker='o', color='red', label="Score Difference (Best - Average)")
        ax[3].set_xlim(1, num_iterations)
        ax[3].set_title("Difference Between Best and Average Score")
        ax[3].set_xlabel("Iteration")
        ax[3].set_ylabel("Score Difference")
        ax[3].grid(True)
        ax[3].legend()

        canvas = FigureCanvasTkAgg(fig, master=new_window)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        canvas.draw()

        # Dodanie wyników
        result_frame = ttk.Frame(new_window, padding=10)
        result_frame.pack(fill=tk.BOTH, expand=True)
        ttk.Label(result_frame, text=f"Best Route: {best_route}", font=("Helvetica", 12), foreground="green").pack(anchor="w", pady=5)
        ttk.Label(result_frame, text=f"Best Score: {best_score:.2f}", font=("Helvetica", 12), foreground="green").pack(anchor="w", pady=5)
        ttk.Label(result_frame, text=f"Total Distance: {best_distance:.2f} km", font=("Helvetica", 12), foreground="green").pack(anchor="w", pady=5)


    # --- Graph Generation Tab ---
    def generate_graph():
        try:
            import subprocess
            subprocess.run(["python", "graph_generator.py"], check=True)
            result_label.config(text="Graph generated successfully!")
            update_graph()
        except subprocess.CalledProcessError as e:
            result_label.config(text=f"Error generating graph: {e}")

    def load_graph():
        global distances, nodes, stations, current_graph, current_pos
        file_path = filedialog.askopenfilename(title="Select Graph File", filetypes=[("Python Files", "*.py")])
        if file_path:
            try:
                imported_graph = {}
                exec(open(file_path).read(), {}, imported_graph)
                distances = imported_graph.get("distances", {})
                nodes = imported_graph.get("nodes", [])
                stations = imported_graph.get("stations", {})
                update_graph()
                result_label.config(text="Graph loaded successfully!")
            except Exception as e:
                result_label.config(text=f"Error loading graph: {e}")

    def update_graph():
        global current_graph, current_pos
        G = nx.Graph()
        G.add_nodes_from(nodes)
        for (node1, node2), distance in distances.items():
            G.add_edge(node1, node2, weight=distance)
        current_graph = G
        current_pos = nx.spring_layout(G, weight="distance", seed=42)
        show_graph(current_graph, pos=current_pos)

    graph_controls_frame = ttk.Frame(graph_tab, padding=10)
    graph_controls_frame.pack(fill=tk.BOTH, expand=True)

    ttk.Button(graph_controls_frame, text="Generate Graph", command=generate_graph).pack(fill=tk.X, pady=5)
    ttk.Button(graph_controls_frame, text="Load Graph from File", command=load_graph).pack(fill=tk.X, pady=5)
    ttk.Label(graph_controls_frame, text="Start Node:").pack(anchor="w", pady=5)
    start_node_entry = ttk.Entry(graph_controls_frame)
    start_node_entry.pack(fill=tk.X)
    ttk.Label(graph_controls_frame, text="End Node:").pack(anchor="w", pady=5)
    end_node_entry = ttk.Entry(graph_controls_frame)
    end_node_entry.pack(fill=tk.X)
    result_label = ttk.Label(graph_controls_frame, text="", foreground="blue")
    result_label.pack(anchor="w", pady=5)

    # Shared Reset Button
    def reset_all():
        # Reset entries and clear graph and results
        start_node_entry.delete(0, tk.END)
        end_node_entry.delete(0, tk.END)

        energy_consumption_entry.delete(0, tk.END)
        energy_consumption_entry.insert(0, "0.2")

        battery_capacity_entry.delete(0, tk.END)
        battery_capacity_entry.insert(0, "60")

        initial_charge_entry.delete(0, tk.END)
        initial_charge_entry.insert(0, "50")

        num_ants_entry.delete(0, tk.END)
        num_ants_entry.insert(0, "10")

        num_iterations_entry.delete(0, tk.END)
        num_iterations_entry.insert(0, "10")

        evaporation_rate_entry.delete(0, tk.END)
        evaporation_rate_entry.insert(0, "0.5")

        alpha_entry.delete(0, tk.END)
        alpha_entry.insert(0, "1")

        beta_entry.delete(0, tk.END)
        beta_entry.insert(0, "2")

        penalty_entry.delete(0, tk.END)
        penalty_entry.insert(0, "10")

        for widget in graph_and_results_frame.winfo_children():
            widget.destroy()

    ttk.Button(left_frame, text="Reset All", command=reset_all).pack(fill=tk.X, pady=10)

    # --- Optimization Tab ---
    def create_entry_field(parent, label_text, default_value):
        frame = ttk.Frame(parent)
        frame.pack(fill=tk.X, pady=5)
        ttk.Label(frame, text=label_text).pack(side=tk.LEFT)
        entry = ttk.Entry(frame)
        entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)
        entry.insert(0, default_value)
        return entry

    energy_consumption_entry = create_entry_field(optimization_tab, "Energy Consumption (kWh/km):", "0.2")
    battery_capacity_entry = create_entry_field(optimization_tab, "Battery Capacity (kWh):", "60")
    initial_charge_entry = create_entry_field(optimization_tab, "Initial Battery Level (kWh):", "50")
    num_ants_entry = create_entry_field(optimization_tab, "Number of Ants:", "10")
    num_iterations_entry = create_entry_field(optimization_tab, "Number of Iterations:", "10")
    evaporation_rate_entry = create_entry_field(optimization_tab, "Evaporation Rate:", "0.5")
    alpha_entry = create_entry_field(optimization_tab, "Pheromone Weight (Alpha):", "1")
    beta_entry = create_entry_field(optimization_tab, "Heuristic Weight (Beta):", "2")
    pheromone_importance_probability_entry = create_entry_field(optimization_tab, "Pheromone Importance Probability:", "0.8")
    penalty_entry = create_entry_field(optimization_tab, "Penalty for Invalid Routes:", "10")

    def run_optimization():
        try:
            # Pobieranie danych wejściowych
            energy_per_km = float(energy_consumption_entry.get())
            battery_capacity = float(battery_capacity_entry.get())
            initial_charge = float(initial_charge_entry.get())
            num_ants = int(num_ants_entry.get())
            num_iterations = int(num_iterations_entry.get())
            evaporation_rate = float(evaporation_rate_entry.get())
            alpha = float(alpha_entry.get())
            beta = float(beta_entry.get())
            pheromone_importance_probability = float(pheromone_importance_probability_entry.get())
            penalty = float(penalty_entry.get())
            start_node = start_node_entry.get()
            end_node = end_node_entry.get()

            vehicle = ElectricVehicle(energy_per_km, battery_capacity, initial_charge)

            # Tworzenie grafu
            graph = Graph()
            for (node1, node2), distance in distances.items():
                graph.add_edge(node1, node2, distance)

            aco = AntColonyOptimization(
                graph=graph,
                vehicle=vehicle,
                stations=stations,
                num_ants=num_ants,
                num_iterations=num_iterations,
                evaporation_rate=evaporation_rate,
                alpha=alpha,
                beta=beta,
                pheromone_importance_probability=pheromone_importance_probability,
                penalty=penalty
            )
            best_route, best_score, iteration_scores, iteration_times, best_distance, all_routes, average_scores_per_iteration, score_differences, avg_time_per_iteration, total_unique_paths = aco.optimize(start_node, end_node)

            # Wyświetlanie wyników
            show_graph(current_graph, best_route, pos=current_pos)
            show_iteration_plot(iteration_scores, iteration_times, num_iterations, best_route, best_score, best_distance, all_routes, average_scores_per_iteration, score_differences)

            result_text = (f"Best Route: {best_route}\n"
                        f"Best Score: {best_score:.2f}\n"
                        f"Total Distance: {best_distance:.2f} km\n"
                        f"Average Time per Iteration: {avg_time_per_iteration:.5f} s\n"
                        f"Total Unique Paths: {total_unique_paths}")

            # Usuwanie poprzednich etykiet w przypadku aktualizacji wyników
            for widget in graph_and_results_frame.winfo_children():
                if isinstance(widget, ttk.Label):
                    widget.destroy()

            # Tworzenie nowych etykiet z wynikami
            result_label = ttk.Label(graph_and_results_frame, text=result_text)
            result_label.pack()


        except Exception as e:
            ttk.Label(graph_and_results_frame, text=f"Error: {e}", font=("Helvetica", 12), foreground="red").pack(anchor="n", pady=5)



    ttk.Button(optimization_tab, text="Run Optimization", command=run_optimization).pack(fill=tk.X, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_window()