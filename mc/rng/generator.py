MASK = (1 << 64) - 1
MULTIPLIER = 2685821657736338717



class XorShift64Star:

    def __init__(self, seed: int):
        if seed == 0:
            raise ValueError("Seed debe ser diferente de cero.")

        self.state = seed & MASK

    def next_uint64(self) -> int:
        x = self.state
        x ^= (x >> 12)
        x ^= (x << 25) & MASK
        x ^= (x >> 27)
        self.state = x & MASK
        return (x * MULTIPLIER) & MASK

    def random(self) -> float:
        # 53 bits → precisión aproximada de double
        value = self.next_uint64() >> 11
        return value / float(1 << 53)
