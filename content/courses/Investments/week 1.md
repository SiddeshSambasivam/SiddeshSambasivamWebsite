---
title: 'Asset classes and financial instruments'
date: '2022-08-12'
type: book
weight: 1
toc: true
---

{{< toc >}}

## A. The Money Market

Money market is a subsector of the _debt_ market.

- <u>Short term</u> debt instruments
- Highly marketable (high liquidity)
- Low rates of return

**Q.** _What are debt instruments?_ \
Debt refers to money borrowed by corporates or the government in order to finance their capital needs. Deby relfects an obligation of the company to pay back. Example of debt instruments:

- Bonds
- Debentures
- Term loads

### I. Treasury bills

{{% callout note %}}
Investors can use treasury bills to adjust exposure to risk.
{{% /callout %}}

#### I.A. US Treasury bills

U.S Treasury bills (_T-Bills_) are the most marketable of all money market instruments. The T-Bills are issued by the U.S. federal government.

- Maturity: <= 52 weeks (1 Year)
- Default risk? None
- Does it pay a coupon? No

Why is it issued?

- Government **raises money by selling bills** to the public.
- _Whats in it for investors?_

  Investors buy the bills at a face value and difference between the purchase and ultimate maturity value represents the investor's earnings.

{{% callout note %}}

**Why is it special?**

- Safe against defaulting
- Not callable
- Highly liquid

{{% /callout %}}

#### I.B. Singapore Government Securities (SGS)

SGS are issued by the Monetary authority of Singapore on behalf of the government of Singapore.

{{% callout note %}}

- **T-bills:** 3 months, 1 year
- **Bonds:** 2, 5, 10, 15, 20 years
- **Minimum denomination:** <span style="color:green;font-weight:bold">S$1,000</span>
  {{% /callout %}}

  - _What is denomination?_ The face value of a banknote, coin, or postage stamp.

- Proceeds from debt issues cannot be used for government expenditures.
- Retail investors trade through SGX

  - _Who are retail investors?_ A retail investor is a non-professional investor. Also known as individual investors.

- Institutional investors trade on the OTC market.
  - _what is OTC market?_ Over-the-counter (OTC) is the process of trading securities via a broker-dealer network as opposed to on a centralized exchange.

Other money market instruments include but are not limited to:

- Certificates of deposit (CD)
- Commericial paper (CP)
- Banker's Acceptances
- Eurodollar
- London Interback Offer Rate (LIBOR)

## B. The Bond Market

### I. Fixed Income Instruments

US Treasury Bonds and Notes.

- Bonds (10 to 30 years), Notes (up to 10 years)
- Denomination: Typically $1000
- Interest type: Coupon
- Risk: Very safe

**Treasury Inflation Protected Securities (TIPS)**

{{% callout note %}}
TIPS is a fixed-income instrument used to back out market's expectation of inflation.
{{% /callout %}}

A type of U.S. Treasury security whose principal value is indexed to the rate of inflation.

- If inflation rises, the TIPS' principal value is adjusted up.
- If there's deflation, then the principal value is adjusted lower.

TIPS are referenced to one specific index: TIPS have principal adjusted by the consumer price index.

- ❗Remember:
  1. Nominal YTM $\approx$ real YTM + expected inflation
  2. Expected inflation $\approx$ Nominal YTM - real YTM

{{% callout note %}}
**To know:** _Use TIPS to measure the market's expectation of future inflation._

THe math for the inflation rate to break even is shown below,

$\text{Expected Inflation} = \text{Treasury Yield} - \text{TIPS Yield}$

{{% /callout %}}

- TIPS trading volume is much lower that that of T-notes. The yield can often change due to factors that do not relate to what inflation might be in the future.

{{< spoiler text="Discussion: **What are the major differences between T-Bonds/Notes and T-Bills?**">}}

The difference between bills, notes, and bonds are the lengths until maturity.

- T-Bills: < 1 year
- T-Notes: 2,3,5,7 and 10 years
- T-Bonds: 30 years

{{< /spoiler >}}

_Things to learn:_

- Yield to maturity (YTM)
- Coupon rate/Interest rate

## C. Stock and Bond Indexes

_Purposes of indexes:_

