from vehicle import Vehicle
from ElectricPowered import ElectricPowered

class Leaf(Vehicle, ElectricPowered):
    def __init__(self):
        Vehicle.__init__(self, "Leaf", "Nissan", 200, 4)
        ElectricPowered.__init__(self, 50)

    def drive(self):
        ElectricPowered.drive(self, 1)
