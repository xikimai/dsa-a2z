"""
Solution for Warmup 3: Simulate Robot Moves
============================================
Chapter 13: Bronze Battle Plan — Complete Search & Simulation

APPROACH
--------
Walk through each command and update (x, y).

TIME COMPLEXITY:  O(n) where n = len(commands)
SPACE COMPLEXITY: O(1)
"""


def solve(commands: str) -> list[int]:
    """Return final [x, y] position after executing all commands."""
    x, y = 0, 0
    for cmd in commands:
        if cmd == 'U':
            y += 1
        elif cmd == 'D':
            y -= 1
        elif cmd == 'L':
            x -= 1
        elif cmd == 'R':
            x += 1
    return [x, y]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    commands = input().strip()
    print(solve(commands))
