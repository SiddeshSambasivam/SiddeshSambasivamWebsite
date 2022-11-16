---
title: "1. Unsuperised Learning - Clustering & Regression"
date: "2022-11-06"
type: book

summary: " "

weight: 10
---

### A. Concept of Clustering

Clustering is (typically) an _unsupervised learning_ method.

- Learns the **intrinsic patterns** in the data without pre-defined labels

Given a collection of points, the goal is to group/organize the data such that data in the same group are more similar to each other, than to those in other group.

{{% callout note %}}

**Cluster:** A set of data which are similar to each other.

**Cluster Center:** The center of a cluster, which is the average of all the data points in the cluster.

{{% /callout %}}

### B. Distance Measures

We define the distance between any two data samples $x^i$ and $x^j$ as:

$$d(x^i, x^j) \rightarrow R \\ (\text{real scalar})$$

The conditions that needs to be satisfied for a valid distance measure are:

1. $d(x^i, x^j) \geq 0$ $\vee$ $x^i$ and $x^j$
2. $d(x^i, x^j) + d(x^j, x^k) \geq d(x^i, x^k)$ $\vee$ $x^i$, $x^j$ and $x^k$

The most common distance measures are:

1. **Euclidean Distance** (Used in this course)
2. Manhattan Distance
3. Infinity Norm

### C. K-Means Clustering

{{< spoiler text="Types of clustering algorithms" >}}

1. _Partition algorithms_: Cluster the data samples into non-overlapping subsets

   1. **K-Means**
   2. Mixture of Gaussian
   3. Spectral Clustering

2. _Hierarchical algorithms_: A set of nested clusters organized as a hierarchical tree
   1. **Agglomerative**
   2. Divisive

{{< /spoiler >}}

K-Means clustering is a simple and popular clustering algorithm.

Given a set of data samples $x^1, x^2, \dots, x^N$, the goal is to partition the data samples into $K$ clusters.

Clustering goal:

1. Split the data samples into $K$ clusters.
2. Each cluster has a d-dimensional centroid / center $\mu^k$.
3. The sum of distances b/w each $x^i$ and its cluster center $\mu^k$ is minimized.

{{% callout warning %}}

**Limitation of K-Means:** The number of clusters $K$ needs to be specified beforehand.

{{% /callout %}}

- $\mu^k$ is the average of all the data samples in cluster $k$.
- usually **Euclidean distance** is used as the distance measure

#### 1. Algorithm

1. Randomly initialize $K$ cluster centers $\mu^1, \mu^2, \dots, \mu^K$.
2. Repeat until convergence:
   1. Assign each data sample, $x^i$ ,to the closest cluster center $\mu^k$.
   2. Update the cluster centers $\mu^k$ to be the average of all the data samples in cluster $k$.
3. Stopping criteria: No points' assignments change.

#### 2. Cost Function

$$
min_{\mu_k}min_{r_{ik}}\sum_{i=1}^N\sum_{k=1}^K \frac{1}{2}r_{ik}||x^i - \mu^k||^2_2
$$

- $r_{ik}$ is a binary variable that indicates whether $x^i$ is assigned to cluster $k$ or not.

#### 3. Pros & Cons

- Pros

  - Simple and effective
  - Easy to implement

- Cons
  - Need to specify the number of clusters $K$ beforehand
  - Stuck in **poor local minima**
  - Need appropriate distance measure
  - Sensitive to outliers
  - Sensitive to initial cluster centers

### D. Hierarchical Agglomerative Clustering (HAC)

Hierarchical clustering is a clustering algorithm that builds a hierarchy of clusters.

- Start with the points as individual clusters.
- At each step, merge the closest pair of clusters, until only one cluster left (or K clusters). K is a user-defined.

_How to merge?_ Merge the pair of clusters with the minimum distance.

#### 1. Algorithm

1. Start with each data sample as a cluster.
2. Iterate until only K cluster left:
   1. Find the pair of clusters with the minimum distance.
   2. Merge the pair of clusters into a new cluster.
3. Stopping criteria: Only K clusters left.

HAC can be visualized as a **dendrogram**.

{{< figure src="/aim/dendo.png">}}

- **Distance:**
  - **Min/Single linkage:** The minimum distance between any two points in the two clusters.
  - **Max/Complete linkage:** The maximum distance between any two points in the two clusters.
  - **centroid linkage:** The distance between the centroids of the two clusters.
  - **average linkage:** The average distance between any two points in the two clusters.

#### 2. Pros & Cons

- Pros

  - Deterministic
  - No need to specify the number of clusters $K$ beforehand
    - Can just stop at any level of the dendrogram to get the desired number of clusters
  - Easy to interpret

- Cons
  - More memory and computation intensive than K-Means

#### 3. Problem solving

1. Create the distance table
2. Select the smallest off-disgonal value. Merge the corresponding pair.
