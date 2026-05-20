import pathlib
import pandas as pd

VALID_EVENT_TYPES = {"login", "click", "purchase", "scroll", "view"}

INPUT  = pathlib.Path("data/raw/events.csv")
OUTPUT = pathlib.Path("data/clean/events.csv")

def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(INPUT, dtype=str)

    # Drop missing/empty fields
    df = df.dropna()
    df = df[df.apply(lambda r: all(str(v).strip() != "" for v in r), axis=1)]

    # Drop invalid event_type
    df = df[df["event_type"].isin(VALID_EVENT_TYPES)]

    # Drop non-positive duration_seconds
    df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="coerce")
    df = df.dropna(subset=["duration_seconds"])
    df = df[df["duration_seconds"] > 0]
    df["duration_seconds"] = df["duration_seconds"].astype(int)

    # Normalize timestamps to YYYY-MM-DDTHH:MM:SS
    df["timestamp"] = df["timestamp"].apply(
        lambda ts: pd.to_datetime(ts.strip()).strftime("%Y-%m-%dT%H:%M:%S")
    )
    df = df.dropna(subset=["timestamp"])
    df = df.reset_index(drop=True)

    df.to_csv(OUTPUT, index=False)
    print(f"clean: {len(df)} rows written to {OUTPUT}")

if __name__ == "__main__":
    main()