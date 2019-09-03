class ElectricPowered:

    def __init__(self, capacity):
        self.battery_capacity = capacity
        self.battery_level = 0

    def drive(self, lowerby):
        self.battery_level -= lowerby
        print(f'Oh Goood, You only have {self.battery_level} kw/hr left.')

    def refuel(self):
        self.battery_level = self.battery_capacity