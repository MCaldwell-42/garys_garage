from mustang import Mustang
from dodge import Ram
from nissan import Leaf
from crosstrek import CrossTreck
from pumpstation import PumpStation
from chargingstation import ChargingStation

mustang = Mustang()
# mustang.refuel()
# mustang.drive()

goat = Ram()
# goat.refuel()
# goat.drive()

buzz = Leaf()
# buzz.refuel()
# buzz.drive()

buzz_growl = CrossTreck()
# buzz_growl.refuel()
# buzz_growl.drive()

gas_pump_station = PumpStation()
electric_charging_station = ChargingStation()


gas_pump_station.add_vehicle(mustang)
gas_pump_station.add_vehicle(goat)
gas_pump_station.add_vehicle(buzz)

