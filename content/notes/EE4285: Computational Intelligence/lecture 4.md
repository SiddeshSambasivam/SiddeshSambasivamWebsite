---
title: "Lecture 4: Fuzzy Inference System"
date: "2022-05-04"
type: book
weight: 20
---

**General definition:** A computing framework based on the concepts of fuzzy set theory, fuzzy if-then rules, and fuzzy reasoning.

**Interpretation:** Specifically, it is a framework used to model and infer the behaviour of a system. There two important parts:

1. Encoding knowledge as a set of if-then rules
2. Predict the system behaviour using the encoded knowledge

The basic structure of FIS are as follows:

1. Inputs
   - Can be fuzzy or crisp
2. Outputs
   - Always almost fuzzy set
3. Rule Base
   - Number of fuzzy if-then rules, each describing local behavior mapping
4. Reasoning Mechanism

{{% callout note %}}
**Note on rule base**

If a antecedent has two different consequences, then the rule base is considered to be inconsistent.
{{% /callout %}}

### Reasoning Mechanism: Defuzzification

Extracting a crisp value from a fuzzy set. The method of interest for the course are as follow:

##### Centroid of Area (COA) or Centre of Gravity (COG)

$$Z_{COG} = \frac{\int_z \mu_A(z)zdz}{\int_z \mu_A(z)dz}$$
Where $z$ is represents the position on the bar and $\mu_A(z)$ represents the density.
