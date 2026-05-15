# Development Log – The Torchbearer

**Student Name:** Estephanie Fernandez
**Student ID:** 828470273
---

## Entry 1 – [5/9]: Initial Plan

Just finished reading the assignment instructions and looking through all the TODO functions in torchbearer.py. Today I'll mostly just review instructions and documents. Haven't created a new repository, but I downloaded the files from the given GitHub. Currently, I plan to first implement Dijkstra’s algorithm and distance precomputation before working on the recursive search. I expect the recursive backtracking and pruning logic to be the hardest part. I planned to test the program using the provided test cases after each section was completed (that much is a given).

---

## Entry 2 – [5/10]: Dijkstra

Wasn't able to make much progress the past few days. Anyways, started implementing the Dijkstra and precomputation sections today. There was an issue I ran into while doing all this which was figuring out how to store all shortest-path distances in a way that would be easy to access later during the recursive search. I had initially considered recomputing Dijkstra multiple times during recursion; however, that would have been too slow. I changed the design to use a nested dictionary (`dist_table`) so distances could be looked up quickly. Worked also on the README questions.

---

## Entry 3 – [5/14]: Testing and Cleanup

After implementing all functions, I ran the provided tests to check correctness. One issue I checked for was handling unreachable paths correctly using float('inf'). I also added some comments, not very good ones but that'll do, and cleaned up variable names so they matched the README requirements. I also finished up the last of the questions from the README.

---

## Entry 4 – [5/14]: Post-Implementation Reflection

Currently feeling like those scientists from Resident Evil who log all their experiments in journal entries. If I had more time, I would improve the search algorithm by adding a stronger lower-bound estimate for pruning. That way, I could reduce the number of recursive paths explored and improve efficiency. Can't really think of anything else. Created the Github repository so that I can submit my assignment.

---

## Final Entry – [5/14]: Time Estimate

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 0.5 (ish) |
| Part 2: Precomputation Design | 3 |
| Part 3: Algorithm Correctness | 1 |
| Part 4: Search Design | 1 |
| Part 5: State and Search Space | 1 |
| Part 6: Pruning | 2 |
| Part 7: Implementation | 6 |
| README and DEVLOG writing | 2 |
| **Total** | **16.5** |
