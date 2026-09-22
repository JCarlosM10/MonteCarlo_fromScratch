from pathlib import Path
import os


PROJECT_DIR = Path(__file__).resolve().parent.parent
os.chdir(PROJECT_DIR)

from mc_continuo import decay
from graphs.animation.create_gif import create_gif


N_VALUES = [10, 20, 50, 100, 500, 1000, 10000]


def main() -> None:
    for n0 in N_VALUES:
        decay(n0)

    create_gif()


if __name__ == "__main__":
    main()
