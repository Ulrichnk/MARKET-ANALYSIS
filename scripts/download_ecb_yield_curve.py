"""Acquire authentic ECB AAA zero-coupon spot rates; no synthetic fallback.

Run: python scripts/download_ecb_yield_curve.py
Requires: Python 3.10+, pandas, internet access.
Original ECB observations remain in percent per annum, continuous compounding.
"""
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from io import BytesIO
import json

MATURITIES = ("3M","6M","1Y","2Y","3Y","5Y","7Y","10Y","15Y","20Y","30Y")
SERIES = "B.U2.EUR.4F.G_N_A.SV_C_YM." + "+".join("SR_" + t for t in MATURITIES)
BASE_URL = "https://data-api.ecb.europa.eu/service/data/YC/" + SERIES
PARAMS = {"startPeriod": "2026-09-01", "endPeriod": "2026-10-23", "format": "csvdata"}
URL = BASE_URL + "?" + urlencode(PARAMS)
OUTDIR = Path(__file__).resolve().parents[1] / "data" / "raw"

def main():
    import pandas as pd
    request = Request(URL, headers={"Accept": "text/csv", "User-Agent": "FixedIncomeAcademicPortfolio/1.0"})
    with urlopen(request, timeout=60) as response:
        if response.status != 200:
            raise RuntimeError("Unexpected ECB response status")
        raw = response.read()
    if b"TIME_PERIOD" not in raw[:5000] or b"OBS_VALUE" not in raw[:5000]:
        raise ValueError("The server response is not a recognizable ECB SDMX CSV")
    df = pd.read_csv(BytesIO(raw))
    if df.empty or not {"TIME_PERIOD","OBS_VALUE"}.issubset(df.columns):
        raise ValueError("No valid ECB observations returned")
    if "KEY" not in df.columns and "DATA_TYPE_FM" not in df.columns:
        raise ValueError("Cannot identify the ECB maturity series")
    OUTDIR.mkdir(parents=True, exist_ok=True)
    outfile = OUTDIR / "ecb_aaa_spot_rates_2026-09_to_2026-10.csv"
    outfile.write_bytes(raw)
    manifest = {
        "source": "European Central Bank, euro area AAA sovereign zero-coupon curve",
        "request_url": URL,
        "retrieval_utc": datetime.now(timezone.utc).isoformat(),
        "unit": "percent per annum",
        "compounding": "continuous",
        "observations": len(df),
        "first_observation_date": str(df.TIME_PERIOD.min()),
        "last_observation_date": str(df.TIME_PERIOD.max()),
        "columns": list(df.columns),
        "important": "Sovereign AAA estimated spot yields, not an OIS discount curve",
    }
    outfile.with_suffix(".metadata.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print("Saved", outfile, "; rows:", len(df))

if __name__ == "__main__":
    main()
