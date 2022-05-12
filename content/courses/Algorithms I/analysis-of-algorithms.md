---
title: "2. Analysis of Algorithms"
date: "2021-05-09"
type: book

summary: The lecture discusses the scientific method to analyze the performance of algorithms. Computational experiments were performed to measure the running times of test programs and these measurements were used to develop hypothesis about performance.

weight: 20
---

{{% callout note %}}
**WIP:** I am still migrating the notes to this site
{{% /callout %}}

## Emperical Analysis

- Execute program to perform experiments.
- Assume power law and formulate a hypothesis for running time.
- Model enables us to make predictions.

## Mathematical Analysis

- Analyze algorithm to count frequency of operations.
- Use tilde notation to simplify analysis.
- Model enables us to explain behavior

In most trivial cases, the operations (variable declaration, assignment, comparison) are approximated to take constant time.

```java
void main(){
    int count = 0;
    for(int i=0; i<N; i++){
        for(int j=i+1; j<N; j++){
            if(a[i] + a[j] == 0)
                count ++;
        }
    }
}
```

| Operation            | Frequency                |
| -------------------- | ------------------------ |
| Variable declaration | N+2                      |
| Assignment statement | N+2                      |
| Less than compare    | $\frac{1}{2}$ (N+1)(N+2) |
| Equal to compare     | $\frac{1}{2}$ N(N-1)     |

## Scientific Method

- Mathematical model is independent of a particular system;applies to machines not yet built.
- Empirical analysis is necessary to validate mathematical models and to make predictions.
