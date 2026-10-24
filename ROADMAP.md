# Nine-subject research roadmap

| # | Topic | Source | Minimum deliverable |
|---|---|---|---|
| 01 | Interest-rate conventions and forwards | III.1.2 | No-arbitrage derivations; discount curve and forwards; validation tests |
| 02 | Bond classification and cash flows | III.1.3 | Contract definitions, payment calendar, cash-flow engine |
| 03 | Bond valuation and spot curves | III.1.4 | Pricing and yield solver; price–yield analysis |
| 04 | Duration, convexity, immunization | III.1.5 | Derivatives, Taylor errors, portfolio hedge |
| 05 | Floating-rate notes and coupon frequency | III.1.6 | Coupon conventions, reset mechanism, relative rate risk |
| 06 | FRAs and swaps | III.1.7 | Fair rates, leg PVs, value changes, cross-currency case |
| 07 | PV01 and interest-rate risk | III.1.8 | Finite-difference/analytic sensitivities and curve shocks |
| 08 | Yield-curve fitting | III.1.9 | Bootstrap, spline and parametric fit; noise sensitivity |
| 09 | Convertible bonds | III.1.10 | Hybrid contract decomposition and simplified valuation |

## Assignment protocol
1. Publish **original, unsolved** academic problem statement.
2. Prove key formulas independently; document assumptions and conventions.
3. Implement and test numerical calculations in Python.
4. Present reproducible experiments with labelled axes, units and interpretation.
5. Record errors, assumptions, limitations, and sources.
6. Only mark **Complete** after reports, code and tests exist.

**Study cadence:** aim for up to two topics under active study per day. Never confuse subject publication with completion. Keep written solutions separated from exercise statements.

## Completion checklist
- [ ] Proofs are consistent and contain explicit assumptions.
- [ ] All rates have compounding and day-count conventions.
- [ ] Computational methods reproduce analytic benchmarks.
- [ ] Unit tests pass with documented tolerances.
- [ ] Graphs are labelled, reproducible, and interpreted.
- [ ] Results identify model limitations.
- [ ] Readme status matches files actually present.

## Scope extensions
Core § III.1 first, followed by modern OIS discounting, multi-curve projection, and non-parallel curve-risk methods. These are **extensions**, not presented as material contained in the source.
