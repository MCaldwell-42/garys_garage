from ElectricPowered import ElectricPowered

class ChargingStation:

    def __init__(self):
        self.__vehicles = [] #two underscores makes not publicly accesible

    def add_vehicle(self, vehicle):
        #Only allow gas powered vehicles
        if isinstance(vehicle, ElectricPowered):
            self.__vehicles.append(vehicle)

        # if hasattr(vehicle, "charge_level"):    This one is the worst. don't use. 
        #     self.__vehicles.append(vehicle)

        # try:
        #     if vehicle.charge_level > -1 and vehicle.charge_capacity:
        #         self.__vehicles.append(vehicle)
        # except AttributeError:
        #     print(f"THAT AINT NO DUCK!")