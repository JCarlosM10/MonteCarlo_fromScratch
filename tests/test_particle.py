"""Tests for particle state."""

from mc.particle.particle import Particle


def test_particle_defaults():
    p = Particle(x=1.0, direction=1, energy=2.0)

    assert p.x == 1.0
    assert p.direction == 1
    assert p.energy == 2.0
    assert p.alive is True
