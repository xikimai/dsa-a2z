"""
Solution for Warmup 1: Valid Parentheses
============================================
Chapter 22: Stacks & Queues — Order Matters

APPROACH
--------
Use a stack: push opening brackets, pop on closing brackets and check match.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
"""


def solve(s: str) -> bool:
    """Return True if brackets are balanced."""
    stack = []
    match = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != match[ch]:
                return False
            stack.pop()
    return len(stack) == 0


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input().strip()
    print(solve(s))
