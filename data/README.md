# Data — ECB yield curve

**Mandatory for Subject 01:** authentic historical ECB AAA sovereign zero-coupon yield-curve observations. Series key example: YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_1Y. Rates are annualised and continuously compounded, quoted in **percent**.

Source: [ECB Yield Curves](https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/euro_area_yield_curves/html/index.en.html) and [ECB Data Portal YC](https://data.ecb.europa.eu/data/datasets/YC).

Run: python scripts/download_ecb_yield_curve.py (Python + pandas + internet). The script requests 3M, 6M, 1Y, 2Y, 3Y, 5Y, 7Y, 10Y, 15Y, 20Y, and 30Y spots from 2026-09-01 through 2026-10-23, preserving original CSV and metadata in data/raw/.

**Important:** data/raw is not yet populated; the acquisition has not been successfully executed in this environment. Do not invent observations. Verify which dates and maturities were returned before conducting analysis.

The existing spot_curve_synthetic.csv is **synthetic test data only**; do not include it in figures or reports described as real market analysis.

ECB rates are estimated from sovereign bond information using Svensson fitting. They are **not raw zero-coupon trades** at each maturity and are **not OIS €STR collateral discount factors**.
