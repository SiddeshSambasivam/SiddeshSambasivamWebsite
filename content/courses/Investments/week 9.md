---
title: "9. Mutual funds and performance evaluation"
date: "2022-10-04"
type: book
weight: 9
toc: true
# _build:
# render: always
# list: never
---

{{< toc >}}

## Quick Recap

**Capital Allocation Line** -- Line created on a graph of all possible combination of risk-free and risky assets, and slope of which is known as reward-to-risk ratio.

- Used to choose how much to invest in a risk-free asset and one or more risky assets
- Based on the investor's risk tolerance, these allocations can be made

#### Capital Asset Pricing Model

Model that describes the relationship between **systematic risk** and expected return for assets (stocks).

- **Security Market Line** -- Visualization of CAPM, showing the relationship between risk (**measured by beta**) and expected return.

  - An investment evaluation tool derived from the CAPM
  - If expected return of a stock is above the SML, then the stock is **undervalued or underpriced**; Buy the stock
  - If expected return of a stock is below the SML, then the stock is **overvalued or overpriced**; Sell the stock

- **Capital Market Line** -- CAL where the risk portfolio is the market portfolio; Slope of the CML is the sharpe ratio of the market portfolio; **Risk is measured by standard deviation**

  - Intercept point of CML and efficient frontier would result in the most efficient portfolio called the tangency portfolio.

## A. Mutual funds

A mutual fund is a portfolio of financial securities. Many investors (typically investors) provide capital and a professional manager invests this 'pool' of capital in financial securities including stocks, bonds, money markets, etc.

- Passive management -- Invest in a well-diversified portfolio without searching for security mispricing.

  - Examples include index funds, ETFs, etc.
  - Assumes the **efficient market hypothesis is true**

- Active management -- Identifying the "mispriced" securities to beat the market
  - Assumes the **efficient market hypothesis is false**

### 1. Net Asset Value (NAV)

{{< hl >}}NAV is the price per share of a mutual fund.{{< /hl >}}

$$\text{NAV} = \frac{\text{Market Value of Assets} - \text{Liabilities}}{\text{Number of Shares Outstanding}}$$

- Liabilities: Unpaid expenses, management fees, etc.

### 2. Mutual fund fees

1. Front-end load -- A fee charged when you buy the fund
   - {{<hl>}} Front-end load does NOT affect NAV. {{</hl>}}

$$\text{Offer}_{t=0} = \frac{\text{NAV}_0}{1-\text{front-end load}}$$

2. Back-end load -- A fee charged when you sell the fund
   - {{<hl>}} Back-end load does NOT affect NAV. {{</hl>}}

$$\text{Redeem}_{t=1} = \frac{\text{NAV}_1}{1-\text{back-end load}}$$

3. Expense ratio -- % of NAV each year
   - The expense is calculated on the increased NAV after the front-end load

Always note the following:

- Make sure to subtract the expense ratio from the return; this return the current NAV

{{< callout note >}}
**Open-end fund:** Assume frontend load
{{< /callout >}}

#### Calculating <u>Returns</u>

$$\text{Return}_{fund}=\frac{\text{Redeem} - \text{Offer} + \text{Distributions}}{\text{Offer}}$$

- what is distribution??
  - Income - if mutual fund includes stocks, then it includes dividends or bond can payout coupons

$$\text{Return_fund}=\frac{\text{NAV}(1+\text{cap gain})(1-\text{exp ratio}) }{N}-1$$

## B. Portfolio Performance Evaluation

### 1. Risk Model: Jensen's Alpha

$$\alpha_P = \bar{R}\_P - \beta_P \bar{R}\_M$$

- $\alpha_P$ Portfolio alpha
- $\bar{R}_P$ Average excess return on the portfolio
- $\beta_P$ Beta of the portfolio
- $\bar{R}_M$ Average excess return on the market

### 2. Mutual Fund Performance

If <u>markets are efficient,</u> then before expenses, an average mutual fund has $\alpha = 0$.

- Across all fund managers, the average $\beta$ is 0

## C. Selecting Funds/Portfolios in Practice

1. Small investors select one portfolio (Entire-wealth portfolio).

   - Select portfolio with the highest sharpe ratio

2. Large investors hold many funds.

- Select funds using the `Treynor ratio`:

$$\text{Treynor ratio} = \frac{\bar{r_p} - \bar{r_f}}{\beta_p}$$

- $\bar{r_p}$ Average return on the portfolio
- $\bar{r_f}$ Average risk-free rate
- $\beta_p$ Beta of the portfolio

3. Adding an actively managed portfolio: Information Ratio
   - An actively managed portfolio delivers the benefit of $\alpha$, but adds idiosyncratic risk to our passive benchmark portfolio.

$$\text{Information ratio} = \frac{\alpha_p}{\sigma(e_p)}$$

- $\alpha_p$ per unit of unsystematic risk
- $\sigma(e_p)$ Standard deviation of the $e_p$ from an index model: $R_p = \alpha_p + \beta_p R_m + e_p$

**Information Ratio** is often used to evaluate hedge funds.

Hedge funds attempt to follow a <u>market neutral strategy</u>:

1. Beta equals zero, so the fund is not exposed to market risk
2. Alpha is positive

| Performance Measure | Application                                                                  |
| ------------------- | ---------------------------------------------------------------------------- |
| Sharpe Ratio        | To select one fund: for use as the optimal risky portfolio                   |
| Treynor Ratio       | Select fund of funds: for many portfolios                                    |
| Information Ratio   | Add to benchmark: For adding an active fund to an existing passive benchmark |
