"""
Solution for Practice 5: Remove All Adjacent Duplicates in String
=====================================================================
Chapter 22: Stacks & Queues — Order Matters

APPROACH
--------
Use a stack. For each character, if it matches the stack top, pop (remove pair).
Otherwise push. The stack contents form the final string.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
"""


def solve(s: str) -> str:
    """Remove all adjacent duplicates and return the result."""
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return ''.join(stack)


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    s = input().strip()
    print(solve(s))
