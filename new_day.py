import os
import sys
from pathlib import Path


ROOT = Path(__file__).parent


def create_day(day_str: str) -> None:
    day_dir = ROOT / f"day_{day_str}"
    day_dir.mkdir(exist_ok=True)

    example_path = day_dir / "example.txt"
    input_path = day_dir / "input.txt"
    part_1_path = day_dir / "part_1.py"
    part_2_path = day_dir / "part_2.py"

    if not example_path.exists():
        example_path.write_text("", encoding="utf-8")

    if not input_path.exists():
        input_path.write_text("", encoding="utf-8")

    if not part_1_path.exists():
        part_1_path.write_text("", encoding="utf-8")

    if not part_2_path.exists():
        part_2_path.write_text("", encoding="utf-8")


def main() -> None:
    if len(sys.argv) >= 2:
        day_str = sys.argv[1]
    else:
        day_str = input("Enter day number (e.g. 1, 2, 10): ").strip()

    if not day_str.isdigit():
        print("Day must be a number, e.g. '1' or '10'.")
        sys.exit(1)

    create_day(day_str)


if __name__ == "__main__":
    main()
