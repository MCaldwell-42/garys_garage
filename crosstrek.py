from vehicle import Vehicle
from GasPowered import GasPowered
from ElectricPowered import ElectricPowered


class CrossTreck(Vehicle, ElectricPowered, GasPowered):
    def __init__(self):
        ElectricPowered.__init__(self, 40)
        GasPowered.__init__(self, 6)
        Vehicle.__init__(self, "Subaru", "Crosstrek", 60, 4)

    def drive(self):
        ElectricPowered.drive(self, 2)
        GasPowered.drive(self, 0.5)

    def refuel(self):
        ElectricPowered.refuel(self)
        GasPowered.refuel(self)