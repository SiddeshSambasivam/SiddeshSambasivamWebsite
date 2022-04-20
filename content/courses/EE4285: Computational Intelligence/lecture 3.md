---
title: "Lecture 3: Fuzzy If-then & Fuzzy Reasoning"
date: "2021-04-18"
type: book
weight: 20
---

### Fuzzy If-then rule

Fuzzy If-then rules basically encodes fuzzy relations.

If $x$ is $A$, then $y$ is $B$.

In $A$ and $B$ are linguistic values defined by fuzzy sets on universes of discourse $X$ and $Y$. $x$ is $A$ => **Antecedent** / premise ; $y$ is $B$ => **Consequence** / conclusion

### Fuzzy Reasoning (aka) Generalised Modus Ponens

{{% callout note %}}
Fuzzy If-then rule $\subseteq$ Fuzzy relation $=$ Fuzzy set
{{% /callout %}}

Existing information are encoded as rules using the [[#Fuzzy If-then rule]] and is used to make real-time inference. _But the question is how to decode the encoded information?_

There are various methods for decoding, a few popular ones are shown below

**1. Mamdani’s implication**
$$R = A \rightarrow B = A \times B = \int\limits_{X\times Y}\mu_A(x)\wedge \mu_B(y) / (x,y)$$

**2. Zadeh’s max-min implication**
$$R = A \rightarrow B = \int\limits_{X\times Y}(1-\mu_A(x))\vee \mu_A(x)\wedge \mu_B(y) / (x,y)$$

But for the course, only **Mamdani's interpretation** is used for decoding. However, a more generalised form this decoding processes (inference process) is called _compositional rule of inference._ This is explained by the below image.

<!-- ![[fuzzy_inference.png]] -->

#### Single Rule With Single Antecedent

A rule signifies the existing encoded information (If $x$ is $A$, then $y$ is $B$). On the other hand, antecedent is the fact that is provided to be inferred ($x$ is $A^`$).

In such cases,

$$\mu_{B^{'}}(y) =  \mu_{A^{'}}(x) \circ (A \rightarrow B)$$

$$\mu_{B^{'}}(y) =  \vee_x[ \mu_{A^{'}}(x) \wedge \mu_{A}(x) \wedge \mu_{B}(y)]$$

$$\mu_{B^{'}}(y) =  [\vee_x(\mu_{A^{'}}(x) \wedge \mu_{A}(x))] \wedge \mu_{B}(y)$$

{{% callout note %}}
**Degree of match or Degrees of compatibility**

$$w = \vee_x(\mu_{A^{'}}(x) \wedge \mu_{A}(x))$$

$w$ is the degree of match between the $A$ and $A^{'}$
{{% /callout %}}

#### Single Rule With Multiple Antecedent

**Rules:** If $x$ is $A$ and $y$ is $B$, then $z$ is $C$

**Antecedent:** $x$ is $A^{'}$ **and** $y$ is $B^{'}$

$\mu_{C^{'}}(z) =  [\vee_x(\mu_{A^{'}}(x) \wedge \mu_{A}(x))] \wedge [\vee_y(\mu_{B^{'}}(y) \wedge \mu_{B}(y))] \wedge \mu_{C}(z)$

$$W_1 = \vee_x(\mu_{A^{'}}(x) \wedge \mu_{A}(x))$$

$$W_2 = \vee_y(\mu*{B^{'}}(y) \wedge \mu\_{B}(y))$$

{{% callout note %}}
Always check if the multiple antecedent are "and" or "or". Based on the which the operator between the firing weights ($W_i$) need to be used.
{{% /callout %}}

#### Multiple Rules With Multiple Antecedent

**Rules:**

1. $A_1 \times B_1 \rightarrow C_1$
2. $A_2 \times B_2 \rightarrow C_2$

**Antecedent:**

1. $x$ is $A^{'}$ and $y$ is $B^{'}$

$$\mu_{C^{'}}(z) = (A^{'} \times B^{'}) \circ (R_1 \vee R_2)$$

$$\mu_{C^{'}}(z) = ((A^{'} \times B^{'}) \circ R_1 )\vee((A^{'} \times B^{'}) \circ R_2)$$

### Defuzzification

#### Centroid of Area (COA) or Centre of Gravity (COG)

#### Largest of Maximum (LOM)
