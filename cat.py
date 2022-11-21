import generators.unifrom as gen
import math
import random
import matplotlib.pyplot as plt
import numpy as np

# import generators.poisson as gen


class Carbon14:
    def __init__(self, accuracy) -> None:
        self.currentTimeInSimulation = 0
        self.halfLife = 5730
        self.oneStepTime = self.halfLife
        self.accuracyOfSimulation = accuracy

        for _ in range(accuracy):
            self.oneStepTime /= 2
    

res_holder = []

class Cats:
    def __init__(self, count) -> None:
        self.generator = gen.LCG()
        self.count = count
        self.countliving = self.count
        self.livingtime = []

    def forward(self, atom:Carbon14):
        for i in range(int(self.countliving)):
            constant = 2 ** 16 - atom.accuracyOfSimulation
            support_gen = self.generator.generate()
            if support_gen < constant:
                self.countliving -= 1
                # print(str(self.countliving) + " " + str(atom.currentTimeInSimulation))
                res_holder.append((self.countliving, atom.currentTimeInSimulation))
                self.livingtime.append(atom.currentTimeInSimulation)
        
        atom.currentTimeInSimulation += atom.oneStepTime

def Zad1():
    wegiel = Carbon14(16)
    catnumber = 1000
    symulacja = Cats(catnumber)
    symulacja.generator.a = 75
    symulacja.generator.c = 74
    symulacja.generator.m = 1 + 2 ** 16
    symulacja.generator.seed = 62

    while symulacja.countliving > catnumber /100 * 65:
        symulacja.forward(wegiel)
    print(res_holder[-1])

    



# ???
# def gen_z1(half_life: int | float) -> list:
#     _lambda = math.log(2) / half_life  # ln
#     # http://hyperphysics.phy-astr.gsu.edu/hbase/Nuclear/meanlif.html
#     # normalizacja - lambda = ln(2)/hl
#     # p(t) = e^-(lambda*t) [0-inf) - p-stwo ze czastka przetrwa tyle czasu
#     # 1 - p(t) - p-stwo ze sie rozpadnie
#     # t = random.uniform(0, float('inf'))
#     # F^-1(t) = -ln(1-t)/lambda
#     sample = []
#     for _ in range(10000):
#         prob = random.uniform(0, 1)
#         sample.append(-math.log(prob) / _lambda)
#     return sample


def z1_helper(half_life: int | float) -> list[int]:
    # 3561 lat
    # f(t) = lambda*e^-(lambda*t)
    # F(t) = 1-e^(-lambda*t)

    # http://hyperphysics.phy-astr.gsu.edu/hbase/Nuclear/meanlif.html
    _lambda = math.log(2) / half_life  
    data: list[int] = []
    for i in range(20000):
        t = y = x = 0
        while not y < x:
            t = random.randint(0, 51000)
            x = _lambda * math.exp(-_lambda * t)
            y = random.uniform(0, _lambda)
            # y = _lambda
        data.append(t)
        # print(data)
    return data

def z1_simu():
    dist = z1_helper(5730)
    dist_normalized = [s*math.log(2)/5370 for s in dist]
    bins_count = 100
    scaled_data = np.histogram(dist, bins=bins_count, density=True)
    counts, bins = scaled_data[1], (scaled_data[0] * 5730 / math.log(2))
    plt.bar(counts[:-1], bins, 51000 / bins_count)
    plt.ylabel('p-stwo')
    plt.xlabel('czas')
    plt.savefig('test1.png')
    plt.hist(dist_normalized, bins=30, density=True)
    plt.savefig('test2.png')
    closest = min(zip(counts[:-1], bins), key=lambda x: abs(x[1] - 0.65))
    print(closest)


if __name__ == '__main__':
    z1_simu()
    # Zad1()





# if __name__ == '__main__':
    # Zad1()
