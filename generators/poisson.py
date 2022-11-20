from __future__ import annotations
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

# from ..generators import unifrom
# from generators import unifrom
import math
import numpy as np
import scipy.stats as stat

class LCG:
    "LCG generator implemented using classmethods"
    seed = int(datetime.now().timestamp() * 10003)
    x = seed
    a = 22695477
    c = 1
    m = 2 ** 32

    @classmethod
    def _seed(cls, seed: int) -> None:
        # set_seed
        cls.seed = seed
        cls.x = seed

    @classmethod
    def generate(cls) -> float:
        # random
        cls.x = (cls.a * cls.x + cls.c) % cls.m
        return cls.x

    @classmethod
    def uniform(cls) -> float:
        # uniform
        # [0, 1)
        return cls.generate() / cls.m

    @classmethod
    def uniform_range(cls, a: float, b: float) -> float:
        # uniform_range
        # [a, b)
        return (b - a) * cls.uniform() + a

    @classmethod
    def uniform_int(cls, a: int, b: int) -> int:
        # randint
        # [a, b]
        return math.floor(abs(b - a + 1) * cls.uniform() + a)




class PoissonKnuth:
    @classmethod
    def poisson(self, lambd:float=1):
        l, p, k, u = (-1)*math.e, 1, 0, None

        while p > l:
            k += 1
            u = LCG.uniform()
            p = p*u
        return k - 1

if __name__ == '__main__':
    temp = []
    for _ in range(1000):
        temp.append(PoissonKnuth.poisson())
        # print(temp)
        # sns.distplot(np.random.exponential(scale=1.0, size=1000), hist=False)
        # sns.distplot(stat.expon.rvs(0, 1, size=100000), hist=False)
        # sns.distplot(temp, hist=False)
        # X = stat.expon.rvs(0,1,1000) # 1000 zmiennyc Exp(1)
    X = temp
    plt.hist(X,bins=30,density = True)
    xs = np.linspace(0,5,100)
    plt.plot(xs,stat.poisson.pdf(xs)) 
    plt.savefig('poi_test.png')