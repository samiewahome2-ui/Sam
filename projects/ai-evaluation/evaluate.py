"""Summarize fictional human ratings; not an automated fact checker."""
import csv
from pathlib import Path

CRITERIA = ("accuracy", "adherence", "clarity")

def score(row):
    ratings = [int(row[key]) for key in CRITERIA]
    if any(value not in (0, 1, 2) for value in ratings):
        raise ValueError("Ratings must be 0, 1 or 2")
    critical = row["critical"].strip().lower()
    if critical not in ("yes", "no"):
        raise ValueError("Critical must be yes or no")
    total = sum(ratings)
    return total, "PASS" if total >= 5 and critical == "no" else "REVIEW"

def main():
    with Path(__file__).with_name("sample.csv").open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            total, decision = score(row)
            print(f"{row['case_id']}: {total}/6 | {decision}")

if __name__ == "__main__":
    main()
