import numpy as np
import math
import random

def poisson(queue_mean) -> int:
    k, x, y = 0, 0, 0
    while not y < x:
        k = random.randint(0, 20)
        x = (queue_mean ** k) * (math.e ** -queue_mean) / math.factorial(k)
        y = random.uniform(0, 1)
    return k
def exponential(handle_time) -> int:
    # 1/lambda = 8min
    # lambda e ^ - (lambda * t)
    # lambda = 0.125
    _lambda = 1 / handle_time
    return -math.log(np.random.uniform(0, 1)) / _lambda



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
        return poisson(0.1)

    def genrate_service(self):
        return exponential(8)

    def advance_time(self):
        t_event = min(self.t_arrival, self.t_depart)
        self.total_wait += self.num_in_system*(t_event-self.clock)
        print(self.total_wait)

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

    for _ in range(10):
        s.advance_time()