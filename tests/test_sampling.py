"""Tests for probability distributions."""

from mc.rng.generator import XorShift64Star
from mc.rng.distributions import exponential


def test_exponential_mean():
    rng = XorShift64Star(123456789)

    rate = 2.0
    n = 100000

    samples = [exponential(rng, rate) for _ in range(n)]
    mean = sum(samples) / n

    # Monte Carlo tolerance; this is a statistical test.
    assert abs(mean - 1.0 / rate) < 0.01
