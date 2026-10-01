"""Tests for interaction sampling."""

from mc.physics.interactions import sample_collision
from mc.physics.material import Material
from mc.rng.generator import XorShift64Star


def test_absorption_fraction():
    rng = XorShift64Star(1234567891)
    val=0.4
    material = Material(sigma_a=val, sigma_s=(1.0-val))

    n = 100000
    absorptions = sum(
        sample_collision(rng, material) == "absorption"
        for _ in range(n)
    )

    fraction = absorptions / n

    assert abs(fraction - val) < 0.01

    return fraction

print(test_absorption_fraction())
