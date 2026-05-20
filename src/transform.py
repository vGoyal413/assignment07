import pathlib
import pandas as pd

INPUT  = pathlib.Path("data/clean/events.csv")
OUTPUT = pathlib.Path("data/transformed/events.csv")

def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(INPUT)

    df["date"] = pd.to_datetime(df["timestamp"]).dt.strftime("%Y-%m-%d")

    df.to_csv(OUTPUT, index=False)
    print(f"transform: {len(df)} rows written to {OUTPUT}")

if __name__ == "__main__":
    main()