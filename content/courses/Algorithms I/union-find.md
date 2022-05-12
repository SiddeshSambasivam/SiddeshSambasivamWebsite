---
title: "1. Union-Find & Applications"
date: "2021-05-09"
type: book

Summary: The lecture discusses the union–find data type and its several implementations. Finally, union–find data type is applied to the percolation problem from physical chemistry.

weight: 10
---

{{% callout note %}}
**WIP:** I am still migrating the notes to this site
{{% /callout %}}

{{< toc hide_on="lg" >}}

## 1. Dynamic Connectivity

{{< figure src="/algorithms/union_1.png" width="350px" title="Simple connected components">}}

### 1.1 Problem statement

Given a set of objects and connections, find whether two objects are connected.

A connection between objects can be transitive, i.e object $p$ can be connected $s$ if $p$ is connected to $q$ and $q$ is connected to $s$.

**Operations:**

The following are the expected basic operators required for the desired data structure:

1. `connected() -> bool`: Check if two objects are in the same component.
2. `union() -> None`: adds a connection between two objects.

{{% callout note %}}
Therefore the goal can be summarized as following:

**Goal:** Design efficient data structure for to check the connectivity between two objects (union-find).

**Constraints:**

1. Number of objects N can be huge
2. Number of operations M can be huge
3. Find queries and union commands may be intermixed
   {{% /callout %}}

### 1.2 Modeling the objects

The fundamental aspect of designing the data structure is to suppress details that are not relevant to union-find.

There are several way to achieve this goal, however the simplest method is to model _Objects as integers_. These integers are used as an array index. Another method is to use a _symbol table_ to translate from objects to integers.

### 1.3 Modeling the connections

A connection is assumed to be an equivalence relation:

- Reflexive: $p$ is connected to $p$.
- Symmetric: if $p$ is connected to $q$, then $q$ is connected to $p$.
- Transitive: if $p$ is connected to $q$ and $q$ is connected to $r$, then $p$ is connected to $r$.

**Connected components:** Set of objects that are mutually connected.

## 2. Quick Find

<!-- ```mermaid
graph LR
A((0)) --- B((2))

B --- C((1))

B --- d((4))
e((3)) --- f((5))
```

```python

class QuickFind:

    def __init__(self, N:int) -> None:
        self.ids = [i for i in range(N)]
        self.N = N

    def find(self, p:int, q:int) -> bool:
        """Check if p and q are connected"""
        return self.ids[p] == self.ids[q]

    def union(self, p:int, q:int) -> None:
        """Merge objects containing p and q"""

        pid = self.ids[p]
        qid = self.ids[q]

        for id in self.ids:
            if self.ids[id] == pid:
                self.ids[id] = qid

``` -->

## 3. Quick Union

## 4. Improvements

### 4.1 Weighted Quick Union

### 4.2 Weighted Quick Union with path compression

## 5. Applications
