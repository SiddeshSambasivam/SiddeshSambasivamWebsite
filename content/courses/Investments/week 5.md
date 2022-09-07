---
title: "5. CAPM and APT (Part-1)"
date: "2022-08-12"
type: book
weight: 5
toc: true
---

{{< toc >}}

## A. Index Model & Capital Asset Pricing

### I. Two Components of Stock Risk

$$\sigma_i^2 = \sigma(\alpha_i) + \sigma^2(\beta_iR_m) + \sigma^2(\epsilon_i)$$

Total risk = Systematic risk + Firm-specific risk

- $\sigma_i^2 = 0$ **Why?**
- $var(\epsilon_i) = 0$? Not necessarily in index model, but yes in CAPM.

{{% callout note %}}

$R^2$ measures how much of the variation in $R_i$ is explained by $R_m$.

$R^2$ is **fitness of the model**.

$$R^2 = \frac{\beta_i^2 \sigma_m^2}{\sigma_i^2}$$

{{% /callout %}}

## B. Capital Asset Pricing Model (CAPM)

The <u>CAPM</u> shows how risk and expected returns relate in equilibrium, and what type of investment risk matters.

### I. Overview of Implications

<p align="center"><i>"All investors will hold some combination of the market portfolio (M) and the risk-rate"</i></p>

Market portfolio:

- All assets of the security universe
- Market value weighted
- Optimal risky portfolio and on efficient frontier

#### CAPM, Capital Market Line

$$E[r_{C,M}] = r_f + y_M(E[r_M]-r_f)$$

{{< spoiler text="Quick Recap">}}
A theoretical concept that gives optimal combinations of a **risk-free asset** and the **market portfolio**.

The CML is superior to Efficient Frontier because it combines risky assets with risk-free assets.

{{< /spoiler >}}

Given all the assets have been invested in the risky portfolio (y=1), the market risk premium is:

$$E[r_M]-r_f = A\times\sigma_M^2$$

According to capital asset pricing model, the expected return of an asset is a linear function of the expected return of the market portfolio and risk-free rate.

$$E[r_{i}] = r_f + \beta_i(E[r_M]-r_f)$$

### II. Understanding Beta

Beta is a measure of the systematic risk of a security relative to the market.

$$\beta_i = \frac{cov(r_i,r_M)}{\sigma_M^2}$$

- Beta is the **sensitivity** of a security’s excess return to the systematic factor (mkt risk premium).

### III. CAPM: Security Market Line

{{< figure src="/investments/sml-capm.png" width="300px" title="Image from course lecture slides">}}

## C. Arbitrage Pricing Theory (APT)

### I. Overview of APT

<p align="center"><i>"Describes the relation between expected returns and risk when there are <b>ONE or MORE sources of systematic risk.</b>"</i></p>

A systematic risk must be:

1. Pervasive - Source of risk must potentially impact most companies, leading the stock prices to unexpcetedly change.

2. Undiversifiable - Source of risk can not be diversified away in a large portfolio.

### II. APT: Assumptions

1. No taxes, no transaction costs
2. Investors can form well-diversified portfolios
   - Well-diversified portfolios only contain systematic risk
3. No arbitrage opportunities exist

{{% callout note %}}

**Arbitrage:** An investment strategy in which an investor simultaneously buys and sells an asset in different markets to profit from a difference in the price.

- An arbitrage opportunity exists when two securities always
  have the same payoff but **DO NOT** have the **same price**

{{% /callout %}}
