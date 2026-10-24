# Assignment 01 — Interest Rate Theory, Discounting, and Forward Rates

**Level:** Advanced Master's / Early Doctoral Studies  
**Primary reference:** C. Alexander, *Market Risk Analysis*, Volume III, Sections III.1.2.1–III.1.2.5 (pp. 2–8).  
**Further reading:** Björk (no-arbitrage theory), Tuckman and Serrat (market conventions), Brigo and Mercurio (interest rate models).  
**Empirical data:** Official ECB estimates of euro-area AAA sovereign zero-coupon spot rates.  
**Status:** **ASSIGNMENT RELEASED — NOT YET SOLVED.** No completed proofs, tested implementations, or empirical results are claimed.

## Research Question

**Under which assumptions do spot, forward, simple, compounded, and continuously compounded interest rates provide financially consistent representations of the same market prices? What relationships are imposed by the absence of arbitrage?**

**Framework:** Let dates satisfy 0 ≤ S < T, measured in years. Let N denote the notional principal, V(T) a future value, and D(0,T)>0 the time-0 discount factor, with D(0,0)=1. Continuous rates are denoted by r; discrete rates by R. Forward rates f_{n,m} and F_{n,m} use n for the forward start (*term*) and m for the accrual period (*tenor*). Every rate must be accompanied by its compounding frequency, annualisation basis, and day-count convention. Do not identify a market-implied forward rate with the real-world expectation of a future short rate. Initial scenarios are deterministic, default-free, and frictionless; borrowing and lending at the assumed rates are permitted for the no-arbitrage arguments. **Do not treat an estimated AAA government yield curve as a collateralised OIS discount curve.**

## Part A — Foundations (15 marks)

**A1.** Define simple interest and compound interest. Derive the corresponding accumulation and discount factors.

**A2.** Starting from an annual nominal interest rate R, prove the convergence of (1+R/m)^(mT) to exp(RT), stating any positivity and domain restrictions.

**A3.** Solve V'(t)=r(t)V(t) for an integrable interest-rate function r(t). Deduce the associated accumulation formula and identify the required regularity assumptions.

**A4.** Examine the dimensions and units involved. Distinguish maturity, *term*, *tenor*, and accrual period using a labelled timeline.

**A5.** Explain the assumptions justifying A(0,T)=1/D(0,T). Distinguish D(0,T) from D(t,T) and explain their financial meanings.

## Part B — Continuously Compounded Spot and Forward Rates (20 marks)

*Alexander, Section III.1.2.1; Equations (III.1.1)–(III.1.4).*

**B1.** Define the continuously compounded spot rate r(0,T) in terms of D(0,T). Use two no-arbitrage investment strategies to establish the relationship linking time 0, S, and T.

**B2.** Derive the continuously compounded average forward rate over [S,T]. Recover the textbook relationship (III.1.3) for the one-year and two-year maturities.

**B3.** Assuming that T ↦ D(0,T) is positive and continuously differentiable, derive f(0,T)=−∂_T log D(0,T). Establish the corresponding integral representation and the relationship between the average spot rate and the instantaneous forward rate.

**B4.** Compare flat, upward-sloping, and non-monotonic spot curves. Explain why a forward rate observed today is not automatically the expectation, under the physical probability measure, of a future spot rate.

**B5.** For r(0,T)=a, r(0,T)=a+bT, and r(0,T)=a+bT exp(−T), derive D(0,T) and the instantaneous forward rate analytically. Plot and interpret the results.

**B6.** Investigate the assertion: “Every increasing spot-rate curve implies an increasing instantaneous forward-rate curve.” Prove the claim under suitable conditions or disprove it by constructing a counterexample.

## Part C — Conventions and Equivalent Interest Rates (20 marks)

**C1.** Prove the conversion formula between a continuously compounded rate r and an annual nominal rate R compounded m times per year. State the admissible domain.

**C2.** Show that financially equivalent rates produce identical discount factors. Explain why rates with the same numerical value under different conventions generally do not.

