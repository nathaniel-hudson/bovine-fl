import numpy as np

from pathlib import Path

ROOT = Path("~/Research/Data/Wisconsin Cow Data/").expanduser()
PROCESSED_DIR = ROOT / "depth_processed"
RAW_DIR = ROOT / "depth_raw"
INFRA_DIR = ROOT / "infrared"


def load_processed_file(filename: str) -> dict[str, np.ndarray]:
    data: dict[str, np.ndarray] = {}
    with np.load(PROCESSED_DIR / filename, allow_pickle=True) as raw_data:
        errors = []
        for file in raw_data.files:
            try:
                data[file] = raw_data[file]
            except ValueError:
                errors.append(file)

        if errors:
            print(f"Had errors interacting with the following: {errors}")

    return data


def load_all_processed() -> dict[str, dict[str, np.ndarray]]:
    files = {}
    for f in PROCESSED_DIR.glob("*.npz"):
        files[f.stem] = load_processed_file(f.name)
    return files
