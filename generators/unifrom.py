from __future__ import annotations
from datetime import datetime
import math


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