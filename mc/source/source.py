#from . import __name__

class FixedSource:
    def __init__(self, position:float, direction:int, energy:float):
        self.position = position
        self.direction = direction
        self.energy = energy

    def sample(self):
        from mc.particle.particle import Particle

        return Particle(
            x = self.position,
            direction = self.direction,
            energy = self.energy
        )