- Track average returns
- Compare performance of money managers
- Base of derivatives

  **Q.** What is a derivative? \
  A type of financial contract whose value is dependent on the value of an underlying asset, group of assets, or benchmark.

1. _Mutual Fund_ - Investment fund that pools funds from investors to buy securities.
2. _Index Fund_ - A mutual fund which buys securities with the goal of tracking an index.
3. _Exchange traded Fund_ - An index fund which trades on an exchange.

**Examples:** Dow Jones Industrial Average (DJIA)

### Construction of Indexes

**Market-value Weighted**

- _Construction:_ Amount invested in each stock are proportional to market value of each stock.
- _Requires:_ Price and number of shares outstanding.

| Stock | Price (t=0) | Quantity (t=0) | Price (t=1) | Quantity (t=1) |
| ----- | ----------- | -------------- | ----------- | -------------- |
| AAPL  | $10         | 40             | $15         | 40             |
| GOOGL | $50         | 80             | $25         | 160            |
| MSFT  | $140        | 50             | $150        | 50             |

$\text{Index Value}_{\ t=0}$ = $(10 \times 40)+(50 \times 80)+(140 \times 50)$

$\text{Index Value}_{\ t=1}$ = $(15 \times 40) + (25 \times 80) + (150 \times 50)$

Relative value of Index:

$\text{R. Index Value}_{\ t=1}$ = $\frac{\text{Index Value}\_{\ t=0}}{\text{Index Value}\_{\ t=1}} \times 100 = 106.14$

## D. Types of Orders

**Bid price:** Dealer pays you \
**Ask price:** You pay the dealer

$\text{Ask price} - \text{Bid price} = \text{Dealers profit}$

{{< youtube vENGp8Ivo8E >}}

| Type                                                | Description                                                                                                                                                                                                                                           |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- |
| Market order                                        | Execute immediately at the best price (buy now)                                                                                                                                                                                                       |
| Limit order                                         | Buy or sell at a specified price or better <br/> <b>Limit buy:</b> Buy only if someone is willing to buy for price _equal to or lower that specified_ <br/> <b>Limit sell:</b> Sell only if buyer willing to pay _equal or more than specified price_ |
| Stop loss (stop-sell) order                         | Becomes a **market sell order** if the stock price hits a limit set by the rule (protection)                                                                                                                                                          |
| Stop buy order                                      | Becomes a **market buy order** if the stock price hits a tigger value set by the rule (Riding the wave)                                                                                                                                               |     |     |
| Discretionary order                                 | Give broker that power to buy and sell for your account at broker's discretion.                                                                                                                                                                       |
| Time dimension on orders (Other than market orders) | _IOC:_ Immediate or cancel<br> _Day:_ By default <br> _GTC:_ Good until canceled (usually 60 days max)                                                                                                                                                |

### Short Sales: Mechanics

1. Borrow stock from broker/dealer, must post margin
2. Broker sells stock. Deposits proceeds and margin into margin account
   - Not allowed to withdraw the proceeds until you 'cover.'
3. Covering or closing out the position:

**Q1.** Breadtalk, a <u>small cap</u> stock, is currently trading at `$1.32`. It is expected to increase by `5%` tomorrow. OCBC, a <u>large cap</u>stock, is currently trading at `$9.50`. It is expected to fall by `5%` tomorrow. Both stocks are in the Straits Times Index (STI).

How would you <u>expect STI to change</u> (i.e. fall, remain
unchanged, increase) tomorrow, assuming all other stocks
in STI remain flat tomorrow?

**Q2.** You placed a <u>limit buy order</u> at `$55.37`. Given the
market prices, will your order be executed?

|          | Bid    | Ask    |
| -------- | ------ | ------ |
| Marriott | $55.25 | $55.50 |

**Q3.** You placed a <u>stop-loss order</u> at $55 when the current price is `$62`. How much would you receive if the price drops to `$50` ?

## F. Critical Thinking

> “A limit buy order is defined as the highest
> buy and a limit sell order is defined as the
> lowest sell. However, in my notes, I wrote
> down limit buy order as buy low and limit
> sell order as sell high.”

_Are these two statements consistent?_

Yes, they are consistent.
