"""Monte carlo simulation driver"""

from mc.transport.transport import transport

class Simulation:

    def __init__(self, source, geometry, material, rng, tally):
        self.source = source
        self.geometry = geometry
        self.material = material
        self.rng = rng
        self.tally = tally

    def run(self, histories : int):
        if histories <= 0:
            raise ValueError('histories debe ser positivo')

        for _ in range(histories):
            particle = self.source.sample()
            transport(
                particle,
                self.geometry,
                self.material,
                self.rng,
                self.tally
            )
