import pathlib
import pandas as pd

INPUT  = pathlib.Path("data/transformed/events.csv")
OUTPUT = pathlib.Path("data/features/events.csv")

def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(INPUT)

    df["duration_minutes"] = df["duration_seconds"] / 60
    df["weekday"] = pd.to_datetime(df["date"]).dt.day_name()

    df.to_csv(OUTPUT, index=False)
    print(f"features: {len(df)} rows written to {OUTPUT}")

if __name__ == "__main__":
    main()