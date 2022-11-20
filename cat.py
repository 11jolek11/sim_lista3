import generators.unifrom as gen


class Carbon14:
    def __init__(self, accuracy) -> None:
        self.currentTimeInSimulation = 0
        self.halfLife = 5730
        self.oneStepTime = self.halfLife
        self.accuracyOfSimulation = accuracy

        for _ in range(accuracy):
            self.oneStepTime /= 2
    

class Cats:
    def __init__(self) -> None:
        self.generator = gen.LCG.generate()
        self.count = 0
        self.countliving = self.count
        self.livingtime = []

    def doonestep(self, atom:Carbon14):
        pass




if __name__ == '__main__':
    p = Cats()
