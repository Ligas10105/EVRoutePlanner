class ChargingStation:
    def __init__(self, id, x, y, price_per_kwh, queue_time, max_power):
        self.id = id
        self.x = x
        self.y = y
        self.price_per_kwh = price_per_kwh
        self.queue_time = queue_time
        self.max_power = max_power