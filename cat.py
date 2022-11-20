import generators.unifrom as gen
# import generators.poisson as gen


class Carbon14:
    def __init__(self, accuracy) -> None:
        self.currentTimeInSimulation = 0
        self.halfLife = 5730
        self.oneStepTime = self.halfLife
        self.accuracyOfSimulation = accuracy

        for _ in range(accuracy):
            self.oneStepTime /= 2
    

class Cats:
    def __init__(self, count) -> None:
        self.generator = gen.LCG()
        self.count = count
        self.countliving = self.count
        self.livingtime = []

    def doonestep(self, atom:Carbon14):
        for i in range(int(self.countliving)):
            constant = 2 ** 16 - atom.accuracyOfSimulation
            support_gen = self.generator.generate()
            if support_gen < constant:
                self.countliving -= 1
                print("Still alive: " + str(self.countliving) + " After: " + str(atom.currentTimeInSimulation))
                self.livingtime.append(atom.currentTimeInSimulation)
        
        atom.currentTimeInSimulation += atom.oneStepTime

def Zad1():
    wegiel = Carbon14(16)
    catnumber = 1000
    pValue = 65
    symulacja = Cats(catnumber)
    symulacja.generator.a = 75
    symulacja.generator.c = 74
    symulacja.generator.m = 1 + 2 ** 16
    symulacja.generator.seed = 62

    while symulacja.countliving > catnumber /100 * 65:
        symulacja.doonestep(wegiel)

    






if __name__ == '__main__':
    Zad1()
