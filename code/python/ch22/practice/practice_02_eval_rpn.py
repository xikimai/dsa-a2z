"""
Practice 2: Evaluate Reverse Polish Notation
================================================
Chapter 22: Stacks & Queues — Order Matters

PROBLEM
-------
Evaluate an arithmetic expression in Reverse Polish Notation (postfix).
Valid operators are +, -, *, /. Division truncates toward zero.

CONSTRAINTS
-----------
- 1 <= len(tokens) <= 10^4
- Each token is either an integer or one of '+', '-', '*', '/'

EXAMPLES
--------
Input: ["2","1","+","3","*"]
Output: 9   (i.e., (2+1)*3)

Input: ["4","13","5","/","+"]
Output: 6   (i.e., 4+(13/5) = 4+2 = 6)

HINT
----
Push numbers onto a stack. When you see an operator, pop two, compute, push result.

INSTRUCTIONS
------------
Replace the `pass` in the solve() function with your solution.
"""


def solve(tokens: list[str]) -> int:
    """Evaluate the RPN expression and return the result."""
    pass  # TODO: Replace this with your solution


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    tokens = input().strip().split()
    print(solve(tokens))
