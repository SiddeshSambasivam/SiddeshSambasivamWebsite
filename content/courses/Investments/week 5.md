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

$$\sigma_i^2 = \sigma^2(\alpha_i) + \sigma^2(\beta_iR_m) + \sigma^2(\epsilon_i)$$

Total risk = Systematic risk ($\sigma^2[\beta_iR_m]$) + Firm-specific risk ($\sigma^2[\epsilon_i]$)

- $\sigma^2(\alpha_i) = 0$ **Why?** As $\alpha_i$ is the intercept hence does not change;

- $var(\epsilon_i) = 0$? Not necessarily in index model, but yes in CAPM.
  - In CAPM, we only invest in the market portfolio and it is fully diversified.

{{% callout note %}}

$R^2$ measures how much of the variation in $R_i$ is explained by $R_m$.

$R^2$ is **fitness of the model**.

$$R^2 = \frac{\beta_i^2 \sigma_m^2}{\sigma_i^2}$$

{{% /callout %}}

## B. Capital Asset Pricing Model (CAPM)

The <u>CAPM</u> shows how risk and expected returns relate in equilibrium, and what type of investment risk matters.

**Assumptions:**

1. Individual investors are "price takers"
   - The trading does not affect the price
   - Accept the price as given
2. Investments are limited to traded finanicial assets
   - No real estate, art, etc.
3. No taxes or transaction costs
   - Top bracket (22% for income > 320k)
4. People only care about **mean and variance** of returns
5. **Strong assumption:** People all have the same expectations, and the mean and variance of returns are known (Homogeneous expectations).

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

According to {{< hl >}}capital asset pricing model{{< /hl >}}, the expected return of an asset is a linear function of the expected return of the market portfolio and risk-free rate.

$$E[r_{i}] = r_f + \beta_i(E[r_M]-r_f)$$

### II. Understanding Beta

Beta is a {{< hl >}}measure of the systematic risk{{< /hl >}} of a security relative to the market.

$$\beta_i = \frac{cov(r_i,r_M)}{\sigma_M^2}$$

- Beta is the **sensitivity** of a security’s excess return to the systematic factor (mkt risk premium).

### III. CAPM: Security Market Line

{{< figure src="/investments/sml-capm.png" width="300px" title="Image from course lecture slides">}}

SML Slope is given by:

$$\frac{E[r_i]-r_f}{\beta_i} = \frac{E[r_m]-r_f}{\beta_m}$$

And $\beta_m = 1$, which gives us the CAPM equation.

- Buy positive $\alpha$ stocks to get market risk premium

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
