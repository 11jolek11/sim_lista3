import math
import random
import matplotlib.pyplot as plt


class Simulation:
    # czas oblugi - wykladniczy
    # przychodzenie - poisson 0.1/min
    # 1 klient na 10 minut (0.1*10)
    def __init__(self, queue_mean: float = 0.1, simulation_time: int = 180, interval: int = 1,
                 handle_time: int = 8) -> None:
        self.queue_mean = queue_mean
        self.interval = interval
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
        t, x, y = 0, 0, 0
        while not y < x:
            t = random.uniform(0, 36)
            x = _lambda * math.exp(-_lambda * t)
            y = random.uniform(0, _lambda)
        return t

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


if __name__ == '__main__':
    sim_time = 3600
    sim = Simulation(simulation_time=sim_time)
    data = sim.service()
    plt.hist(data['wait_time'], bins=30)
    plt.ylabel('ilość powtórzeń')
    plt.xlabel('Czas oczekiwania')
    plt.show()
    print(data)
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