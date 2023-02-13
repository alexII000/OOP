import random


class Insect:

    def __init__(self,n,w,l):
        self.name = n
        self.wing = w
        self.legs = l
        self.flight = 0

    def flight_length(self):
        self.flight = random.randint(1,10)

    def get_miles(self):
        return self.flight
        # return self.wings
        # return self.legs
