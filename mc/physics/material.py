from dataclasses import dataclass


@dataclass
class Material:

    sigma_a: float
    sigma_s: float

    def __post_init__(self):
        if self.sigma_a < 0 or self.sigma_s < 0:
            raise ValueError('la seccion eficáz debe ser positiva')
        if self.sigma_t < 0:
            raise ValueError('La sección eficáz total debe ser positiva')


    @property
    def sigma_t(self) -> float:
        return self.sigma_a + self.sigma_s