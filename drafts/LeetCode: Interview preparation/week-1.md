---
title: "Graphs and advanced graphs"
date: "2022-07-29"
type: book
weight: 20
toc: true
_build:
  render: always
  list: never
---

{{< toc >}}

### 133. Clone Graph

### 994. Rotting Oranges

You are given an `m x n` grid where each cell can have one of three values:

- 0 representing an empty cell,
- 1 representing a fresh orange, or
- 2 representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return _the minimum number of minutes that must elapse until no cell has a fresh orange._ If this is impossible, return -1.

Example:

{{< figure src="/leetcode/rotting_oranges_1.png" title="Image from https://leetcode.com/problems/rotting-oranges/" >}}

##### Key Ideas

- An easy way to iterate level by level is to use an inner loop to iterate `k` number of times, where `k` is length of the queue at the start of inner loop.
  <br/><br/>

  ```python
  while queue:
      q_len = len(queue)
      for _ in range(q_len):
          ... # do something

  ```

  This formulation can be used for _multi-source BFS._

- Use a counter variable to track the number of fresh oranges

{{< spoiler text="Code" >}}

```python
from collections import deque
from itertools import product

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        time_step = 0
        fresh_oranges = 0
        m,n = len(grid), len(grid[0])

        DIRECTIONS = [(1,0), (0,1), (-1, 0), (0, -1)]
        check_valid_coord = lambda x, y: x >=0 and x < m and y >= 0 and y < n
        queue = deque([])

        for i,j in product(range(m), range(n)):
            if grid[i][j] == 2:
                queue.append((i,j))
            if grid[i][j] == 1:
                fresh_oranges += 1

        while queue and fresh_oranges > 0:

            time_step += 1
            q_len = len(queue)
            for _ in range(q_len):
                x,y = queue.popleft()

                for dx, dy in DIRECTIONS:
                    xx,yy = x+dx, y+dy
                    if check_valid_coord(xx,yy) and grid[xx][yy] == 1:
                        grid[xx][yy] = 2
                        queue.append((xx,yy))
                        fresh_oranges -= 1

        if fresh_oranges > 0:
            return -1

        return time_step
```

{{< /spoiler >}}

**Time complexity:** `O(m*n)`, where `m` is the number of rows and `n` is the number of columns. \
**Space complexity:** `O(m*n)`, in worst case, the queue is filled with all the coordinates in the grid.

### 684. Redundant Connection

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with `n` nodes labeled from 1 to n, with one additional edge added. The added edge has two **different** vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array `edges` of length n where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the graph.

Return an edge that can be removed so that the resulting graph is a tree of `n` nodes. If there are multiple answers, return the answer that occurs last in the input.

Example 1:

{{< figure src="/leetcode/redundant_connection_1.jpg" title="Image from https://leetcode.com/problems/redundant-connection/" >}}

Answer: `[1,4]`

#### Key Ideas

- Represent the graph as an adjacency list
- Maintain a results list, which contains the edges that can be removed.
- Iterate through the edges
- If two nodes are already connected, add the edge to results list
  - else: connect the nodes with the edge
- return the last element in the results list

{{< spoiler text="Code">}}

```python
from collections import defaultdict, deque

class Graph:

    def __init__(self, N:int) -> None:
        self.N = N
        self.edges = defaultdict(list)

    def connect(self, p:int, q:int) -> None:
        self.edges[p].append(q)
        self.edges[q].append(p)

    def is_connected(self, p:int, q:int) -> bool:

        if p in self.edges[q]:
            return True

        queue = deque([p])
        visited = set()

        while queue:

            node = queue.popleft()
            visited.add(node)

            if node == q:
                return True

            for child in self.edges[node]:
                if child not in visited:
                    queue.append(child)
                    visited.add(child)

        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        g = Graph(n)

        result = []
        for edge in edges:

            p = edge[0]
            q = edge[1]

            connected = g.is_connected(p,q)
            if connected is False:
                g.connect(p,q)
                continue

            result.append(edge)

        return result[-1]

```

{{< /spoiler >}}

**Time complexity:** `O(n^2)`, \
**Space complexity:** `O(n^2)`.