**C3.** Reproduce Example III.1.1 from the textbook (N=500, R=4%, T=3.5 years, semiannual compounding). Compare the result with continuous compounding at the **numerically identical** rate of 4%.

**C4.** Compare the textbook's hybrid convention in Equation (III.1.11), for a non-integer maturity, with fractional-period compound interest. Use T=1.4 and R=5%.

**C5.** Determine the exact number of days from 15 January to 17 April 2026. Calculate the interest on a €10 million notional at an annualised rate of 3.2% using ACT/360 and ACT/365F. Explain the numerical difference.

**C6.** Revisit C3 and calculate the continuously compounded rate **equivalent** to 4% with semiannual compounding. Verify that it produces exactly the same terminal value, unlike a continuously compounded rate merely equal to 4% numerically.

**C7.** Analyse admissible negative rates and the domain of discount factors. Explain why D(0,T)>0 does **not** imply D(0,T)<1.

## Part D — Discretely Compounded Spot and Forward Rates (20 marks)

*Alexander, Section III.1.2.4; Equations (III.1.17)–(III.1.18).*

**D1.** Derive Equation (III.1.17) from no-arbitrage reasoning and generalise the product identity in Equation (III.1.18).

**D2.** Given annual-compounding spot rates of 5%, 6%, and 6.5% at maturities of 1, 2, and 3 years, respectively, calculate the successive annual forward rates and verify the no-arbitrage accumulation identities.

**D3.** Given a year fraction α(S,T), derive the annualised simple forward rate in terms of D(0,S)/D(0,T). Specify the units and the day-count assumptions.

**D4 — Critical reading of the source.** Examine the notation F_{6,9} and the dates stated in Section III.1.2.4. A forward rate starting in six months with a nine-month tenor cannot simultaneously start in month nine. Draw the consistent timeline, identify the inconsistency, and explain the correction while preserving the notation convention.

**D5.** Given annualised simple spot rates of 4.5%, 4.3%, 4.2%, and 4.0% at 3, 6, 9, and 12 months, respectively, reconstruct the successive three-month forwards and a six-month forward starting in six months. State all accrual factors and verify the accumulation identities without intermediate rounding.

## Part E — Empirical Research with Official ECB Data and a Python Laboratory (15 marks)

