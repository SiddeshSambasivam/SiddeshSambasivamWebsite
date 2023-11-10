---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'CAP Theorem Explained: Why You Can’t Have It All'
subtitle: ''
summary: ''
authors: ['Siddesh Sambasivam']
tags: []
categories: []
date: 2023-09-03T12:57:13+08:00
lastmod: 2023-09-03T12:57:13+08:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []

_build:
  render: never
  list: never
---

Designing efficient systems at scale and making tradeoffs frequently requires understanding a fundamental system concept known as CAP theorem.

{{% callout note %}}

**What is CAP Theorem?**

It states that any distributed data store can provide only two out of three guarantees: Consistency, Availability, and Partition Tolerance.

{{% /callout %}}

Understanding the tradeoffs between the three tolerances comes handy when working on new features or building a product. It is important to consider these tradeoffs at early stage to prevent later inefficiencies

## Understanding the CAP theorem

{{< figure src="blog/cap.png" width="280px" title="Illustration from https://blog.jetbrains.com/blog/2021/06/03/big-data-world-part-5-cap-theorem/" >}}

### 1. Consistency

It ensures that a query always return the most recent data from the data store. In case the system can't guarantee consistency, the query will fail.

However, achieving consistency comes at a cost. To maintain this guarantee, the system might need to wait for updates to propagate across all nodes in the network, resulting in high latency.

#### Examples:

1. If you transfer money from one bank account to another, the balances of both accounts should be updated instantly.

2. When a customer purchases a product in e-commerce site, it is essential that the stock quantity is updated immediately to reflect the availability accurately.

- Inconsistent data could result in overselling products, leading to disappointed customers and potential financial losses for the business.

In both of these examples, achieving consistency is paramount for the proper functioning and reliability of the distributed data systems.

It ensures that users have the most up-to-date and accurate information, providing a seamless experience and avoiding potential errors or inconsistencies in data handling.
