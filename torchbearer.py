"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Estephanie Fernandez
Student ID:   828470273

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    """
    return """
    - Why a single shortest-path run from S is not enough:
    It is not enough because it only tells the cheapest cost from the entrance to each location, but the order of the relic chambers is not decided by the single shortest-path run from S.

    - What decision remains after all inter-location costs are known:
    The decision that remains is determining which relic chamber to visit first, second, third, etc. before going to the exit.

    - Why this requires a search over orders:
    Different relic visit orders can have different total fuel costs; therefore, the program must compare possible orders to find the minimum.
    """


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    # Selects all nodes used as Dijkstra sources.
    sources = []
    # add the spawn node first
    sources.append(spawn)
    # if it is not already included then add every relic 
    for relic in relics:
        if relic not in sources:
            sources.append(relic)
    return sources


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    # Runs Dijkstra's algorithm.
    # Returns the cheapest distance to every node.
    # store shortest known distances
    distances = {}
    for node in graph:
        distances[node] = float('inf')
    distances[source] = 0
    pq = [(0, source)]
    while pq:
        # get node with smallest distance
        current_distance, current_node = heapq.heappop(pq)
        # skip if  better path is found 
        if current_distance > distances[current_node]:
            continue
        # check all neighbors
        for neighbor, cost in graph[current_node]:
            # calculate new possible distance
            new_distance = current_distance + cost
            # update if shorter path found
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))
    return distances



def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    dist_table = {}
    sources = select_sources(spawn, relics, exit_node)
    # run Dijkstra from every source
    for source in sources:
        # store all shortest distances for this source
        dist_table[source] = run_dijkstra(graph, source)
    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    """
    return """
    - For nodes already finalized:
    Shortest distance from the source is known. There will be no changes.

    - For nodes not yet finalized:
    Stored distance is the best distance found, but it may still improve.

    - Initialization:
    Source starts with distance 0 because there is no cost. Path has not been found for other nodes, thus they start at infinity.

    - Maintenance:
    Node with the smallest current distance is safe to finalize because every other path is at least as expensive. Since edge weights are nonnegative, a later path cannot come back.

    - Termination:
    When the algorithm ends, every reachable node has its true shortest distance and any node that remains at infinity cannot be reached from the source.

    - Why this matters:
    Correct distances let the route planner compare relic visit orders using the true cheapest fuel costs between locations.
    """


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    """
    return """
    - The failure mode:
     Greedy only chooses the closest next relic and ignores future costs.

    - Counter-example setup:
    From S, B costs 1, C costs 2, and D costs 2.

    - What greedy picks:
    Greedy picks B first because it is the cheapest immediate move.

    - What optimal picks:
    Optimal search compares all possible relic orders.

    - Why greedy loses:
    A cheaper first move can lead to a more expensive total route later.

    - What the algorithm must explore:
    The algorithm must explore different relic visit orders to find the minimum total cost.
    """


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    # Finds the cheapest order
    # stores best cost/best order found 
    best = [float('inf'), []]
    # use a set for fast lookup/removal
    relics_remaining = set(relics)
    _explore(
        dist_table,
        spawn,
        relics_remaining,
        [],
        0,
        exit_node,
        best
    )
    return best[0], best[1]


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    # pass
    #Recursive search
    # base case
    if len(relics_remaining) == 0:
        final_cost = cost_so_far + dist_table[current_loc][exit_node]
        # update best solution if cheaper
        if final_cost < best[0]:
            best[0] = final_cost
            best[1] = relics_visited_order.copy()
        return

    # pruning 
    # If current cost is already worse than the best solution,
    # this path cannot become optimal later.
    if cost_so_far >= best[0]:
        return
    for relic in list(relics_remaining):
        # get travel cost to next relic
        next_cost = dist_table[current_loc][relic]
        if next_cost == float('inf'):
            continue
        relics_remaining.remove(relic)
        relics_visited_order.append(relic)
        _explore(
            dist_table,
            relic,
            relics_remaining,
            relics_visited_order,
            cost_so_far + next_cost,
            exit_node,
            best
        )

        # backtrack
        relics_remaining.add(relic)
        relics_visited_order.pop()


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    #pass
    # precompute shortest distances
    dist_table = precompute_distances(
        graph,
        spawn,
        relics,
        exit_node
    )
    # find best relic order
    return find_optimal_route(
        dist_table,
        spawn,
        relics,
        exit_node
    )


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()

