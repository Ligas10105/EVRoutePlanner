class ElectricVehicle:
    def __init__(self, energy_per_km, battery_capacity, initial_charge):
        self.energy_per_km = energy_per_km
        self.battery_capacity = battery_capacity
        self.charge = initial_charge
