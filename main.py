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

    def travel_time(self):
        return f"{self.mileage // self.max_speed} hr"


class Bus(Vehicle):
    """
    This is a child class which inherits all properties and methods
    of its parent class and also adds a new property
    """
    def __init__(self, max_speed, mileage, seating_capacity=50):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity
