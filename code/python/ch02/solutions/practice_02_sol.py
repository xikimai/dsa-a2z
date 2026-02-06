"""
Solution for Practice 02: Time Conversion
============================================
Chapter 2: Your First Programs

This is the reference solution. Try to solve the problem yourself before
looking at this!

APPROACH
--------
Use integer division (//) and modulo (%) to break total seconds into
hours, minutes, and seconds:
    hours   = total // 3600
    minutes = (total % 3600) // 60
    seconds = total % 60

The key insight is that % 3600 gives the leftover seconds after
removing full hours, and then // 60 converts those to minutes.

TIME COMPLEXITY:  O(1) — just arithmetic
SPACE COMPLEXITY: O(1) — no extra memory used
"""


def solve(total_seconds: int) -> tuple[int, int, int]:
    """Return a tuple (hours, minutes, seconds) from the given total seconds."""
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return (hours, minutes, seconds)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    total_seconds = int(input())
    h, m, s = solve(total_seconds)
    print(h, m, s)
