def calculate_travel_time(distance, difficulty, base_speed=60):
    speed = base_speed / difficulty
    return distance / speed

def calculate_charging_cost(required_energy, price_per_kwh):
    return required_energy * price_per_kwh

def calculate_charging_time(required_energy, max_power):
    return required_energy / max_power

def is_reachable(current_charge, distance, energy_per_km):
    return current_charge >= distance * energy_per_km

def calculate_energy_deficit(current_charge, distance, energy_per_km):
    required_energy = distance * energy_per_km
    return max(0, required_energy - current_charge)