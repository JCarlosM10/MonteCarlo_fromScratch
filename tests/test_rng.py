"""Tests for the project RNG."""

import numpy as np
import matplotlib.pyplot as plt
from mc.rng.generator import XorShift64Star

semilla=123456789

def test_rng_range(seed:int):
    rng = XorShift64Star(seed)

    values = [rng.random() for _ in range(1000000)]
    return values


def test_rng_reproducibility(seed):
    rng1 = XorShift64Star(seed)
    rng2 = XorShift64Star(seed)

    #assert
    if [rng1.random() for _ in range(100)] != [
        rng2.random() for _ in range(100)
    ]:
        print('Discrepancia en las salidas de la funion random para la misma semilla')


th_mean = 1/2
th_var = 1/12
test_rng_reproducibility(semilla)
rng = np.array(test_rng_range(semilla))
print(f'Promedio semilla: {np.mean(rng):.6}')
print(f'Varianza semilla: {np.var(rng):.6}')
print(f'Promedio teórico: {th_mean:.6}')
print(f'Varianza teórica: {th_var:.6}')
print ('---------------------------------')
print(f'Error en promedio = {np.abs(np.mean(rng) - th_mean):.6}')
print(f'Error en varianza = {np.abs(np.var(rng) - th_var):.6}')
plt.hist(rng, bins=100)
plt.show()