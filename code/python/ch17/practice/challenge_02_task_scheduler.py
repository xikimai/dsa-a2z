"""
Challenge 2: Task Scheduler
===============================
Chapter 17: Heaps & Priority Queues — The VIP Line

PROBLEM
-------
Given a list of tasks represented by characters and a cooldown period n,
find the minimum number of intervals the CPU will take to finish all tasks.
The CPU can either execute a task or be idle. The same task must have at
least n intervals between two executions.

INPUT FORMAT
------------
Line 1: space-separated characters (tasks)
Line 2: integer n (cooldown)

OUTPUT FORMAT
-------------
A single integer — minimum intervals needed.

CONSTRAINTS
-----------
- 1 <= len(tasks) <= 10^4
- tasks[i] is an uppercase English letter
- 0 <= n <= 100

EXAMPLES
--------
Input:
  A A A B B B
  2
Output: 8
Explanation: A B _ A B _ A B (8 intervals)

Input:
  A A A B B B
  0
Output: 6
Explanation: No cooldown needed.

Input:
  A A A A A A B C D E
  2
Output: 16

HINT
----
Use a max-heap of task frequencies. Each round, pick up to (n+1) tasks
from the heap (the most frequent ones). If there are still tasks left
after the round, the round took (n+1) intervals. The last round may
be shorter.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(tasks: list[str], n: int) -> int:
    """Return minimum intervals to complete all tasks with cooldown n."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    tasks = input().strip().split()
    n = int(input().strip())
    print(solve(tasks, n))
