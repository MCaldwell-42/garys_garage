class GasPowered:

    def __init__(self, capacity):
        self.fuel_capacity = capacity
        self.fuel_level = 0

    def drive(self, lowerby):
        self.fuel_level -= lowerby
        print(f'Oh Goood, You only have {self.fuel_level} gallons left.')

    def refuel(self):
        self.fuel_level = self.fuel_capacity