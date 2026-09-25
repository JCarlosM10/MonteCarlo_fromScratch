from mc.rng.distributions import exponential

def sample_free_path(rng, material):
    return exponential(rng, material.sigma_t)

def sample_collision(rng, material):
    xi = rng.random()
    if xi < material.sigma_a / material.sigma_t:
        return "absorption"
    return "scattering"

def scatter(rng):
    if rng.random() < 0.5:
        return +1
    return -1