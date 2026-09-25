"""Representacion del estado de la partícula"""

from dataclasses import dataclass

@dataclass
class Particle:
    x : float
    direction : int
    energy : float
    alive : bool = True