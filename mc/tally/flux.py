import numpy as np


class FluxTally:

    def __init__(self, xmin:float, xmax:float, n_bins:int):

        if xmax <= xmin:
            raise ValueError('xmax debe ser mayor a xmin')
        if n_bins <= 0:
            raise ValueError('n_bins debe ser mayor que cero')

        self.xmin = xmin
        self.xmax = xmax
        self.n_bins = n_bins
        self.width = (xmax - xmin) / n_bins
        self.track_length = np.zeros(n_bins, dtype=float)

    def score_track(self, x0:float, x1:float):

        # Primera versión:
        # asumimos que el segmento pertenece a una sola celda.

        midpoint = 0.5 * (x0 + x1)

        index = int((midpoint - self.xmin) / self.width)

        if 0 <= index < self.n_bins:

            self.track_length[index] += abs(x1 - x0)

    def flux(self, histories:int):
        if histories <= 0:
            raise ValueError('histories debe ser mayor que cero')
        return (self.track_length / (histories * self.width))