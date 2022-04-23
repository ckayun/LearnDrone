from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())
print(me.get_temperature())
me.takeoff()
me.rotate_clockwise(180)
me.rotate_counter_clockwise(180)
me.land()
print(me.get_battery())
print(me.get_temperature())
print(me.get_flight_time())