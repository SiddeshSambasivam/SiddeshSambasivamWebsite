---
title: 'Efficient market hypothesis - I'
date: '2022-09-20'
type: book
weight: 7
toc: true
---

{{< toc >}}

## A. Using Multi-factor model

### 1. Fama-French (FF) 3 Factor Model

Fama and French 3 factor model is a standard model for analyzing stock returns. Built upon the observation that **firm size** and the **book-to-market ratio** historically explain stock returns.

MVSP = P x # of shares outstanding

**Observation:** Smaller firms have <u>higher</u> beta; <u>more-than</u> average returns.

- **Conclusion:** Smaller firms haver higher returns that what the CAPM would predict; This deviation is not captured by the CAPM. This missing factor was the FIRM SIZE.

$$\text{Book to Market Ratio} = \frac{\text{Book value of equity}}{\text{Market value of equity}}$$

### 2. Fama-French (FF) - 3 Factors model

$$E(r_G) = r_f + \beta_{G,M}(E(r_M)-r_f) + \beta_{G, SMB}E(r_{SMB}) + \beta_{G, HML}E(r_{HML})$$

1. Market Index Excess Return: $E(r_M)-r_f$; We only subtract the risk-free rate because

2. Small Minus Big (SMB) Index Excess Return: $E(r_{SMB})$

   - Difference between the returns of small and big firms

3. High Minus Low (HML) Index Excess Return: $E(r_{HML})$
   - Difference between the returns of high and low book-to-market firms

<font color="purple" style="font-weight:bold">Kahoot!</font> Q1: If the TRUE model of expected returns is the 10 Fama French 3 factor model:

$$E(r_G) = r_f + \beta_{G,M}(E(r_M)-r_f) + \beta_{G, SMB}E(r_{SMB}) + \beta_{G, HML}E(r_{HML})$$

An analyst instead estimates the CAPM index model:

$$E(r_i) = r_f + \alpha +\beta_{i}(E(r_M)-r_f)$$

What is the $\alpha$ if the analyst uses the CAPM model?

(2) Greater than 3%, less than 5%

### 3. Omitted Systematic Factors

<center><i>"Index models that OMIT important systematic factors produces poor estimates of $E(r_i)$"</i></center>

- Fama-French 3-factor model is better than the singleindex CAPM at explaining stock returns because it includes important factors.

- Single-index CAPM fails to explain the returns on too many stocks

## B. Random Walks and the Efficient Market Hypothesis

### 1. Efficient Market Hypothesis (EMH)

<center><i>"EMH proposes that security prices accurately reflect all available information"</i></center>

- If markets are efficient:

  - On average, investors cannot earn risk-adjusted positive profits

- If markets are not efficient:
  - active strategies should eaarn risk-adjusted positive profits and outperform passive strategies

### 2. Competition

<center><i>"Investor competition causes stock prices to fully and accurately reflect relevant, available information very quickly"</i></center>

- Once information becomes available, market participants quickly analyze it and trade on it.

Competition may not imply information efficiency when:

- Information is not available to all market participants

### 3. Random Walks

<center><i>"Stock prices should exhibit a Random Walk if price changes are unpredictable and random"</i></center>

$$P_{i,t} = B_{i} \times P_{i,t-1} + e_{i,t}$$

- $P_{i,t}$: Price of stock $i$ at time $t$
- $B_{i}$: $1+E(r_i)$
- $e_{i,t}$: Random change

**Why is there a postive trend?**

- Investors are risk averse average and they demand for positive risk premiums. They on average invest in stocks with positive risk premiums.
- Firms invest in postive NPV projects and grow on average
- Survivorship Bias. What about the firms performing poorly consistently? Kicked out

### 4. EMH: Three Forms

{{< figure src="/investments/emh-info.png" title="Relation b/w forms of EMH" >}}

{{< hl >}}Always use the information set to evaluate EMH related questions.{{< /hl >}}

1. Weak Form: Prices reflect all past information (historical prices and trading data)

   - if markets are weak-form efficient, investors can never construct a strategy with positive risk-adjusted returns using using historical price and trading data.

2. Semi-Strong Form: Prices reflect all public information

   - if markets are semi-strong-form efficient, investors can never construct a strategy with positive risk-adjusted returns using growth forecasts, accounting statements, past price, volume data & earnings

3. Strong Form: Prices reflect all information: both public and private

   - if markets are strong-form efficient, investors can never construct a strategy with positive risk-adjusted returns using any information (public or private)

{{% callout note %}}

- **Technical analysis** is a trading discipline employed to evaluate investments and identify trading opportunities by analyzing statistical trends gathered from trading activity, such as price movement and volume.

- **Fundamental analysis**, which attempts to evaluate a security's value based on business results such as sales and earnings.
  {{% /callout %}}
