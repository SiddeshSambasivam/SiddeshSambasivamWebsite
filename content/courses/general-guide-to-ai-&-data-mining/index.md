---
title: A General Guide to AI & Data Mining
date: 2022-09-09
math: true
diagram: true
highlight: true

reading_time: true

image:
  preview_only: true

reading_time: true
pager: true

type: page

summary: "A brief introduction to AI and Data Mining. This post covers basic concepts discussed in the course, 'IE4483: AI and Data Mining' at NTU, Singapore."


_build:
  render: always
  list: never
# _build:
  # render: always
  # list: never

---

> This post is a short summary of first half of the course, 'IE4483: AI and Data Mining' at NTU, Singapore. The course is taught by Prof. Dr. Lihui Chen.

## Introduction: AI & Search

The two most fundamental concerns of AI researchers:

1. **Knowledge representation**

   - Capturing knowledge in a way suitable for computer manipulation

   - Graphs (Powerful representation for many problems)
     - Example: Euler graph, Konigsberg bridge problem
   - ANN - Network + weights

2. **Search**

   - Systematically exploring the space of possible solutions to a problem

#### Example: The Bridges of Konigsberg Problem

{{< figure src="/blog/konigsberg--1905-13.jpg" width="500px" title="Visual depiction of the konigsberg problem">}}

Is there a walk around the city that crosses each bridge exactly once?

{{% callout note %}}

No universally superior search algorithms for all problems, also known as the "No-Free-Lunch Theorem."

{{% /callout %}}

The <u>degree</u> of a node of a graph: An _even degree node_ has an even number of arcs joining it neghbouring nodes. An _odd degree node_ has an odd number of arcs joining it to neighbouring nodes.

**Euler's conclusion**: A walk around the city that crosses each bridge exactly once is possible if and only if the {{< hl >}}graph contains **exactly 0 or 2** nodes of odd degree.{{< /hl >}}

**Another example:** Travelling Salesman Problem (TSP)

## Search Strategies

{{< figure src="/blog/AI-algos-1-e1547043543151.png" width="600px" title="Search strategies">}}

A strategy is defined by picking the order of node expansion in a graph.

Strategies are evaluated along the following dimensions:

- **Completeness**: Does the strategy always find a solution if one exists?
- **Optimality**: Does the strategy always find the best solution if one exists?
- **Time complexity**: How much time does the strategy take to find a solution?
- **Space complexity**: How much memory does the strategy require to find a solution?

Un-informed search = blind search \
Informed search = heuristic-applied search

### Strategies for State Space Search

- **Data-driven search**: Facts & rules => New facts -> ... => Goal

  - This approach is sometimes called **forward chaining**.
  - Has a branch factor
  - eg: Playing go, chess

- **Goal-driven search**: Goal => Sub goals -> ... => Facts
  - This approach is sometimes called **backward chaining**.
  - eg: Medical diagnostic

#### How to systematically search a graph?

_Why a graph?_ Very close to how we make decisions in real life.

- We use **backtracking** to systematically search a graph.
  - Depth-first search (DFS) for constraint satisfaction problem (CSP)

**Notations:**

- CS = Current state
- SL = State list
- NSL = Next state list (Unprocesses states)
- DE = Dead ends

**Breadth-first search (BFS)**

- Level order traversal of a graph

If the branching factor, B (average number of children), is large, the combinatorics may prevent the algorithm from finding a solution using the available memory.

**Depth-first search (DFS)**

- Depth-first traversal of a graph

**DFS w/ Iterative deepening search (IDS)**

- First performs a dfs on the space with a depth bound of one
- If it fails to find a goal, it performs another dfs with a depth bound of two. We **increase** the **depth bound by one** each time.

- At each iteration, the algorithm performs a complete dfs to the **current depth bound**. NO info about the state space is retained between iterations.

## Uninformed vs Informed Search Strategies

**Uninformed strategies** use only information available in the problem definition.

- Systematically generate new states
- BFS, DFS, IDS

| Criteria         | BFS    | DFS    | IDS    |
| ---------------- | ------ | ------ | ------ |
| Completeness     | Yes    | No     | Yes    |
| Optimality       | Yes    | No     | Yes    |
| Time complexity  | O(b^d) | O(b^m) | O(b^d) |
| Space complexity | O(b^d) | O(bm)  | O(bd)  |

**Informed strategies** use problem-specific knowledge to guide the search.

- Use an evaluation function to estimate the cost of a state
- A\* search, Hill climbing, Best-first (Greedy)

