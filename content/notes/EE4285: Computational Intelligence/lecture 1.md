---
title: "Lecture 1: Introduction to Fuzzy Sets"
date: "2022-05-04"
type: book
weight: 20
---

A fuzzy set is totally characterised by a Membership function (MF). And is mathematically expressed as
$$S = {(x, \mu_s(x) | x\in X)}$$
The above equation is known as **characteristic equation.** Where $S$ is a fuzzy set, $\mu_s(x)$ is a membership function (MF). A membership function basically tells how much does a element belong to a set. Finally, $X$ is called the universe of discourse.

When $X$ is discrete,
$$S = \sum_{x_i \in X}\mu_S(x_i)/x_i$$
and when $X$ is continous,
$$S = \int\limits_X \mu_S(x_i)/x_i$$

### Fuzzy set operations

1. Subset/containment: $A \subseteq B \Leftrightarrow \mu_A \leq \mu_B$
2. Completement: $\mu_\bar{A}(x) = 1 - \mu_A(x)$
3. Union: $C = A \cup B \Leftrightarrow \mu_C(x) = \mu_A(x) \vee \mu_B(x)$
4. Intersection: $C = A \cap B \Leftrightarrow \mu_C(x) = \mu_A(x) \wedge \mu_B(x)$

### Fuzzy set terms

- Support => $\mu_S(x) > 0$
- Core => $\mu_S(x) = 1$
- Normality => When core set is non-empty
- Crossover => $\mu_S(x) = 0.5$
- Singleton => When Core(S) = Support(S)

### Cartesian product

When there are two fuzzy sets $A$ and $B$ in $X$ and $Y$, respectively. A operation called **cartesian product** creates a new product space $X\times Y$ for all combinations of elements in input fuzzy sets.
$$\mu_{A\times B}(x, y) = min\{\mu_A(x), \mu_B(y)\} = \mu_A(x) \wedge \mu_B(y)$$
$$A\times B \Rightarrow A \wedge B$$

### Cyclindrical Extension

It is used to deproject or deaggregate values. In other words, this operation increases the dimension of a space $1D => 2D$

{{% callout note %}}
Two important notions to understand: **dimension** and **measure.**

- Dimension are sets which define the space along which we can aggregate information (value of variables).
- Measure is a special variable which represents the aggregated information (variables).
  {{% /callout %}}

In fuzzy logic, if $A \subseteq X$ is a fuzzy set. Then cylindrical extension in the space $X\times Y$ is $$\mu_{C(A)}(x,y) := \mu_A$$

### Projection

Projection can be viewed as aggregation or consolidation of information. In other words, reduces the dimension of a space $2D => 1D$.
$$R_y = \int\limits_X max_x\{\mu_R(x,y)\}/y$$$$R_x = \int\limits_Y max_y\{\mu_R(x,y)\}/x$$

### Extension principle

A function $f: X_1\times X_2 \times ... \times X_n \rightarrow Y$ maps n-dimensions in $X$ (input space) to $Y$. Assuming that there is $A_1, A_2, ..., A_n$ fuzzy sets in $X_1, X_2,..., X_n$. The function would induce another fuzzy set in the output space $Y$ with membership function,

$$
\mu_B(y) = \begin{cases}
\max\limits_{{x_1, ..., x_n \in f^{-1}(x)}} \mu_A(x), f^{-1}(x) \neq 0 \\
0, otherwise
\end{cases}
$$

since $X = X_1\times X_2 \times ... \times X_n$ , [[#Cartesian product]] could be used to determine that,
$$\mu_A(x) = \mu_{A_1}(x) \wedge ... mu_{A_n}(x)$$
$$\mu_A = \min_i \mu_A(x)$$
Substituing the above equation in the $\mu_B(y)$ , we get that

$$
\mu_B(y) = \max_{(x_1, ..., x_n
) \in f^{-1}(x)} \min_i \mu_A(x)
$$

### Different dimension altering ops

1. Cylindrical extension => $X \rightarrow X\times Y$
2. Cartesian product => $X, Y \rightarrow X \times Y$
3. Extension principle => $X \rightarrow Y$
