"""
Example 01: Stack & Queue Basics — See LIFO and FIFO in Action
===============================================================
Chapter 22: Stacks & Queues — Order Matters

This example demonstrates:
  - Part 1: Stack (LIFO) — push, pop, peek with a Python list
  - Part 2: Queue (FIFO) — enqueue, dequeue, peek with collections.deque
  - Part 3: Stack for balanced parentheses — step-by-step trace
  - Part 4: Queue for BFS level-order — simple tree traversal
"""

from collections import deque


# ── Part 1: Stack Demo ───────────────────────────────────────────────

def part1_stack_demo():
    """Demonstrate stack (LIFO) behavior using a Python list."""
    print("=" * 60)
    print("PART 1: Stack (LIFO) — Last In, First Out")
    print("=" * 60)

    stack = []
    actions = ["push 10", "push 20", "push 30", "pop", "peek", "push 40", "pop", "pop"]

    for action in actions:
        parts = action.split()
        if parts[0] == "push":
            val = int(parts[1])
            stack.append(val)
            print(f"  push({val})  -> stack = {stack}")
        elif parts[0] == "pop":
            val = stack.pop()
            print(f"  pop()    -> returned {val}, stack = {stack}")
        elif parts[0] == "peek":
            val = stack[-1]
            print(f"  peek()   -> {val}, stack = {stack}")

    print(f"\n  Final stack: {stack}")
    print(f"  Is empty? {len(stack) == 0}")


# ── Part 2: Queue Demo ──────────────────────────────────────────────

def part2_queue_demo():
    """Demonstrate queue (FIFO) behavior using collections.deque."""
    print("\n" + "=" * 60)
    print("PART 2: Queue (FIFO) — First In, First Out")
    print("=" * 60)

    q = deque()
    actions = ["enqueue A", "enqueue B", "enqueue C", "dequeue", "peek",
               "enqueue D", "dequeue", "dequeue"]

    for action in actions:
        parts = action.split()
        if parts[0] == "enqueue":
            val = parts[1]
            q.append(val)
            print(f"  enqueue('{val}')  -> queue = {list(q)}")
        elif parts[0] == "dequeue":
            val = q.popleft()
            print(f"  dequeue()      -> returned '{val}', queue = {list(q)}")
        elif parts[0] == "peek":
            val = q[0]
            print(f"  peek()         -> '{val}', queue = {list(q)}")

    print(f"\n  Final queue: {list(q)}")


# ── Part 3: Balanced Parentheses Trace ───────────────────────────────

def part3_balanced_parens():
    """Step-by-step trace of balanced parentheses checking."""
    print("\n" + "=" * 60)
    print("PART 3: Balanced Parentheses — Stack Trace")
    print("=" * 60)

    test_cases = ["({[]})", "([)]", "((()))", "(((", ""]
    match = {')': '(', ']': '[', '}': '{'}

    for s in test_cases:
        print(f"\n  Checking: \"{s}\"")
        stack = []
        valid = True
        for ch in s:
            if ch in '([{':
                stack.append(ch)
                print(f"    '{ch}' is opening -> push -> stack = {stack}")
            elif ch in ')]}':
                if not stack or stack[-1] != match[ch]:
                    print(f"    '{ch}' is closing -> MISMATCH or empty stack!")
                    valid = False
                    break
                popped = stack.pop()
                print(f"    '{ch}' matches '{popped}' -> pop -> stack = {stack}")

        if valid and len(stack) == 0:
            print(f"  Result: VALID")
        elif valid:
            print(f"  Unmatched openers remain: {stack}")
            print(f"  Result: INVALID")
        else:
            print(f"  Result: INVALID")


# ── Part 4: Queue for BFS ────────────────────────────────────────────

def part4_bfs_demo():
    """BFS level-order traversal using a queue."""
    print("\n" + "=" * 60)
    print("PART 4: Queue for BFS — Level-Order Traversal")
    print("=" * 60)

    # Simple tree as adjacency list (undirected)
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [6],
        4: [], 5: [], 6: []
    }

    print("  Tree:")
    print("       1")
    print("      / \\")
    print("     2   3")
    print("    / \\   \\")
    print("   4   5   6")
    print()

    queue = deque([1])
    visited = {1}
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        print(f"  Dequeue {node} -> visit it -> enqueue children: {graph[node]}")
        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                queue.append(child)

    print(f"\n  BFS order: {order}")
    print("  Notice: nodes are visited level by level (1 -> 2,3 -> 4,5,6)")


# ── Main ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_stack_demo()
    part2_queue_demo()
    part3_balanced_parens()
    part4_bfs_demo()
