"""
Solution for Challenge 2: Course Schedule
==========================================
Chapter 19: Graphs I — Exploring Networks

APPROACH
--------
Cycle detection in a directed graph using DFS with three states:
  0 = UNVISITED, 1 = IN_PROGRESS, 2 = DONE
If we encounter an IN_PROGRESS node during DFS, there's a cycle.
If there's a cycle, we can't finish all courses.

TIME COMPLEXITY:  O(V + E)
SPACE COMPLEXITY: O(V + E)
"""


def solve(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """Return True if all courses can be finished (no cycle)."""
    adj = [[] for _ in range(numCourses)]
    for a, b in prerequisites:
        adj[b].append(a)  # b -> a (b must come before a)

    # 0=unvisited, 1=in_progress, 2=done
    state = [0] * numCourses

    def has_cycle(node):
        state[node] = 1  # in progress
        for neighbor in adj[node]:
            if state[neighbor] == 1:
                return True  # cycle found
            if state[neighbor] == 0:
                if has_cycle(neighbor):
                    return True
        state[node] = 2  # done
        return False

    for course in range(numCourses):
        if state[course] == 0:
            if has_cycle(course):
                return False

    return True


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    parts = input().strip().split()
    numCourses, m = int(parts[0]), int(parts[1])
    prerequisites = []
    for _ in range(m):
        a, b = map(int, input().strip().split())
        prerequisites.append([a, b])
    print(solve(numCourses, prerequisites))