**Mandatory data source:** [ECB — Euro Area Yield Curves](https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/euro_area_yield_curves/html/index.en.html) and [ECB — YC Dataset](https://data.ecb.europa.eu/data/datasets/YC).

The reported series are **Svensson-based estimates of sovereign zero-coupon yields**, quoted as **annual percentages with continuous compounding**. They are **not** OIS rates, nor are they individually traded bond prices for every quoted maturity.

Use the script at `scripts/download_ecb_yield_curve.py` to retrieve AAA-series observations for maturities 3M, 6M, 1Y, 2Y, 3Y, 5Y, 7Y, and 10Y, with optional 15Y, 20Y, and 30Y series. An example full series key is **YC.B.U2.EUR.4F.G_N_A.SV_C_YM.SR_1Y**.

**Requested observation window:** 1 September–23 October 2026. Prefer **22 October 2026** for the first cross-sectional analysis **only if all required series have observations on that date**. Compare it with a second common observation date approximately one month earlier. **No market observations are supplied or assumed unless the download has completed successfully.**

**E1.** Produce a data dictionary identifying series keys, observation dates, retrieval dates, units, missing values, and the rule used to select common observation dates. Demonstrate the conversion from percentages to decimal rates.

**E2.** Implement `discount_continuous`, `discount_simple`, `discount_compound`, `nominal_to_continuous`, `continuous_to_nominal`, `forward_continuous`, and `forward_simple`. Document all parameters and admissible domains.

**E3.** Reconstruct D(0,T) from ECB spot estimates observed on a common date. Calculate average forward rates over [3M,6M], [6M,1Y], [1Y,2Y], [2Y,3Y], [3Y,5Y], and [5Y,10Y]. For this first experiment, explicitly set α(S,T)=T−S. Explain why contractual ACT-based accrual factors may differ.

**E4.** Implement at least **ten independent tests**, including inverse relationships, equivalence across conventions, discount-factor decomposition, continuity, unit consistency, boundary cases, admissible negative rates, and missing observations. Specify and justify numerical tolerances.

**E5.** Produce and interpret four charts: **(1)** ECB spot curves on two dates; **(2)** the corresponding discount-factor curves; **(3)** average forwards by maturity segment; **(4)** historical changes in basis points. Identify market-derived observations, calculated rates, and any interpolation.

**E6.** Remove one maturity, reconstruct it through a clearly specified interpolation method, and measure the difference from the corresponding ECB estimate. Discuss why a good statistical fit alone does not establish the absence of arbitrage.

**Optional extension:** Compare an ECB instantaneous forward-rate estimate (e.g., IF_1Y or IF_2Y) with an average forward rate over a finite interval.

**Data-integrity warning:** The existing `data/spot_curve_synthetic.csv` file is a **synthetic testing dataset**. It must never be described as historical market data.

## Part F — Critical Analysis (10 marks)

**F1.** Explain the historical role of LIBOR in Section III.1.2.5 and why it must not be treated as a currently published benchmark in 2026 (final LIBOR publication: 30 September 2024). Distinguish €STR, Euribor, and AAA government yields. Refer to the [FCA LIBOR notice](https://www.fca.org.uk/news/press-releases/end-libor), the [ECB €STR page](https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/euro_short-term_rate/html/index.en.html), and [EMMI Euribor](https://www.emmi-benchmarks.eu/benchmarks/euribor/).

**F1b.** Locate an independently verifiable daily €STR fixing. Distinguish its reference date, publication date, and tenor.

**F2 — Research essay (700–1,000 words).** Discuss the proposition: **“Why are discount factors more fundamental than interest-rate quotation conventions?”** Support your response with a no-arbitrage argument, a numerical illustration, and at least two limitations of the deterministic framework.

## Required Deliverables and Completion Criteria

1. **`reports/01_interest_rates.md`:** independently derived proofs, calculations, assumptions, and critical discussion.
2. **`src/rates/`:** documented Python functions with explicit signatures and assumptions.
3. **`tests/test_01_rates.py`:** reproducible unit tests with justified tolerances.
4. **`notebooks/01_interest_rates.ipynb`:** reproducible analysis and interpretation of the four ECB-market-data charts.
5. **`data/`:** authenticated ECB observations and a provenance manifest; see `data/README.md`.
6. **`results/01-summary.md`:** concise account of verified findings, discrepancies, and limitations.

**Mark allocation:** Part A: 15; Part B: 20; Part C: 20; Part D: 20; Part E: 15; Part F: 10. **Total: 100 marks.**

**Scientific completion standard:** This assignment may be marked **Complete** only after proofs have been checked, tests executed successfully, empirical figures reproduced from documented sources, and limitations critically evaluated. Publishing an assignment statement does not mean that its research has been completed.

## References

- **Carol Alexander**, *Market Risk Analysis*, Volume III, Section III.1.2.1–III.1.2.5: the principal syllabus, historical examples III.1.1–III.1.3, and Equations III.1.1–III.1.18. The questions in this assignment are original and are not a transcription of the source.
- **Tomas Björk**, *Arbitrage Theory in Continuous Time*, 4th ed.: supplementary foundations of arbitrage theory, without importing advanced stochastic assumptions without justification.
- **Bruce Tuckman and Angel Serrat**, *Fixed Income Securities*: market conventions and fixed-income interpretation.
- **Damiano Brigo and Fabio Mercurio**, *Interest Rate Models: Theory and Practice*: later extensions to advanced interest-rate models.
- **European Central Bank**, [Yield Curve Methodology](https://data.ecb.europa.eu/methodology/yield-curves) and [YC Dataset](https://data.ecb.europa.eu/data/datasets/YC).
- **Financial Conduct Authority**, [The End of LIBOR](https://www.fca.org.uk/news/press-releases/end-libor).

**Scope limitation:** Estimated AAA sovereign yields must not be silently substituted for collateralised OIS discount rates. Multi-curve pricing, swap valuation, and fully stochastic rate models belong to later assignments.
