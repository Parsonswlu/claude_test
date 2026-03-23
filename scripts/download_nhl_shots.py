"""
Download the NHL Clean Shots Dataset (2020-21 to 2024-25) from Kaggle.

Dataset: https://www.kaggle.com/datasets/samuarg/nhl-clean-shots-data-2020-2021-to-2024-2025

Prerequisites:
    1. Install the kaggle CLI:   pip install kaggle
    2. Create a Kaggle API token at https://www.kaggle.com/settings → Account → API
    3. Place kaggle.json in ~/.kaggle/kaggle.json  (chmod 600)

Usage:
    python scripts/download_nhl_shots.py
    python scripts/download_nhl_shots.py --dest data/raw/nhl_shots
"""

import argparse
import subprocess
import sys
import zipfile
from pathlib import Path


DATASET = "samuarg/nhl-clean-shots-data-2020-2021-to-2024-2025"
DEFAULT_DEST = Path(__file__).parent.parent / "data" / "raw" / "nhl_shots"


def check_kaggle_cli():
    try:
        subprocess.run(["kaggle", "--version"], check=True, capture_output=True)
    except FileNotFoundError:
        print("ERROR: kaggle CLI not found. Install it with:  pip install kaggle")
        sys.exit(1)
    except subprocess.CalledProcessError:
        print("ERROR: kaggle CLI failed. Check your installation.")
        sys.exit(1)


def check_credentials():
    cred_path = Path.home() / ".kaggle" / "kaggle.json"
    if not cred_path.exists():
        print(
            "ERROR: Kaggle API credentials not found.\n"
            "  1. Go to https://www.kaggle.com/settings → Account → API → Create New Token\n"
            f"  2. Move the downloaded kaggle.json to {cred_path}\n"
            "  3. Run: chmod 600 ~/.kaggle/kaggle.json"
        )
        sys.exit(1)


def download(dest: Path):
    dest.mkdir(parents=True, exist_ok=True)

    print(f"Downloading dataset '{DATASET}' → {dest}")
    result = subprocess.run(
        ["kaggle", "datasets", "download", "-d", DATASET, "-p", str(dest)],
        capture_output=False,
    )
    if result.returncode != 0:
        print("ERROR: Download failed. Check the error above.")
        sys.exit(1)

    # Unzip any downloaded zip files
    for zip_path in dest.glob("*.zip"):
        print(f"Extracting {zip_path.name} ...")
        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extractall(dest)
        zip_path.unlink()
        print(f"  Removed {zip_path.name}")

    csv_files = list(dest.glob("**/*.csv"))
    print(f"\nDone. {len(csv_files)} CSV file(s) in {dest}:")
    for f in csv_files:
        size_mb = f.stat().st_size / 1_048_576
        print(f"  {f.name}  ({size_mb:.1f} MB)")


def main():
    parser = argparse.ArgumentParser(description="Download NHL shots dataset from Kaggle")
    parser.add_argument(
        "--dest",
        type=Path,
        default=DEFAULT_DEST,
        help=f"Destination directory (default: {DEFAULT_DEST})",
    )
    args = parser.parse_args()

    check_kaggle_cli()
    check_credentials()
    download(args.dest)


if __name__ == "__main__":
    main()
