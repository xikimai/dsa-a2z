"""
Solution for Warmup 1: Flood Fill
============================================
Chapter 20: Graphs II — Real Problems

APPROACH
--------
BFS from (sr, sc). Change all connected same-color cells to new color.
Early return if original == color to avoid infinite revisiting.

TIME COMPLEXITY:  O(m * n)
SPACE COMPLEXITY: O(m * n)
"""

from collections import deque


def solve(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    """Flood fill starting from (sr, sc) with new color."""
    rows, cols = len(image), len(image[0])
    original = image[sr][sc]
    if original == color:
        return image

    queue = deque([(sr, sc)])
    image[sr][sc] = color
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c = queue.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original:
                image[nr][nc] = color
                queue.append((nr, nc))

    return image


# ── Do not change anything below this line ──────────────────────────
if __name__ == "__main__":
    first_line = input().split()
    rows, cols = int(first_line[0]), int(first_line[1])
    sr, sc, color = int(first_line[2]), int(first_line[3]), int(first_line[4])
    image = []
    for _ in range(rows):
        image.append(list(map(int, input().split())))
    result = solve(image, sr, sc, color)
    for row in result:
        print(" ".join(map(str, row)))
