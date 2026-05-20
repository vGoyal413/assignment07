import marimo

__generated_with = "0.9.0"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt
    return mo, pd, plt


@app.cell
def __(mo):
    mo.md("# Event Duration Report")
    return


@app.cell
def __(pd):
    df = pd.read_csv("data/features/events.csv")
    df.head()
    return (df,)


@app.cell
def __(df, mo):
    mo.md(f"""
    ## Dataset Summary
    - **Total events:** {len(df)}
    - **Unique users:** {df['user_id'].nunique()}
    - **Event types:** {', '.join(sorted(df['event_type'].unique()))}
    - **Date range:** {df['date'].min()} to {df['date'].max()}
    """)
    return


@app.cell
def __(df, plt):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df["duration_minutes"], bins=20, edgecolor="white", color="#4C72B0")
    ax.set_xlabel("Duration (minutes)")
    ax.set_ylabel("Number of Events")
    ax.set_title("Distribution of Event Durations")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    fig
    return ax, fig


if __name__ == "__main__":
    app.run()