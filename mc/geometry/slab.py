"""One-Dimesional geometry"""

from dataclasses import dataclass


@dataclass
class Slab:

    xmin: float
    xmax: float

    def __post_init__(self):
        if self.xmax <= self.xmin:
            raise ValueError('xmax debe ser mayor que xmin')

    def contains(self, x) -> bool:
        return self.xmin <= x <= self.xmax

    def distance_to_boundary(self, Particle) -> float:
        if Particle.direction > 0:
            return self.xmax - Particle.x
        if Particle.direction < 0:
            return Particle.x - self.xmin
        raise ValueError('La dirección de la partícula debe ser +1 o -1')