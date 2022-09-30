class Vehicle:
    """
    This is the blueprint to create Vehicle and the method to
    measure its travelled time by giving speed and mileage

    Args:
        max_speed: The maximum and constant travelling speed (km/hr)
        mileage: The passed mileage (km)
    """

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return capacity

    def travel_time(self):
        return f"{self.mileage // self.max_speed} hr"


class Bus(Vehicle):
    """
    This is a child class which inherits all properties and methods
    of its parent class and also adds a new property
    """
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

