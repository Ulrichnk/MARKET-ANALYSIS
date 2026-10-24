# Fixed-Income Quantitative Research — Bonds & Swaps

**Advanced MSc / early PhD | Quantitative Finance | Mathematical Derivations | Python**

A progressive, research-style portfolio of **nine academic assignments** on fixed-income instruments, interest-rate term structures, pricing, and market-risk hedging.

> **Current status:** Subject 01 substantially revised, with a 2026 ECB market-data study and additional proofs. Its solutions, tested pricing implementations, notebooks, data snapshot and empirical findings remain **to be completed**. The acquisition script has been published but has **not been successfully executed** here. The repository will distinguish work in progress from validated work.

## Research objectives

- Derive compounding conventions and relations between discount factors, spot rates, and forwards.
- Price fixed-income instruments, FRAs, and interest-rate swaps using no-arbitrage arguments.
- Derive duration, convexity, PV01, and curve-based risk sensitivities.
- Build and validate yield curves through bootstrapping and fitting.
- Design and test strategies to hedge bond and swap portfolios.
- Document assumptions, numerical accuracy, financial interpretation, and model limitations.

## Research roadmap

| # | Assignment | Status |
|---|---|---|
| 01 | [Interest rates and discounting](subjects/01-interest-rates-discounting.md) | **Problem statement published** |
| 02 | Bond contracts and classifications | Planned |
| 03 | Bond pricing and term structures | Planned |
| 04 | Duration, convexity, immunization | Planned |
| 05 | Coupon conventions and floating-rate notes | Planned |
| 06 | FRAs, interest-rate swaps, cross-currency swaps | Planned |
| 07 | PV01 and curve risk | Planned |
| 08 | Yield curve bootstrapping, interpolation, calibration | Planned |
| 09 | Convertible bonds and hybrid-risk models | Planned |

## Method

Every finished assignment will contain (1) rigorous hypotheses and derivations, (2) hand calculations, (3) reproducible Python code, (4) independent numerical tests, (5) interpreted plots, and (6) a critical discussion. Assignment texts are published separately from solutions. Merely publishing an assignment is not evidence of completed research.

**Cadence goal:** study up to two subjects per day while reserving adequate time for proof writing and technical validation. Progress is measured by verified deliverables, not commit counts.

## Reference and provenance

The syllabus follows Carol Alexander, *Market Risk Analysis*, Volume III, **Chapter III.1: Bonds and Swaps**, Sections III.1.2–III.1.10. Problem sets are original academic exercises motivated by the chapter, not reproductions of copyrighted content. The original book PDF is intentionally not uploaded.

The document's LIBOR treatment is historical: the final synthetic LIBOR settings ceased on **30 September 2024** ([FCA](https://www.fca.org.uk/markets/libor-transition)). Later work will distinguish legacy models from modern overnight-index discounting and multi-curve pricing.

## Official ECB dataset for Subject 01

- [Academic Subject 01](subjects/01-interest-rates-discounting.md) — proof exercises, market data, and critical analysis.
- [ECB dataset provenance](data/README.md) — definitions, official sources, and limitations.
- [ECB acquisition script](scripts/download_ecb_yield_curve.py) — obtains sovereign AAA zero-coupon spot observations with explicit dates and a metadata manifest.
- The older synthetic file is retained only as a **unit-test fixture**, never as real market evidence.

## Repository structure

- `subjects/`: French academic problem statements; worked proofs to follow separately.
- `data/`: official observations **when downloaded**, source manifests, and synthetic test fixtures.
- `src/`: implementation modules (added as completed).
- `tests/`: verification of mathematical identities and pricing routines.
- `notebooks/`: computational experiments and annotated visualizations.
- `results/`: research summaries, plots, and reports.

**Scope note:** Educational and research portfolio. No claim of production readiness or investment advice.
