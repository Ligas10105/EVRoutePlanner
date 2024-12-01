from src.util_functions import calculate_charging_cost, calculate_charging_time, calculate_energy_deficit, calculate_travel_time, is_reachable

def objective_function(routes, vehicle, stations, graph, penalty=1000):
    """
    Funkcja celu optymalizująca trasę z uwzględnieniem kary za niedopuszczalne rozwiązania.
    :param routes: Lista tras do analizy.
    :param vehicle: Obiekt pojazdu elektrycznego.
    :param stations: Słownik stacji ładowania.
    :param graph: Obiekt grafu.
    :param penalty: Wartość kary za niedopuszczalną trasę.
    """
    best_route = None
    best_score = float('inf')

    for route in routes:
        print(f"\nAnalizowana trasa: {route}")
        total_time = 0
        total_cost = 0
        current_charge = vehicle.charge
        feasible = True  # Zmienna określająca dopuszczalność trasy

        for i in range(len(route) - 1):
            point_i = route[i]
            point_j = route[i + 1]
            edge_data = graph.edges.get(point_i, {}).get(point_j)

            if edge_data is None:
                print(f"Brak krawędzi między {point_i} a {point_j}")
                feasible = False
                break

            distance = edge_data["distance"]
            difficulty = edge_data["difficulty"]

            # Oblicz czas przejazdu
            travel_time = calculate_travel_time(distance, difficulty)
            total_time += travel_time
            energy_needed = distance * vehicle.energy_per_km
            print(f"Przejazd {point_i} -> {point_j}: {distance} km, trudność {difficulty}, czas {travel_time:.2f} h, "
                  f"zużycie energii {energy_needed:.2f} kWh")

            # Sprawdź, czy pojazd musi się ładować
            if not is_reachable(current_charge, distance, vehicle.energy_per_km):
                deficit = calculate_energy_deficit(current_charge, distance, vehicle.energy_per_km)
                station = stations.get(point_i)

                if station:
                    charging_time = calculate_charging_time(deficit, station.max_power)
                    charging_cost = calculate_charging_cost(deficit, station.price_per_kwh)
                    total_time += charging_time
                    total_cost += charging_cost
                    current_charge += deficit
                    print(f"Ładowanie w {point_i}: potrzeba {deficit:.2f} kWh, czas {charging_time:.2f} h, koszt {charging_cost:.2f} zł")
                else:
                    print(f"Brak stacji ładowania w {point_i}. Niedopuszczalna trasa.")
                    feasible = False
                    break

            # Zaktualizuj poziom baterii po przejeździe
            current_charge -= energy_needed
            print(f"Pozostały poziom baterii: {current_charge:.2f} kWh")

        # Oblicz wynik dla trasy
        score = total_time * 0.75 + total_cost * 0.25
        if not feasible:
            score += penalty  # Dodaj karę za niedopuszczalną trasę

        print(f"Całkowity czas: {total_time:.2f} h, koszt: {total_cost:.2f} zł, wynik: {score:.2f}")

        if score < best_score:
            best_route = route
            best_score = score

    return best_route, best_score
