import math


def exponential(rng, rate:float) -> float:
    if rate <= 0:
        raise ValueError("Rate debe ser positivo.")

    u = rng.random()

    # Evitar log(0)
    while u == 0.0:
        u = rng.random()

    return -math.log(u) / rate