# Coding Algorithms

Coding Algorithms

Author

Benedict Thekkel

| Category | Algorithm | Why It’s Useful | Python Example |
|:---|:---|:---|:---|
| Searching | Binary Search | Fast lookup in sorted data | ✅ |
| Sorting | Quick Sort | Sorting efficiently | ✅ |
| Recursion/DP | Fibonacci (Memoization) | Dynamic Programming intro | ✅ |
| Greedy | Dijkstra’s Algorithm | Shortest path finding | ✅ |
| Graphs | BFS / DFS | Navigating networks, trees | ✅ |
| Sliding Window | Max Subarray Sum | Real-time analytics, optimization | ✅ |
| Divide & Conquer | Merge Sort | Balanced sorting | ✅ |
| Trees | Lowest Common Ancestor (LCA) | Tree queries (databases, filesystems) | ✅ |
| Hashing | Two Sum | Fast lookups using hashmaps | ✅ |
| Union-Find (DSU) | Kruskal’s Algorithm | Group connectivity (e.g., social networks) | ✅ |

------------------------------------------------------------------------

### 1. **Binary Search**

``` python
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

------------------------------------------------------------------------

### 2. **Quick Sort**archete

``` python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)
```

------------------------------------------------------------------------

### 3. **Fibonacci (Memoized)**

``` python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```

------------------------------------------------------------------------

### 4. **Dijkstra’s Algorithm**

``` python
import heapq

def dijkstra(graph, start):
    heap = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    while heap:
        curr_distance, node = heapq.heappop(heap)
        if curr_distance > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            distance = curr_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return distances
```

------------------------------------------------------------------------

### 5. **Breadth-First Search (BFS)**

``` python
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

------------------------------------------------------------------------

### 6. **Sliding Window (Max Subarray Sum)**

``` python
def max_subarray_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum
```

------------------------------------------------------------------------

### 7. **Merge Sort**

``` python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
```

------------------------------------------------------------------------

### 8. **Lowest Common Ancestor (LCA) in Binary Tree**

``` python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    return root if left and right else left or right
```

------------------------------------------------------------------------

### 9. **Two Sum (Hashing)**

``` python
def two_sum(nums, target):
    seen = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], idx]
        seen[num] = idx
```

------------------------------------------------------------------------

### 10. **Union-Find (Disjoint Set Union - DSU)**

``` python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)
```

------------------------------------------------------------------------

## 🌟 If I had to recommend **learning priority**:

| Priority | Learn First…                         |
|:---------|:-------------------------------------|
| 1        | Binary Search, BFS/DFS               |
| 2        | Sliding Window, Two Sum              |
| 3        | Quick Sort, Merge Sort               |
| 4        | Dijkstra, Union Find                 |
| 5        | LCA (Trees), Fibonacci (Memoization) |

------------------------------------------------------------------------

Back to top
