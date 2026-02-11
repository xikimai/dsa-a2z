"""
Warmup 3: Simulate Robot Moves
================================
Chapter 13: Bronze Battle Plan — Putting It All Together

PROBLEM
-------
A robot starts at position (0, 0) on a 2D grid. Given a string of
commands ('U' = up, 'D' = down, 'L' = left, 'R' = right), return
the robot's final [x, y] position.

INPUT FORMAT
------------
A single string of characters from {U, D, L, R}.

OUTPUT FORMAT
-------------
A list [x, y] representing the final position.

CONSTRAINTS
-----------
- 0 <= len(commands) <= 10^4
- Each character is one of 'U', 'D', 'L', 'R'

EXAMPLES
--------
Input:
  RRRUUU
Output: [3, 3]

Input:
  UUDDLR
Output: [0, 0]

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
The main block at the bottom handles input/output — don't change it.
"""


def solve(commands: str) -> list[int]:
    """Return final [x, y] position after executing all commands."""
    pass  # TODO: Replace this with your solution



# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    commands = input().strip()
    print(solve(commands))

