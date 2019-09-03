from GasPowered import GasPowered

class PumpStation:

    def __init__(self):
        self.__vehicles = [] #two underscores makes not publicly accesible

    def add_vehicle(self, vehicle):
        #Only allow gas powered vehicles
        if isinstance(vehicle, GasPowered):
            self.__vehicles.append(vehicle)

        # if hasattr(vehicle, "fuel_level"):    This one is the worst. don't use. 
        #     self.__vehicles.append(vehicle)

        # try:
        #     if vehicle.fuel_level > -1 and vehicle.fuel_capacity:
        #         self.__vehicles.append(vehicle)
        # except AttributeError:
        #     print(f"THAT AINT NO DUCK!")