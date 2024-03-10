---
title: 'CAPM and APT (Part-2)'
date: '2022-08-12'
type: book
weight: 6
toc: true

_build:
  render: always
  list: never
---

{{< toc >}}

## A. Multifactor models

### 1. Factor Loadings & Risk Preiums

$$E(r_p) = r_f + \beta_{P,1}\times(E(r_1)-r_f) + \beta_{P,2}\times(E(r_2)-r_f)$$

1. Loading on the factor portfolios: $\beta_{P,1}$ and $\beta_{P,2}$

   - How a security's (P) returns "co-vary" with the returns of the factor portfolios (1 and 2)

2. Risk premium on the factor portfolios: $(E(r_1)-r_f)$ and $(E(r_2)-r_f)$

   - Risk premium associated with the risk factor portfolio

### 2. What is Factor Portfolio?

A <u>well-diversified</u> portfolio of many securities:

1. Zero idiosyncratic risk
2. A beta of 1 related to one risk factor
3. A beta of 0 w.r.t other risk factors

   - Market portfolio with respect to the interest rate risk factor portfolio is:

   $$\beta_{M, IR} = 0$$

### 3. Understanding equilibrium

In equilibrium, a <u>well-diversified</u> portfolio P must satisfy:

$$\frac{E(r_p)-r_f}{\beta_p} = \frac{E(r_M)-r_f}{\beta_M}$$

{{% callout note %}}
The above equation is based on capital asset pricing model (CAPM) and is the slope of <u>security market line</u>.
{{% /callout %}}

Hence we can re-write the equation as:

$$E(r_p) = r_f + \beta_p\times(E(r_M)-r_f)$$

This is very similar to **CAPM.**

$$E(r_i) = r_f + \beta_i\times(E(r_M)-r_f)$$

If $\alpha_p \ne 0$, an arbitrage opportunity exists.

## B. Arbitrage Pricing Theory (APT)

**INTUITION** for arbitrage pricing:

How to take advantage of arbitrage opportunity?

1. Requires no initial investment
2. Earns a positive profit with complete certainty

No initial investment + No risk

## C. 1-Factor Arbitrage Pricing

**Step 1:**

## D. 2-Factor Arbitrage Pricing
