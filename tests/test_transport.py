"""Basic transport smoke test."""

from mc.geometry.slab import Slab
from mc.physics.material import Material
from mc.rng.generator import XorShift64Star
from mc.source.source import FixedSource
from mc.tally.flux import FluxTally
from mc.simulation.simulation import Simulation


def test_transport_runs():
    geometry = Slab(0.0, 1.0)
    material = Material(sigma_a=1.0, sigma_s=0.0)
    rng = XorShift64Star(123456789)

    source = FixedSource(0.0, +1, 1.0)
    tally = FluxTally(0.0, 1.0, 10)

    sim = Simulation(source, geometry, material, rng, tally)
    sim.run(100)

    assert tally.track_length.sum() > 0.0
