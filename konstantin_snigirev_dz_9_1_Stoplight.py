import time
class TrafficLight:


    def __init__(self, colour):
        self.colour = colour


    def lights(self):
        print(self.colour)


red = TrafficLight('Red')
red.lights()
time.sleep(7)

yellow = TrafficLight('Yellow')
yellow.lights()
time.sleep(2)

green = TrafficLight('Green')
green.lights()
time.sleep(7)
print('\nEnd of TrafficLight Program')


