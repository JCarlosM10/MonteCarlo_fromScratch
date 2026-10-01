"""Minimal example: 1D slab transport."""
import matplotlib.pyplot as plt 
from mc.geometry.slab import Slab
from mc.physics.material import Material
from mc.rng.generator import XorShift64Star
from mc.source.source import FixedSource
from mc.tally.flux import FluxTally
from mc.simulation.simulation import Simulation


def main():
    geometry = Slab(0.0, 10.0)
    material = Material(sigma_a=0.5, sigma_s=0.5)

    rng = XorShift64Star(seed=123456789)

    source = FixedSource(
        position=1.0,
        direction=+1,
        energy=1.0,
    )

    tally = FluxTally(
        xmin=0.0,
        xmax=10.0,
        n_bins=100,
    )

    simulation = Simulation(
        source=source,
        geometry=geometry,
        material=material,
        rng=rng,
        tally=tally,
    )

    simulation.run(histories=10000)

    print(tally.flux(histories=10000))
    plt.plot(tally.flux(histories=10000))
    #plt.yscale('log')
    plt.show()




if __name__ == "__main__":
    main()
