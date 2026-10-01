"""Tests for slab geometry."""

from mc.geometry.slab import Slab
from mc.particle.particle import Particle


def test_distance_to_right_boundary():
    slab = Slab(0.0, 10.0)
    p = Particle(x=2.0, direction=1, energy=1.0)

    assert slab.distance_to_boundary(p) == 8.0


def test_distance_to_left_boundary():
    slab = Slab(0.0, 10.0)
    p = Particle(x=2.0, direction=-1, energy=1.0)

    assert slab.distance_to_boundary(p) == 2.0