### Introduction: Heuristic search

**heuristic (adj.)** means based on learning from personal discoveries and experiences.

- Formulated as rules for choosing those branches in a state space that are most likely to lead to a solution.

This _increases_ the feasibility of the search process.

#### Limitations

1. A heuristic is only an informed guess.
2. Can lead a search algorithm to sub-optimal solution or fail to find any solution at all.

#### Two key components of a heuristic search

1. A heuristic function, h(n), that estimates the cost of the cheapest path from the state n to a goal state.
2. A search strategy that uses h(n) to guide the search.

#### Divising heuristics

THe evaluation function, f(n), the sum of two components:
$$f(n) = g(n)+h(n)$$

- $g(n)$: path-cost function = cost from **initial** state to **current** state _n_.
- $h(n)$: heuristic function = estimated cost of the cheapest path from _n_ to a goal state.
  - If $h(n)$ is not larger than the real cost, the search is **admissible**.

## Introduction to Data Mining and Association Analysis

- **Data** - Facts, numbers, or text that can be processed by a computer.
- **Information** - Patterns, associations, relationships, or trends that can be extracted from data.
- **Knolwedge** - Information can be converted into knowledge about historical patterns and future trends.

_Data mining_ - Processes of extracting patterns or knowledge from large amounts of data. Application areas include:

- Market or business analysis and decision support
- Text mining
- Medical and biological data analysis
- Fraud detection
- Social network analysis

### Data Mining Process

Input Data -> Data Preprocessing -> Data Mining -> Post processing -> Knowledge Discovery -> Knowledge Representation -> Knowledge Evaluation

### Data Mining Tasks

1. Predictive
   - Classification
   - Regression
   - Time-series analysis
   - Prediction
2. Descriptive
   - Association rules
   - Clustering
   - Summarization
   - Sequence discovery

### Data Mining Architecture

{{< figure width="350px" src="/blog/Architecture-of-a-typical-data-mining-system.png" title="Data Mining Architecture" >}}

### Association Analysis

- **Association analysis** - Search for relationships between items in a dataset.
  - Finding frequent patterns, correlations, or causal structures among variables in large databases.
  - Frequent pattern: A pattern that occurs frequently in a dataset.

Rule form: $X \rightarrow Y$

#### Basic Concepts

- I = {i1, i2, ..., in} is a set of items.
- T = {t1, t2, ..., tm} is a set of transactions.
- Each transaction contains a subset of items.

- Support count $\sigma(X)$: The number of transactions that contain a given itemset.
- Support $\sigma(X)/|T|$: The fraction of transactions that contain a given itemset.
  - How often a rule is applicable in a given dataset.

**Association rule** is an implication of the form $X \rightarrow Y$ where $X$ and $Y$ are itemsets; $X \cap Y = \emptyset$.

- Strength of association: Measured in terms of _support_ and _confidence_.
  - Support: $\sigma(X \cup Y)/|T|$ - Applicability of the rule in the dataset.
  - Confidence: $\sigma(X \cup Y)/\sigma(X)$ - How frequently items in $Y$ appear in transactions containing $X$. (Conditional probability)

### Frequent Itemset Generation

### Apriori Algorithm

> Write about maximal and closed frequent itemsets.

1. Find the minimum support count, $minsup=|T| \times \text{\% of min support}$.
2. Let k = 1
3. Repeat until no more frequent itemsets are found:
   1. Generate frequency count of all itemsets of size k.
   2. Prune the itemsets that do not meet the minimum support count.
      - Prune itemsets which has subsets that are not frequent.
   3. k = k + 1

### FP-Growth Algorithm

> TO BE CONTINUED

- FP-Growth compresses the dataset by representing frequent items into a FP-tree (frequent pattern tree).

* FP-Tree
* Conditional pattern base
* COnditional FP-tree for item_i

### Association Rules Evaluation

**Lift** is a simple correlation measure between two itemsets $X$ and $Y$.

$$
\begin{aligned}
\text{Lift}(X,Y) &= \frac{\text{Confidence}(X\rightarrow Y)}{\text{Support}(Y)} \\
&= \frac{\frac{\sigma(X \cup Y)}{\sigma(X)}}{\frac{\sigma(Y)}{|T|}} \\
&= \frac{P(X\cup Y)}{P(X)P(Y)}
\end{aligned}
$$

- Lift = 1: No association between X and Y.
- Lift > 1: Positive correlated between X and Y.
- Lift < 1: Negative correlated between X and Y.

- Some rules are **strong** associations; some may still not be interesting
