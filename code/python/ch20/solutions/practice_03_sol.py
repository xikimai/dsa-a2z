"""
Solution for Practice 3: Pacific Atlantic Water Flow
============================================
Chapter 20: Graphs II — Real Problems

APPROACH
--------
BFS from Pacific border cells (top + left edges) and from Atlantic border
cells (bottom + right edges). Water flows from lower to higher (reverse
direction). Return cells reachable from both.

TIME COMPLEXITY:  O(m * n)
SPACE COMPLEXITY: O(m * n)
"""

from collections import deque


def solve(heights: list[list[int]]) -> list[list[int]]:
    """Return sorted list of cells that can reach both oceans."""
    if not heights or not heights[0]:
        return []

    rows, cols = len(heights), len(heights[0])
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def bfs(starts):
        reachable = set()
        queue = deque()
        for r, c in starts:
            reachable.add((r, c))
            queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if (0 <= nr < rows and 0 <= nc < cols
                        and (nr, nc) not in reachable
                        and heights[nr][nc] >= heights[r][c]):
                    reachable.add((nr, nc))
                    queue.append((nr, nc))
        return reachable

    # Pacific: top row + left column
    pacific_starts = []
    for c in range(cols):
        pacific_starts.append((0, c))
    for r in range(1, rows):
        pacific_starts.append((r, 0))

    # Atlantic: bottom row + right column
    atlantic_starts = []
    for c in range(cols):
        atlantic_starts.append((rows - 1, c))
    for r in range(rows - 1):
        atlantic_starts.append((r, cols - 1))

    pacific = bfs(pacific_starts)
    atlantic = bfs(atlantic_starts)

    result = sorted([r, c] for r, c in pacific & atlantic)
    return result


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    first_line = input().split()
    rows, cols = int(first_line[0]), int(first_line[1])
    heights = []
    for _ in range(rows):
        heights.append(list(map(int, input().split())))
    result = solve(heights)
    for cell in result:
        print(cell[0], cell[1])
