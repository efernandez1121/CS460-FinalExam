# The Torchbearer

**Student Name:** Estephanie Fernandez
**Student ID:** 828470273
**Course:** CS 460 – Algorithms | Spring 2026

---

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**
  It is not enough because it only tells the cheapest cost from the entrance to each location, but the order of the relic chambers isz not decided by the single shortest-path run from S

- **What decision remains after all inter-location costs are known:**
   The decision that remains is determining which relic chamber to visit first, second, third, etc. before going to the exit.

- **Why this requires a search over orders (one sentence):**
  Different relic visit orders can have different total fuel costs; therefore, the program must compare possible orders to find the minimum.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source |
|---|---|
| Entrance node `S` | Route starts at the entrance, thus the program needs cheapest travel costs from `S` to each relic. |
| Relic chamber nodes | Program needs cheapest travel costs from that relic to the remaining relics after visiting one reli and eventually to the exit. |

### Part 2b: Distance Storage

| Property | Your answer |
|---|---|
| Data structure name | Nested dictionary |
| What the keys represent | The outer key is the source node, and the inner key is the destination node. |
| What the values represent | The minimum fuel cost from the source to  destination node. |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | `dist_table[u][v]` can be accessed directly because python dictionaries use hashing. |

### Part 2c: Precomputation Complexity

- **Number of Dijkstra runs:** `k + 1`
- **Cost per run:** `O(m log n)`
- **Total complexity:** `O((k + 1) * m log n)`
- **Justification:** One Dijkstra run is needed from the entrance and from each of the `k` relics.
---

## Part 3: Algorithm Correctness


### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
  Shortest distance from the source is known. There will be no changes.

- **For nodes not yet finalized (not in S):**
  Stored distance is the best distance found, but it may still improve.

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
  Source starts with distance 0 because there is no cost.
  Path has not been found for other nodes, thus they start at infinity.


- **Maintenance : why finalizing the min-dist node is always correct:**
  Node with the smallest current distance is safe to finalize because every other path is at least as expensive.
  Since edge weights are nonnegative, a later path cannot come back.

- **Termination : what the invariant guarantees when the algorithm ends:**
  When the algorithm ends, every reachable node has its true shortest distance and any node remains at infinity is cannor reach from the source.

### Part 3c: Why This Matters for the Route Planner

Correct distances let the route planner compare relic visit orders using the true cheapest fuel costs between locations.
---

## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:** Greedy only chooses the closest next relic and ignores future costs.
- **Counter-example setup:** From S, B costs 1, C costs 2, and D costs 2.
- **What greedy picks:** Greedy picks B first because it is the cheapest immediate move.
- **What optimal picks:** Optimal search compares all possible relic orders.
- **Why greedy loses:** A cheaper first move may lead to a more expensive total route.

### What the Algorithm Must Explore

- The algorithm must explore different relic visit orders to find the minimum total cost.
---

## Part 5: State and Search Space

### Part 5a: State Representation

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | current_loc | node | Current node being explored |
| Relics already collected | relics_visited_order | list | Relics collected so far |
| Fuel cost so far | cost_so_far | float | Current total fuel cost |


### Part 5b: Data Structure for Visited Relics

| Property | Your answer |
|---|---|
| Data structure chosen | set |
| Operation: check if relic already collected | Time complexity: O(1) |
| Operation: mark a relic as collected | Time complexity: O(1) |
| Operation: unmark a relic (backtrack) | Time complexity: O(1) |
| Why this structure fits | Sets allow fast checking and updating during recursion. |
### Part 5c: Worst-Case Search Space
- **Worst-case number of orders considered:** O(k!)
- **Why:** The algorithm needs to try every possible relic order.

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

- **What is tracked:** The minimum route cost.
- **When it is used:** Before exploring a new recursive path.
- **What it allows the algorithm to skip:** Paths that already cost more than the current best route.

### Part 6b: Lower Bound Estimation
- **What information is available at the current state:** Current location, remaining relics, and current fuel cost.
- **What the lower bound accounts for:** The minimum possible remaining travel cost.
- **Why it never overestimates:** It only uses shortest-path distances.

### Part 6c: Pruning Correctness

- _Your answer here._

- It is safe because skipped paths, which cannot become cheaper later since all edge weights are nonnegative, cost more than the best solution found.

---

## References

Lecture Notes 