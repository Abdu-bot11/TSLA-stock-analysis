"""
Part 1: Extract daily closing prices for TSLA from the SP500 minute-level CSV.
Saves results to TSLA_close.txt (one closing price per line, no header).
"""

import os
import pandas as pd


def export_daily_close_onecol(
    csv_path: str,
    out_txt_path: str,
    ticker: str,
    start_date: str | None = None,
    end_date: str | None = None,
    tz: str = "America/New_York",
):
    it = pd.read_csv(
        csv_path,
        usecols=["Unnamed: 0", "close", "ticker"],
        chunksize=2_000_000,
        dtype={"ticker": "string"},
    )

    start = pd.Timestamp(start_date, tz=tz) if start_date else None
    end   = pd.Timestamp(end_date,   tz=tz) if end_date   else None

    daily_parts = []

    for chunk in it:
        ts_utc = pd.to_datetime(chunk["Unnamed: 0"], utc=True, errors="coerce")
        ts     = ts_utc.dt.tz_convert(tz)

        mask = chunk["ticker"] == ticker
        if start is not None:
            mask &= ts >= start
        if end is not None:
            mask &= ts <= end + pd.Timedelta(days=1) - pd.Timedelta(seconds=1)

        if mask.any():
            daily_parts.append(
                pd.DataFrame({
                    "ts":    ts[mask].values,
                    "close": chunk.loc[mask, "close"].values,
                })
            )

    if not daily_parts:
        print(f"No data found for ticker '{ticker}'.")
        open(out_txt_path, "w").close()
        return pd.Series(dtype="float64")

    df          = pd.concat(daily_parts, ignore_index=True).sort_values("ts")
    daily_close = df.groupby(df["ts"].dt.date)["close"].last()

    daily_close.to_csv(out_txt_path, index=False, header=False, float_format="%.6f")
    print(f"Done! Saved {len(daily_close)} daily closing prices to: {out_txt_path}")
    return daily_close


if __name__ == "__main__":
    # This is the exact filename we saw in your Desktop folder
    CSV_PATH = "SP500.min.2023Jan.bars (1).csv"
    OUT_PATH = "TSLA_close.txt"

    print("Looking for CSV:", CSV_PATH)
    print("File found?", os.path.exists(CSV_PATH))

    daily = export_daily_close_onecol(
        csv_path=CSV_PATH,
        out_txt_path=OUT_PATH,
        ticker="TSLA",
        start_date="2023-01-01",
        end_date="2023-01-31",
    )

    if len(daily) > 0:
        print("\nTSLA daily closing prices:")
        print(daily.to_string())
