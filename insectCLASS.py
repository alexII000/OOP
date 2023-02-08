import random


class Insect:

    def __init__(self):
        wings = 2
        legs = 4

    def flight(self):
        for randint in range(0, 11):
            self.flight_time = randint

    def get_flighttime(self):
        return self.flight_time
        # return self.wings
        # return self.legs
