from pathlib import Path
import re

from PIL import Image


SCRIPT_DIR = Path(__file__).resolve().parent
GRAPHS_DIR = SCRIPT_DIR.parent
OUTPUT_PATH = SCRIPT_DIR / "decay_continuo.gif"
FRAME_DURATION_MS = 1000


def frame_number(path: Path) -> int:
    match = re.search(r"_(\d+)\.png$", path.name)
    return int(match.group(1)) if match else 0


def create_gif() -> None:
    frame_paths = sorted(
        GRAPHS_DIR.glob("decay_continuo_*.png"),
        key=frame_number,
    )

    if not frame_paths:
        raise FileNotFoundError(f"No se encontraron imagenes PNG en {GRAPHS_DIR}")

    frames = [Image.open(path).convert("RGB") for path in frame_paths]
    try:
        frames[0].save(
            OUTPUT_PATH,
            save_all=True,
            append_images=frames[1:],
            duration=FRAME_DURATION_MS,
            loop=0,
        )
    finally:
        for frame in frames:
            frame.close()

    print(f"GIF creado: {OUTPUT_PATH}")
    print(f"Fotogramas: {len(frame_paths)}")


if __name__ == "__main__":
    create_gif()
