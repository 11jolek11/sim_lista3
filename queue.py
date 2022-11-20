import numpy as np
from generators.poisson import PoissonKnuth
from generators.exponential import ExpInverse



class Simulation:
    def __init__(self) -> None:
        self.num_in_system = 0

        self.clock = 0.0
        self.t_arrival = self.generate_interarrival()
        self.t_depart = float('inf')

        self.num_arrivals = 0
        self.num_departs = 0
        self.total_wait = 0.0


    def generate_interarrival(self):
        return PoissonKnuth.poisson(0.1)

    def genrate_service(self):
        return ExpInverse.exponential(8)

    def advance_time(self):
        t_event = min(self.t_arrival, self.t_depart)
        self.total_wait += self.num_in_system*(t_event-self.clock)

        self.clock = t_event

        if self.t_arrival <= self.t_depart:
            self.handle_arrival_event()
        else:
            self.handle_departure_event()

    def handle_arrival_event(self):
        self.num_in_system += 1
        self.num_arrivals += 1
        if self.num_in_system <= 1:
            self.t_depart = self.clock + self.genrate_service()
        self.t_arrival = self.clock + self.generate_interarrival()

    def handle_departure_event(self):
        self.num_in_system -= 1
        self.num_departs += 1
        if self.num_in_system > 0:
            self.t_depart = self.clock + self.genrate_service()
        else:
            self.t_depart = float('inf')

if __name__ == '__main__':
    s = Simulation()
