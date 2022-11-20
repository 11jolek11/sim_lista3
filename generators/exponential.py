from __future__ import annotations
import seaborn as sns
import matplotlib.pyplot as plt
from generators import unifrom
import math
import numpy as np
import scipy.stats as stat

class ExpInverse:
    """Sample from exponential distr using inverse method"""
    
    @classmethod
    def exponential(self, lambd:float=1) -> float:
        u = unifrom.LCG.uniform()
        x = (math.log(1-u)/(lambd))*(-1)
        # x = (math.log(u)/(lambd))*(-1)

        return x


if __name__ == "__main__":
    temp = []
    for _ in range(1000):
        temp.append(ExpInverse.exponential())
    # print(temp)
    # sns.distplot(np.random.exponential(scale=1.0, size=1000), hist=False)
    # sns.distplot(stat.expon.rvs(0, 1, size=100000), hist=False)
    # sns.distplot(temp, hist=False)
    # X = stat.expon.rvs(0,1,1000) # 1000 zmiennyc Exp(1)
    X = temp
    plt.hist(X,bins=30,density = True)
    xs = np.linspace(0,5,100)
    plt.plot(xs,stat.expon.pdf(xs)) 
    plt.savefig('exp_test.png')
