class ElectricVehicle:
    def __init__(self, max_range, energy_per_km, battery_capacity, initial_charge):
        self.max_range = max_range
        self.energy_per_km = energy_per_km
        self.battery_capacity = battery_capacity
        self.charge = initial_charge
