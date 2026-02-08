"""
Solution for Practice 2: Evaluate Reverse Polish Notation
=============================================================
Chapter 22: Stacks & Queues — Order Matters

APPROACH
--------
Push numbers onto a stack. On an operator, pop two operands,
compute result, push back. Division truncates toward zero.

TIME COMPLEXITY:  O(n)
SPACE COMPLEXITY: O(n)
"""


def solve(tokens: list[str]) -> int:
    """Evaluate the RPN expression and return the result."""
    stack = []
    ops = {'+', '-', '*', '/'}
    for token in tokens:
        if token in ops:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                # Truncate toward zero (not floor division)
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[0]


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    tokens = input().strip().split()
    print(solve(tokens))
