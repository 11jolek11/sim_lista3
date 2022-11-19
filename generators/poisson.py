from __future__ import annotations
import seaborn as sns
import matplotlib.pyplot as plt
import unifrom
import math
import numpy as np
import scipy.stats as stat


class PoissonKnuth:
    @classmethod
    def poisson(self, lambd:float=1):
        l, p, k, u = (-1)*math.e, 1, 0, None

        while p > l:
            k += 1
            u = unifrom.LCG.uniform()
            p = p*u
        return k - 1
