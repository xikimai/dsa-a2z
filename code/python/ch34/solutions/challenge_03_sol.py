"""
Solution for Challenge 3: Rectangle Union Area (Sweep Line)
=============================================================
Chapter 34: Computational Geometry & Sweep Line

APPROACH
--------
Sweep line with coordinate compression:
1. Collect all y-coordinates and compress them
2. Create events: +1 at left edge, -1 at right edge
3. Sort events by x-coordinate
4. Sweep left to right; between consecutive x-events, compute
   total active y-length using a coverage count array
5. Area += x_delta * active_y_length

TIME COMPLEXITY:  O(n^2) with simple coverage counting
SPACE COMPLEXITY: O(n)
"""


def solve(rectangles: list[list[int]]) -> int:
    """Return total area of union of rectangles."""
    if not rectangles:
        return 0

    # Collect all y-coordinates for compression
    ys = set()
    events = []
    for x1, y1, x2, y2 in rectangles:
        ys.add(y1)
        ys.add(y2)
        events.append((x1, 0, y1, y2))  # 0 = open (left edge)
        events.append((x2, 1, y1, y2))  # 1 = close (right edge)

    # Sort events: by x, then open before close at same x
    events.sort()

    # Compress y-coordinates
    ys = sorted(ys)
    y_index = {y: i for i, y in enumerate(ys)}
    m = len(ys) - 1  # number of y-intervals

    if m <= 0:
        return 0

    # Coverage count for each y-interval
    count = [0] * m

    def active_y_length():
        """Compute total length of active y-intervals."""
        total = 0
        for i in range(m):
            if count[i] > 0:
                total += ys[i + 1] - ys[i]
        return total

    area = 0
    prev_x = events[0][0]

    for x, typ, y1, y2 in events:
        # Add area contribution from previous x to current x
        area += (x - prev_x) * active_y_length()
        prev_x = x

        # Update coverage
        i1 = y_index[y1]
        i2 = y_index[y2]
        delta = 1 if typ == 0 else -1
        for i in range(i1, i2):
            count[i] += delta

    return area


# ── Do not change anything below this line ──────────────────────
if __name__ == "__main__":
    import sys
    import json
    data = json.loads(sys.stdin.read())
    print(solve(data))
