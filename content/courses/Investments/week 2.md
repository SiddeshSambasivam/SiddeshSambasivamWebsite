---
title: "2. Securities markets and trading"
date: "2022-08-12"
type: book
weight: 2
toc: true
---

{{< toc >}}

## A. Securities Markets

### A.1. Trading Costs

1. **Commission**: Fee paid to broker for making the transaction
   - SG: 0.5%
   - HK: 1%
   - CHN: 0.05%
   - US: $9.9/trade (Irespective of the amount of the trade)
2. Spread: Costof trading with dealer
   - Bid: Price the dealer is willing to pay
   - Ask: Price the dealer will sell
   - $\text{Spread} = \text{Bid} - \text{Ask}$

{{% callout note %}}
_Depth of the market:_ Total number of shares offered for trading at the best bid and ask prices.

- Market orders are highly volatile and can be executed at any price.

{{% /callout %}}

### A.2. Margin Trading

**Borrow** money, **Buy** stock.

Each broker would have a minimum cost to open a margin account. This minimum amount is called the **initial margin requirements**.

There are two margin requirements:

1. **Initial margin requirement (IMR):** Amount that needs to be payed as a down payment.

2. **Maintenance margin requirement (MMR):** Equity percentage that needs to be maintained in a margin account.

Buying on margin = Leveraging your position

The **margin** is the asset placed as a collateral as a percentage of stock position.

- Buying on margin is exteremely risky and magnifies both the profits and loss.

{{% callout note %}}

Sitaution: **Margin call** \
_The current value of equity equals or is less than the maintenance margin requirement._

- Ignore interest if considering a decrease in equity immediately after a purchase
- Include interest if considering a decrease in equity over a time period such as one year

{{% /callout %}}

Important Relationships / Concepts:

- $\text{Equity} (E)$ = Amount of own money invested
- $\text{Market value of stock position} \text{ (MVSP)}$ = # of shares x current price
- $\text{Borrowed amount} \text{ (B)}$ = Amount of money borrowed from the broker
- $\text{interest} \text{ (I)}$ = Interest paid on borrowed money
- $\text{additional cash} \text{ (C)}$ = Additional cash paid to the broker on margin calls (If any)
- $\text{dividend} \text{ (D)}$ = Dividend from stocks

$$E = \text{MVSP} - L - I + C + D$$
$$\frac{E}{\text{MVSP}} \le \text{MMR}$$

A margin call occurs,

$$\text{MVSP} \le \frac{\text{L}-\text{I}+\text{C}+\text{D}}{1-\text{MMR}}$$

A few key things to remember:

1. How to calculate margins at different stock prices
2. Calculating the rate of return for investments on margin

   $$\text{RR}= \frac{\text{MVSP} - \text{B} - \text{I}}{\text{E}}-1$$

   2.1 With Interest

   2.2 Without Interest

{{% callout note %}}

**Rate of Return on Investment by margin trading**

$$\text{RR} = \frac{\text{Final market value}-\text{Loan} - \text{Interest} + \text{Dividend}}{\text{Initial investment}} - 1$$

{{% /callout %}}

### A.3. Short Sales

**What is shorting?**

- Borrow shares of a stock and sell thm on market at current price in hope that the price will decrease.
- Buy the stock at a lower price and return to the lender

{{% callout note %}}
Federal Reserve Board requires all short sale accounts to have 150% of the value of the short sale at the time the sale is initiated.
{{% /callout %}}

#### The mechanics

1. Borrow stock from a broker/dealer, must post margin
2. Broker sells stock. Deposits proceeds and margin into a margin account
   - You are not allowed to withdraw the proceeds until you ‘cover.’
3. Covering or closing out the position:
   - Buy the stock.
   - Return the stock title back to the party from which it was borrowed

All the formulations remain almost the same as trading on margin, except the equity.

$$\text{Equity}=\text{Initial margin account}-\text{MVSP}-\text{Dividends}$$

_Market value of stock position and dividends are subtracted as the stocks are borrowed._

- The lender lends the stock with additional interest and commission imposed on the lending.`

$$\text{Initial margin account} = \text{Proceeds from sale}+\text{Cash deposited to meet margin requirements}$$

Furthermore, margin cll occurs when,
$$\text{MVSP} \ge \frac{\text{Margin Account} - \text{Dividend}}{1+\text{MMR}}$$

{{% callout note %}}

**Rate of Return on Investment by shorting on margin**

$$\text{RR} = \frac{\text{Proceeds from sale}-\text{Repurchase cost - Dividend}}{\text{Initial investment}}$$

{{% /callout %}}

## B. Risk and Return: Past and Prologue

### B.1. Rates of Return

1. Holding period returns

$$HPR_t = \frac{(P_t - P_{t-1} + D_t)}{P_{t-1}}$$

2. Arithmetic rates of return vs. Geometric rates of return

$$HPR_{AAR} = \frac{1}{T}\sum^T_{t=1}HPR_t$$

$$HPR_{GAR} = \frac{1}{T}\prod^T_{t=1}[1+HPR_t]^{1/T}-1$$

{{% callout note %}}

The geometric mean differs from the arithmetic average, or arithmetic mean, in how it is calculated because it takes into account the compounding that occurs from period to period.

**Conclusion:** Geometric mean is more accurate in real world calculation

{{% /callout %}}

## C. Class notes

Singapore is one to the top most expensive city to live in the world.

_What can we learn from buffett's investment strategy?_

- Value investing: Fundamental analysis
