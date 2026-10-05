"""Step 1: validate fictional inventory data and save below-threshold parts."""

import json
from pathlib import Path


# The input and output live beside this script, whichever folder you run it from.
PROJECT_FOLDER = Path(__file__).resolve().parent
INPUT_FILE = PROJECT_FOLDER / "inventory.json"
OUTPUT_FILE = PROJECT_FOLDER / "shortages.json"


def main():
    try:
        # 1. Read the JSON file.
        parts = json.loads(INPUT_FILE.read_text(encoding="utf-8-sig"))
        if not isinstance(parts, list) or not parts:
            raise ValueError("inventory.json must contain a nonempty list of parts.")

        shortages = []
        seen_part_numbers = set()

        for row, part in enumerate(parts, start=1):
            # 2. Check each record before using its numbers.
            if not isinstance(part, dict):
                raise ValueError(f"Record {row} must be a JSON object.")

            for field in ("partNumber", "supplier"):
                value = part.get(field)
                if not isinstance(value, str) or not value.strip():
                    raise ValueError(f"Record {row}: {field} must contain text.")

            number = part["partNumber"].strip()
            if number in seen_part_numbers:
                raise ValueError(f"Duplicate partNumber: {number}.")
            seen_part_numbers.add(number)

            for field in ("quantityOnHand", "reorderPoint", "leadTimeDays"):
                value = part.get(field)
                if type(value) is not int or value < 0:
                    raise ValueError(
                        f"{number}: {field} must be a whole number of 0 or more."
                    )

            # 3. Flag parts strictly below the reorder point.
            gap = part["reorderPoint"] - part["quantityOnHand"]
            if gap > 0:
                shortages.append({**part, "gapToReorderPoint": gap})

        # 4. Save results only after every input record passes validation.
        OUTPUT_FILE.write_text(
            json.dumps(shortages, indent=2) + "\n", encoding="utf-8"
        )

        # 5. Display a readable summary.
        print(f"Checked: {len(parts)} inventory records")
        print(f"Parts below reorder point: {len(shortages)}")
        total_gap = sum(part["gapToReorderPoint"] for part in shortages)
        print(f"Total gap to reorder points: {total_gap} units")
        print()
        for part in shortages:
            print(
                f"{part['partNumber']}: on hand {part['quantityOnHand']}, "
                f"reorder point {part['reorderPoint']}, "
                f"gap {part['gapToReorderPoint']}"
            )
        print("\nSaved: shortages.json")
        return 0

    except (OSError, ValueError) as error:
        print(f"ERROR: {error}")
        if OUTPUT_FILE.exists():
            print("The previous shortages.json was not refreshed. Fix the input and rerun.")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
