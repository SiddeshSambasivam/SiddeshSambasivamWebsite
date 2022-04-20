---
title: "Lecture 2: Fuzzy Relations & Compositions"
date: "2021-04-18"
type: book
weight: 20
---

### Fuzzy Relations

**Binary relation:** When there are two universe of discourse $X \times Y$ , then a fuzzy relation is defined as
$$R = \{((x, y), \mu_{R}(x,y))| (x,y) \in X \times Y\}$$

{{% callout note %}}
Fuzzy relations are just multi-dimensional fuzzy sets.
{{% /callout %}}

#### Composition

When there are two fuzzy relations, defined $R_1 = X \times Y$ and $R_2 = Y \times Z$. Then a new fuzzy relation can be formed by performing projection on to the _common space_.
$$R:= R_1 \circ R_2 \subseteq X \times Z$$
$$\mu_R(x, z) = \max_y \min[\mu_{R_1}(x, y), \mu_{R_2}(y,z)]$$
$$R_1 \circ R_2 = \vee_y[\mu_{R_1}(x, y) \wedge \mu_{R_2}(y,z)]$$

##### Max-min composition

$$R_1 \circ R_2 = \vee_y[\mu_{R_1}(x, y) \wedge \mu_{R_2}(y,z)]$$

##### Max-product composition

$$R_1 \circ R_2 = \vee_y[\mu_{R_1}(x, y) \cdot \mu_{R_2}(y,z)]$$

{{% callout note %}}
Set operations are performed in the same dimension. On the other hand, set compositions are performed in different dimensions.
{{% /callout %}}

### Linguistic variables and values

{{% callout note %}}

**Principle of incompatibility**

As the complexity of the system _increases_, our ability to make precise and yet significant statements about its behaviour _diminishes_ until a threshold is reached.

Beyond the threshold, precision and significance become almost mutually exclusive characteristics.
{{% /callout %}}

Therefore, _Zadeh_ proposed an approach in an approximate manner, to summarise information and express it in terms of fuzzy sets.

A _linguistic variable_ is a quintuple $(x, T(x), X, G, M)$

- $x$ => Name of the variable
- $T(x)$ => Term set consisting of linguistic values or terms
- $X$ => Universe of discourse
- $G$ => Syntactic rule, which generates terms in T(x)
- $M$ => Semantic rule, which maps each linguistic value $T(x)$ to a fuzzy set in $X$

> **Example:** > _Age_ is linguistic variable (Note: name of the variable is "Age")
>
> T(_Age_) = {young, old, ..., very old, not very young}
>
> $X = [0, 100]$

### Operations on linguistic variables

##### a. Exponential

$$
A^k = \int\limits_{X} [\mu_A(x)]^k/x
$$

##### b. Concentration

$$
CON(A) = A^2
$$

##### c. Dilation

$$DIL(A) = A^{0.5}$$

##### d. Contrast Intensification

$$
INT(A) = \begin{cases}
2A^2, 0\leq u_A(x) \leq 0.5\\
\neg2(\neg A^2), 0.5 < u_A(x) \leq 1
\end{cases}
$$
