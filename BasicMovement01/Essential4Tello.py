from djitellopy import tello
from time import sleep
class Essential4Tello:
    def InitialTello(self):
        tl = tello.Tello()
        tl.connect()
        print("Battery: " . tl.get_battery())
        print("Temperature: " . tl.get_temperature())
        return tl