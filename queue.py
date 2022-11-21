import math
import random
from statistics import mean
import matplotlib.pyplot as plt
import numpy as np
# https://timeseriesreasoning.com/contents/poisson-process/

class Simulation:
    def __init__(self, queue_mean: float = 0.1, simulation_time: int = 180, clock_step: int = 1,
                 handle_time: int = 8) -> None:
        self.queue_mean = queue_mean
        self.interval = clock_step
        self.simulation_time = simulation_time
        self.handle_time = handle_time
        self.wait_time = 0

    def poisson(self) -> int:
        k, x, y = 0, 0, 0
        while not y < x:
            k = random.randint(0, 20)
            x = (self.queue_mean ** k) * (math.e ** -self.queue_mean) / math.factorial(k)
            y = random.uniform(0, 1)
        return k

    def exponential(self) -> int:
        # 1/lambda = 8min
        # lambda e ^ - (lambda * t)
        # lambda = 0.125
        _lambda = 1 / self.handle_time
        return -math.log(np.random.uniform(0, 1)) / _lambda
        # t, x, y = 0, 0, 0
        # while not y < x:
        #     t = random.uniform(0, 36)
        #     x = _lambda * math.exp(-_lambda * t)
        #     y = random.uniform(0, _lambda)
        # return t

    def service(self) -> dict:
        # 1 klient na 8 min
        _queue = {}
        wait_times = []
        client_count = []
        cur_time = 0
        for _ in range(0, self.simulation_time, self.interval):
            # co 1 min
            clients = self.poisson()
            handle_times = [self.exponential() for _ in range(clients)]
            if clients:
                for time in handle_times:
                    wait_times.append(cur_time)
                    cur_time += time
            cur_time = max(0, cur_time - self.interval)
            client_count.append((clients, handle_times))
        _queue['clients'] = client_count
        _queue['wait_time'] = wait_times
        return _queue

def runSimulation(sim_time=3600):
    sim = Simulation(simulation_time=sim_time)
    data = sim.service()
    plt.hist(data['wait_time'], bins=30)
    plt.ylabel('ilość powtórzeń')
    plt.xlabel('Czas oczekiwania')
    plt.show()
    # print(data)
    clients_data = data['clients']
    clients_time = []
    for _x in clients_data:
        clients_time += _x[1]
    plt.hist(clients_time, bins=30)
    plt.ylabel('ilość powtórzeń')
    plt.xlabel('Czas obsługi klienta')
    plt.show()
    print(f'Średni czas oczekiwania: {sum(data["wait_time"]) / len(data["wait_time"])}')
    print(f'Średni czas obsługi klienta: {sum(clients_time) / len(clients_time)}')
    print(f'ilość klientów na {sim_time} minut: {len(data["wait_time"])}')

def simulate(clients):
    def expr(lam):
        return -math.log(np.random.uniform(0, 1)) / lam


    awaiting_time = []

    service = clients*[0]
    for i in range(clients):
        service[i] = expr(8)
    print(service)

    arrival = clients*[0]
    for i in range(1, clients):
        arrival[i] = arrival[i-1] + expr(0.1)
    enter_service_time, leave_service_time = clients*[0], clients*[0]
    leave_service_time[0] = service[0]

    for i in range(1, clients):
        if leave_service_time[i-1] < arrival[i]:
            enter_service_time[i] = arrival[i]
            awaiting_time.append(0)
        else:
            awaiting_time.append(leave_service_time[i-1] - arrival[i])

            enter_service_time[i] = leave_service_time[i-1]
        leave_service_time[i] = enter_service_time[i] + service[i]

    print(f"Średni czas obsługi klienta: {mean(service)}")
    print(f'Średni czas oczekiwania klienta: {mean(awaiting_time)}')

if __name__ == '__main__':
    # runSimulation()
    simulate(10000)