# Computational Geometry & Sweep Line

{% hint style="info" %}
**This is the FINAL chapter of the entire workbook — the grand finale!** Computational geometry is the crown jewel of competitive programming. It combines mathematical precision with algorithmic cleverness. Cross products, convex hulls, sweep lines — these are the tools that separate Platinum-level contestants from the rest. By the end of this chapter, you will have completed your journey from "Hello World" to the summit of competitive programming.
{% endhint %}

## Chapter Goals

By the end of this chapter, you will:

- Understand 2D points, vectors, and how to represent them in code
- Master the cross product and use it to determine orientation (clockwise, counter-clockwise, collinear)
- Use cross products to test whether two line segments intersect
- Implement the convex hull using Andrew's Monotone Chain algorithm
- Understand the sweep line paradigm: processing events left-to-right
- Solve the closest pair of points problem in O(n log n) using divide and conquer
- Apply the Shoelace formula to compute polygon areas
- Determine whether a point lies inside a polygon using the ray casting algorithm
- Find the maximum number of collinear points
- Solve rectangle union area using coordinate compression and sweep line
- Recognize USACO Platinum geometry patterns and apply the right tools

---

## The Story: "The Drone Surveyor"

Maya had just started her summer internship at TerraScan, a company that used drones to map farmland and forests. Her supervisor handed her a laptop and a problem.

"These are GPS coordinates from our latest survey flight," she said, pointing at thousands of dots on the screen. "The client needs four things by Friday."

Maya looked at the list:

1. **Property boundaries** — stretch a fence around the outermost survey markers. The fence should use the least total length.
2. **Plot area** — calculate the exact area enclosed by boundary markers, without measuring it on the ground.
3. **Inside or outside** — for each new marker a field worker places, determine if it falls within the property or outside it.
4. **Closest landmarks** — find the two survey markers that are closest to each other (possible duplicate markers to merge).

Maya had never taken a geometry class in college. But she had taken an algorithms class. She opened her IDE and typed `def cross_product`. Everything she needed came down to one operation: the cross product of two vectors.

By Friday, she had all four answers. And TerraScan offered her a full-time job.

This chapter teaches you the same tools Maya used. Let's begin.

---

## Johari Window: Before

Before diving in, take 5 minutes to fill out the **"Before"** section of your [Johari Window worksheet](johari.md).

{% hint style="info" %}
Be honest with yourself! Knowing what you *don't* know is the first step to learning it. There are no wrong answers — only honest ones.
{% endhint %}

---

## Discovery

Before we dive into the theory, try these puzzles by hand.

### Puzzle 1: "Which Way Do We Turn?"

Three points are plotted: A = (0, 0), B = (4, 4), C = (1, 2).

If you walk from A to B and then turn to face C, do you turn LEFT (counter-clockwise) or RIGHT (clockwise)?

What if C = (1, 0) instead? What about C = (2, 2)?

{% hint style="info" %}
**Hint:** Draw it on paper. For C = (1, 2), you turn LEFT (counter-clockwise). For C = (1, 0), you turn RIGHT (clockwise). For C = (2, 2), all three points are on the same line — no turn needed (collinear). The cross product of vectors AB and AC tells you the answer: positive means left turn, negative means right turn, zero means collinear.
{% endhint %}

### Puzzle 2: "The Rubber Band"

You have 5 nails hammered into a board at positions: (0,0), (1,1), (2,0), (0,2), (2,2).

Stretch a rubber band around ALL the nails. What shape does it form? Which nails are on the boundary of the rubber band, and which are inside?

{% hint style="info" %}
**Hint:** The rubber band forms a square: (0,0), (2,0), (2,2), (0,2). The nail at (1,1) is INSIDE the rubber band. This shape is called the **convex hull** — the smallest convex polygon that contains all the points.
{% endhint %}

### Puzzle 3: "The Closest Pair"

You have 6 points: (0,0), (3,4), (1,1), (5,5), (10,0), (10,1).

Which two points are closest to each other? Can you figure it out without checking all 15 pairs?

{% hint style="info" %}
**Hint:** (10,0) and (10,1) are distance 1 apart. (0,0) and (1,1) are distance sqrt(2) apart. The closest pair is (10,0) and (10,1). The brute force checks all C(n,2) pairs, which is O(n^2). But there is a clever divide and conquer approach that does it in O(n log n) — you will learn it in Section 34.5.
{% endhint %}

---

## 34.1 Points, Vectors, and Cross Products

Everything in 2D computational geometry starts with three concepts: **points**, **vectors**, and the **cross product**.

### Points and Vectors

A **point** is a location: P = (x, y). A **vector** is a direction with magnitude: V = (dx, dy). The vector from point A to point B is:

```
AB = (B.x - A.x, B.y - A.y)
```

### The Cross Product (2D)

The cross product of two 2D vectors U = (u1, u2) and V = (v1, v2) is a scalar:

```
U x V = u1 * v2 - u2 * v1
```

This single formula is the most important tool in computational geometry. It tells you:

| Cross Product Value | Meaning |
|-------------------|---------|
| Positive | V is to the LEFT of U (counter-clockwise turn) |
| Negative | V is to the RIGHT of U (clockwise turn) |
| Zero | U and V are parallel (collinear) |

### Orientation of Three Points

Given three points A, B, C, the orientation is determined by the cross product of vectors AB and AC:

```
cross = (B.x - A.x) * (C.y - A.y) - (B.y - A.y) * (C.x - A.x)
```

{% tabs %}
{% tab title="Python" %}
```python
def cross(o, a, b):
    """Cross product of vectors OA and OB."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def orientation(a, b, c):
    """Return 1 (CCW), -1 (CW), or 0 (collinear)."""
    cp = cross(a, b, c)
    if cp > 0: return 1    # counter-clockwise
    if cp < 0: return -1   # clockwise
    return 0               # collinear
```
{% endtab %}
{% tab title="Java" %}
```java
static long cross(int[] o, int[] a, int[] b) {
    return (long)(a[0] - o[0]) * (b[1] - o[1])
         - (long)(a[1] - o[1]) * (b[0] - o[0]);
}

static int orientation(int[] a, int[] b, int[] c) {
    long cp = cross(a, b, c);
    if (cp > 0) return 1;   // counter-clockwise
    if (cp < 0) return -1;  // clockwise
    return 0;               // collinear
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
long long cross(vector<int>& o, vector<int>& a, vector<int>& b) {
    return (long long)(a[0] - o[0]) * (b[1] - o[1])
         - (long long)(a[1] - o[1]) * (b[0] - o[0]);
}

int orientation(vector<int>& a, vector<int>& b, vector<int>& c) {
    long long cp = cross(a, b, c);
    if (cp > 0) return 1;   // counter-clockwise
    if (cp < 0) return -1;  // clockwise
    return 0;               // collinear
}
```
{% endtab %}
{% endtabs %}

**Language Spotlight:**

| Feature | Python | Java | C++ |
|---------|--------|------|-----|
| Integer overflow risk | No (arbitrary precision) | Yes — use `long` | Yes — use `long long` |
| Point representation | tuple or list | int[] | vector<int> or pair |
| Cross product type | int (auto big) | long | long long |

{% hint style="warning" %}
**Integer overflow alert!** If coordinates can be up to 10^9, the cross product can be as large as 4 * 10^18, which overflows a 32-bit integer. In Java and C++, always use `long` / `long long` for cross products.
{% endhint %}

### The Dot Product

While cross product handles orientation, the **dot product** measures alignment:

```
U . V = u1 * v1 + u2 * v2
```

- Positive: vectors point roughly the same direction
- Zero: vectors are perpendicular
- Negative: vectors point roughly opposite directions

### Distance Between Points

```
distance(A, B) = sqrt((B.x - A.x)^2 + (B.y - A.y)^2)
```

{% hint style="info" %}
**Pro tip:** When comparing distances, compare the SQUARED distances to avoid floating point issues. You only need `sqrt` for the final answer.
{% endhint %}

---

## 34.2 Line Segment Intersection

Two line segments AB and CD intersect if and only if:
1. A and B are on **opposite sides** of line CD, AND
2. C and D are on **opposite sides** of line AB.

"Opposite sides" means the orientations have different signs.

### The General Position Test

```
d1 = orientation(C, D, A)
d2 = orientation(C, D, B)
d3 = orientation(A, B, C)
d4 = orientation(A, B, D)
```

Segments intersect if `d1 * d2 < 0` AND `d3 * d4 < 0`.

### Edge Cases: Collinear Points

When a cross product is zero, one point lies ON the other segment's line. We need an additional **on-segment** check:

{% tabs %}
{% tab title="Python" %}
```python
def on_segment(p, q, r):
    """Check if point q lies on segment pr (assuming collinear)."""
    return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
            min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

def segments_intersect(a, b, c, d):
    """Return True if segment AB intersects segment CD."""
    d1 = orientation(c, d, a)
    d2 = orientation(c, d, b)
    d3 = orientation(a, b, c)
    d4 = orientation(a, b, d)

    if d1 * d2 < 0 and d3 * d4 < 0:
        return True

    # Collinear special cases
    if d1 == 0 and on_segment(c, a, d): return True
    if d2 == 0 and on_segment(c, b, d): return True
    if d3 == 0 and on_segment(a, c, b): return True
    if d4 == 0 and on_segment(a, d, b): return True

    return False
```
{% endtab %}
{% tab title="Java" %}
```java
static boolean onSegment(int[] p, int[] q, int[] r) {
    return q[0] >= Math.min(p[0], r[0]) && q[0] <= Math.max(p[0], r[0])
        && q[1] >= Math.min(p[1], r[1]) && q[1] <= Math.max(p[1], r[1]);
}

static boolean segmentsIntersect(int[] a, int[] b, int[] c, int[] d) {
    int d1 = orientation(c, d, a), d2 = orientation(c, d, b);
    int d3 = orientation(a, b, c), d4 = orientation(a, b, d);
    if (d1 * d2 < 0 && d3 * d4 < 0) return true;
    if (d1 == 0 && onSegment(c, a, d)) return true;
    if (d2 == 0 && onSegment(c, b, d)) return true;
    if (d3 == 0 && onSegment(a, c, b)) return true;
    if (d4 == 0 && onSegment(a, d, b)) return true;
    return false;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
bool onSegment(vector<int>& p, vector<int>& q, vector<int>& r) {
    return q[0] >= min(p[0], r[0]) && q[0] <= max(p[0], r[0])
        && q[1] >= min(p[1], r[1]) && q[1] <= max(p[1], r[1]);
}

bool segmentsIntersect(vector<int> a, vector<int> b,
                       vector<int> c, vector<int> d) {
    int d1 = orientation(c, d, a), d2 = orientation(c, d, b);
    int d3 = orientation(a, b, c), d4 = orientation(a, b, d);
    if (d1 * d2 < 0 && d3 * d4 < 0) return true;
    if (d1 == 0 && onSegment(c, a, d)) return true;
    if (d2 == 0 && onSegment(c, b, d)) return true;
    if (d3 == 0 && onSegment(a, c, b)) return true;
    if (d4 == 0 && onSegment(a, d, b)) return true;
    return false;
}
```
{% endtab %}
{% endtabs %}

---

## 34.3 Convex Hull — The Rubber Band

The **convex hull** of a set of points is the smallest convex polygon that contains all the points. Think of it as stretching a rubber band around nails on a board.

### Andrew's Monotone Chain Algorithm

This is the most popular convex hull algorithm for competitive programming. It builds the hull in two passes: one for the **lower hull** (left to right) and one for the **upper hull** (right to left).

**Algorithm:**
1. Sort points by x-coordinate (break ties by y-coordinate)
2. Build the lower hull: scan left to right, keeping only left turns
3. Build the upper hull: scan right to left, keeping only left turns
4. Concatenate (removing duplicate endpoints)

{% tabs %}
{% tab title="Python" %}
```python
def convex_hull(points):
    """Return convex hull in CCW order starting from bottom-left.
    Excludes collinear points on the hull boundary."""
    points = sorted(set(map(tuple, points)))
    if len(points) <= 1:
        return [list(p) for p in points]

    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenate, removing last point of each half (duplicate)
    hull = lower[:-1] + upper[:-1]
    return [list(p) for p in hull]
```
{% endtab %}
{% tab title="Java" %}
```java
static int[][] convexHull(int[][] points) {
    int n = points.length;
    if (n <= 1) return points;
    Arrays.sort(points, (a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);

    // Remove duplicates
    int[][] unique = new int[n][];
    int u = 0;
    for (int[] p : points)
        if (u == 0 || p[0] != unique[u-1][0] || p[1] != unique[u-1][1])
            unique[u++] = p;
    if (u <= 1) return Arrays.copyOf(unique, u);

    int[][] hull = new int[2 * u][];
    int k = 0;

    // Lower hull
    for (int i = 0; i < u; i++) {
        while (k >= 2 && cross(hull[k-2], hull[k-1], unique[i]) <= 0) k--;
        hull[k++] = unique[i];
    }

    // Upper hull
    int lower = k + 1;
    for (int i = u - 2; i >= 0; i--) {
        while (k >= lower && cross(hull[k-2], hull[k-1], unique[i]) <= 0) k--;
        hull[k++] = unique[i];
    }

    return Arrays.copyOf(hull, k - 1);
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
vector<vector<int>> convexHull(vector<vector<int>> points) {
    sort(points.begin(), points.end());
    points.erase(unique(points.begin(), points.end()), points.end());
    int n = points.size();
    if (n <= 1) return points;

    vector<vector<int>> hull;

    // Lower hull
    for (auto& p : points) {
        while (hull.size() >= 2 &&
               cross(hull[hull.size()-2], hull[hull.size()-1], p) <= 0)
            hull.pop_back();
        hull.push_back(p);
    }

    // Upper hull
    int lower = hull.size() + 1;
    for (int i = n - 2; i >= 0; i--) {
        while ((int)hull.size() >= lower &&
               cross(hull[hull.size()-2], hull[hull.size()-1], points[i]) <= 0)
            hull.pop_back();
        hull.push_back(points[i]);
    }

    hull.pop_back(); // remove duplicate of first point
    return hull;
}
```
{% endtab %}
{% endtabs %}

**Time**: O(n log n) — dominated by the sort. The hull construction itself is O(n).

**Language Spotlight:**

| Feature | Python | Java | C++ |
|---------|--------|------|-----|
| Sorting points | `sorted()` with tuple comparison | `Arrays.sort` with comparator | `sort()` with default `<` on `vector` |
| Deduplication | `set(map(tuple, ...))` | Manual loop | `unique()` + `erase()` |
| Dynamic array | list with `pop()` | Array with index counter | vector with `pop_back()` |

---

## 34.4 Sweep Line Technique

The **sweep line** is a paradigm, not a single algorithm. Imagine a vertical line sweeping from left to right across the plane. As it moves, it processes **events** (points, segment endpoints, rectangle edges) in order.

### The Sweep Line Pattern

1. Collect all events and sort them by x-coordinate
2. Maintain an active data structure (sorted set, segment tree, etc.)
3. At each event, update the active structure
4. Extract the answer from the active structure

### Example: Maximum Rectangle in Histogram

One of the most elegant sweep line applications uses a **stack** instead of a tree. As we sweep through histogram bars left to right:

- If the current bar is taller than the stack top, push it
- If shorter, pop bars and compute their maximum rectangle area
- The stack maintains bars in increasing height order

{% tabs %}
{% tab title="Python" %}
```python
def largest_rectangle_histogram(heights):
    """Return area of largest rectangle in histogram."""
    stack = []   # stack of indices
    max_area = 0
    n = len(heights)

    for i in range(n + 1):
        h = heights[i] if i < n else 0
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area
```
{% endtab %}
{% tab title="Java" %}
```java
static int largestRectangleHistogram(int[] heights) {
    Deque<Integer> stack = new ArrayDeque<>();
    int maxArea = 0, n = heights.length;
    for (int i = 0; i <= n; i++) {
        int h = (i < n) ? heights[i] : 0;
        while (!stack.isEmpty() && heights[stack.peek()] > h) {
            int height = heights[stack.pop()];
            int width = stack.isEmpty() ? i : i - stack.peek() - 1;
            maxArea = Math.max(maxArea, height * width);
        }
        stack.push(i);
    }
    return maxArea;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
int largestRectangleHistogram(vector<int>& heights) {
    stack<int> st;
    int maxArea = 0, n = heights.size();
    for (int i = 0; i <= n; i++) {
        int h = (i < n) ? heights[i] : 0;
        while (!st.empty() && heights[st.top()] > h) {
            int height = heights[st.top()]; st.pop();
            int width = st.empty() ? i : i - st.top() - 1;
            maxArea = max(maxArea, height * width);
        }
        st.push(i);
    }
    return maxArea;
}
```
{% endtab %}
{% endtabs %}

### Sweep Line for Rectangle Union Area

A more advanced sweep line application: given multiple rectangles, find the total area of their union (overlapping regions counted only once).

**Algorithm:**
1. Create events for each rectangle's left and right edges
2. Sort events by x-coordinate
3. Sweep left to right; at each event, maintain the active y-intervals
4. Between consecutive x-events, the area contribution equals (x_delta) * (total active y-length)
5. Use coordinate compression on y-values and count coverage for each y-interval

---

## 34.5 Closest Pair of Points

Given n points, find the two points with the minimum Euclidean distance between them.

### Five-Lens Framework

{% hint style="info" %}
**Constraints Lens:** n can be up to 10^5 points with coordinates up to 10^9.

**Brute Force Lens:** Check all C(n,2) pairs. Time: O(n^2). This works for n up to about 10^4.

**Pattern Lens:** If we sort points by x and split them in half, the closest pair is either entirely in the left half, entirely in the right half, or split across the boundary. The split case only needs to check points within distance delta of the dividing line.

**Optimization Lens:** Divide and conquer gives O(n log n). In the "strip" of width 2*delta, each point only needs to be compared with at most 6 other points (those in a delta-by-2*delta box). This keeps the merge step at O(n).

**Proof Lens:** Why only 6 points? In a delta x 2*delta rectangle, you can pack at most 8 points that are all at least delta apart (place them in a 2x4 grid of delta/2 cells). Since we already know the pair within each half is at least delta apart, the bound holds.
{% endhint %}

{% tabs %}
{% tab title="Python" %}
```python
import math

def closest_pair(points):
    """Return the minimum distance between any pair of points."""
    pts = sorted(points)

    def dist(a, b):
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

    def solve(pts):
        n = len(pts)
        if n <= 3:
            best = float('inf')
            for i in range(n):
                for j in range(i+1, n):
                    best = min(best, dist(pts[i], pts[j]))
            return best

        mid = n // 2
        mid_x = pts[mid][0]
        d = min(solve(pts[:mid]), solve(pts[mid:]))

        # Build strip
        strip = [p for p in pts if abs(p[0] - mid_x) < d]
        strip.sort(key=lambda p: p[1])

        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and strip[j][1] - strip[i][1] < d:
                d = min(d, dist(strip[i], strip[j]))
                j += 1

        return d

    return solve(pts)
```
{% endtab %}
{% tab title="Java" %}
```java
static double closestPair(int[][] points) {
    int[][] pts = points.clone();
    Arrays.sort(pts, (a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);
    return solve(pts, 0, pts.length - 1);
}

static double dist(int[] a, int[] b) {
    return Math.sqrt((double)(a[0]-b[0])*(a[0]-b[0])
                   + (double)(a[1]-b[1])*(a[1]-b[1]));
}

static double solve(int[][] pts, int lo, int hi) {
    if (hi - lo < 3) {
        double best = Double.MAX_VALUE;
        for (int i = lo; i <= hi; i++)
            for (int j = i+1; j <= hi; j++)
                best = Math.min(best, dist(pts[i], pts[j]));
        return best;
    }
    int mid = (lo + hi) / 2;
    int midX = pts[mid][0];
    double d = Math.min(solve(pts, lo, mid), solve(pts, mid+1, hi));
    List<int[]> strip = new ArrayList<>();
    for (int i = lo; i <= hi; i++)
        if (Math.abs(pts[i][0] - midX) < d) strip.add(pts[i]);
    strip.sort((a, b) -> a[1] - b[1]);
    for (int i = 0; i < strip.size(); i++)
        for (int j = i+1; j < strip.size()
             && strip.get(j)[1] - strip.get(i)[1] < d; j++)
            d = Math.min(d, dist(strip.get(i), strip.get(j)));
    return d;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
double dist(vector<int>& a, vector<int>& b) {
    return sqrt((double)(a[0]-b[0])*(a[0]-b[0])
              + (double)(a[1]-b[1])*(a[1]-b[1]));
}

double solve(vector<vector<int>>& pts, int lo, int hi) {
    if (hi - lo < 3) {
        double best = 1e18;
        for (int i = lo; i <= hi; i++)
            for (int j = i+1; j <= hi; j++)
                best = min(best, dist(pts[i], pts[j]));
        return best;
    }
    int mid = (lo + hi) / 2;
    int midX = pts[mid][0];
    double d = min(solve(pts, lo, mid), solve(pts, mid+1, hi));
    vector<vector<int>> strip;
    for (int i = lo; i <= hi; i++)
        if (abs(pts[i][0] - midX) < d) strip.push_back(pts[i]);
    sort(strip.begin(), strip.end(),
         [](auto& a, auto& b) { return a[1] < b[1]; });
    for (int i = 0; i < (int)strip.size(); i++)
        for (int j = i+1; j < (int)strip.size()
             && strip[j][1] - strip[i][1] < d; j++)
            d = min(d, dist(strip[i], strip[j]));
    return d;
}

double closestPair(vector<vector<int>>& points) {
    sort(points.begin(), points.end());
    return solve(points, 0, points.size() - 1);
}
```
{% endtab %}
{% endtabs %}

**Time**: O(n log^2 n) for this version (due to sorting strip at each level). Can be optimized to O(n log n) by pre-sorting by y and merging.

---

## 34.6 Area Calculations

### The Shoelace Formula

The area of a simple polygon with vertices (x1,y1), (x2,y2), ..., (xn,yn) listed in order is:

```
Area = |sum of (x_i * y_{i+1} - x_{i+1} * y_i) for i = 1..n| / 2
```

where indices wrap around (vertex n+1 = vertex 1).

This is called the "Shoelace formula" because if you write the coordinates in two columns and cross-multiply diagonally, the pattern looks like lacing a shoe.

{% tabs %}
{% tab title="Python" %}
```python
def polygon_area(polygon):
    """Return the area of a simple polygon. Vertices in order."""
    n = len(polygon)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    return abs(area) / 2.0
```
{% endtab %}
{% tab title="Java" %}
```java
static double polygonArea(int[][] polygon) {
    int n = polygon.length;
    long area = 0;
    for (int i = 0; i < n; i++) {
        int j = (i + 1) % n;
        area += (long) polygon[i][0] * polygon[j][1];
        area -= (long) polygon[j][0] * polygon[i][1];
    }
    return Math.abs(area) / 2.0;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
double polygonArea(vector<vector<int>>& polygon) {
    int n = polygon.size();
    long long area = 0;
    for (int i = 0; i < n; i++) {
        int j = (i + 1) % n;
        area += (long long)polygon[i][0] * polygon[j][1];
        area -= (long long)polygon[j][0] * polygon[i][1];
    }
    return abs(area) / 2.0;
}
```
{% endtab %}
{% endtabs %}

### Point in Polygon (Ray Casting)

To check whether a point Q is inside a polygon, cast a ray from Q in any direction (typically rightward) and count how many times it crosses the polygon boundary. If the count is **odd**, the point is inside; if **even**, it is outside.

{% tabs %}
{% tab title="Python" %}
```python
def point_in_polygon(polygon, point):
    """Return True if point is inside or on the boundary of polygon."""
    x, y = point
    n = len(polygon)

    # Check if point is on any edge
    for i in range(n):
        j = (i + 1) % n
        ax, ay = polygon[i]
        bx, by = polygon[j]
        # Check collinear and within bounding box
        cp = (bx - ax) * (y - ay) - (by - ay) * (x - ax)
        if cp == 0:
            if (min(ax, bx) <= x <= max(ax, bx) and
                min(ay, by) <= y <= max(ay, by)):
                return True

    # Ray casting
    inside = False
    j = n - 1
    for i in range(n):
        yi, yj = polygon[i][1], polygon[j][1]
        xi, xj = polygon[i][0], polygon[j][0]
        if ((yi > y) != (yj > y)):
            x_intersect = (xj - xi) * (y - yi) / (yj - yi) + xi
            if x < x_intersect:
                inside = not inside
        j = i

    return inside
```
{% endtab %}
{% tab title="Java" %}
```java
static boolean pointInPolygon(int[][] polygon, int[] point) {
    int x = point[0], y = point[1];
    int n = polygon.length;

    // Check if on boundary
    for (int i = 0; i < n; i++) {
        int j = (i + 1) % n;
        long cp = (long)(polygon[j][0] - polygon[i][0]) * (y - polygon[i][1])
                - (long)(polygon[j][1] - polygon[i][1]) * (x - polygon[i][0]);
        if (cp == 0
            && x >= Math.min(polygon[i][0], polygon[j][0])
            && x <= Math.max(polygon[i][0], polygon[j][0])
            && y >= Math.min(polygon[i][1], polygon[j][1])
            && y <= Math.max(polygon[i][1], polygon[j][1]))
            return true;
    }

    // Ray casting
    boolean inside = false;
    for (int i = 0, j = n - 1; i < n; j = i++) {
        int yi = polygon[i][1], yj = polygon[j][1];
        int xi = polygon[i][0], xj = polygon[j][0];
        if ((yi > y) != (yj > y)) {
            double xIntersect = (double)(xj - xi) * (y - yi) / (yj - yi) + xi;
            if (x < xIntersect) inside = !inside;
        }
    }
    return inside;
}
```
{% endtab %}
{% tab title="C++" %}
```cpp
bool pointInPolygon(vector<vector<int>>& polygon, vector<int>& point) {
    int x = point[0], y = point[1];
    int n = polygon.size();

    // Check if on boundary
    for (int i = 0; i < n; i++) {
        int j = (i + 1) % n;
        long long cp = (long long)(polygon[j][0] - polygon[i][0]) * (y - polygon[i][1])
                     - (long long)(polygon[j][1] - polygon[i][1]) * (x - polygon[i][0]);
        if (cp == 0
            && x >= min(polygon[i][0], polygon[j][0])
            && x <= max(polygon[i][0], polygon[j][0])
            && y >= min(polygon[i][1], polygon[j][1])
            && y <= max(polygon[i][1], polygon[j][1]))
            return true;
    }

    // Ray casting
    bool inside = false;
    for (int i = 0, j = n - 1; i < n; j = i++) {
        int yi = polygon[i][1], yj = polygon[j][1];
        int xi = polygon[i][0], xj = polygon[j][0];
        if ((yi > y) != (yj > y)) {
            double xIntersect = (double)(xj - xi) * (y - yi) / (yj - yi) + xi;
            if (x < xIntersect) inside = !inside;
        }
    }
    return inside;
}
```
{% endtab %}
{% endtabs %}

---

## Think Like a Pro

{% hint style="info" %}
**Tourist (Gennady Korotkevich):** "Geometry problems scare many programmers, but they follow predictable patterns. Cross product is the fundamental tool — it tells you orientation, area, and intersection all at once. Master the cross product, and geometry problems become manageable. Build a tested geometry library, and reuse it in every contest."
{% endhint %}

---

## AOPS Showcase: Closest Pair of Points

Let's see the same problem solved three different ways.

### Solution 1: Brute Force — O(n^2)

```python
def closest_pair_brute(points):
    n = len(points)
    best = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            d = math.sqrt((points[i][0]-points[j][0])**2
                        + (points[i][1]-points[j][1])**2)
            best = min(best, d)
    return best
```

Simple, correct, but too slow for n > 10^4.

### Solution 2: Divide and Conquer — O(n log^2 n)

This is the algorithm from Section 34.5. Sort by x, split in half, recurse on both halves, then check the strip of points near the dividing line. The key insight: you only need to check at most 6-7 nearby points in the strip for each point.

### Solution 3: Randomized Grid Hashing — Expected O(n)

**Concept (not full implementation):** Insert points one by one in random order. Maintain a grid with cell size d (current closest distance). When inserting a point, check only the 9 neighboring cells. If a closer pair is found, rebuild the grid with the new cell size. On average, this runs in O(n) expected time.

This approach is used in practice when the expected input is well-distributed, but the divide-and-conquer approach is the standard choice for competitive programming because it has a guaranteed worst-case bound.

---

## Legend's Corner

{% hint style="info" %}
**Petr Mitrichev:** "I used to dread geometry problems in contests. Then I realized: 90% of competitive programming geometry comes down to three operations — cross product, dot product, and distance. Build reliable templates for these three, test them on tricky edge cases (collinear points, overlapping segments, degenerate polygons), and most geometry problems become about combining these building blocks. The other 10% is just careful case analysis."
{% endhint %}

---

## Gotchas

{% hint style="danger" %}
**Common mistakes to avoid:**

1. **Floating point precision**: Use integer arithmetic (cross products, squared distances) whenever possible. Only take `sqrt` at the very end for the final answer. Never compare floating point numbers with `==` — use `abs(a - b) < epsilon`.

2. **Collinear points in convex hull**: Decide in advance whether to INCLUDE or EXCLUDE collinear points on the hull boundary. Use `<= 0` to exclude them (strict left turns only), `< 0` to include them. Most problems expect exclusion.

3. **Cross product sign convention**: Positive cross product means counter-clockwise, negative means clockwise. But this is only true in the standard mathematical coordinate system (y-axis pointing UP). If your y-axis points down (as in screen coordinates), the convention is reversed.

4. **Integer overflow in cross products**: If coordinates are up to 10^9, the cross product can reach 4 * 10^18. This fits in a 64-bit integer (`long` in Java, `long long` in C++) but NOT in a 32-bit `int`. Python handles this automatically.

5. **Degenerate cases**: Always handle: all points collinear (hull is a line), only 1-2 points, duplicate points, polygon with zero area. These cases often cause crashes or wrong answers.

6. **Convex hull sorting**: Andrew's Monotone Chain requires points sorted by (x, y). Forgetting the sort or sorting incorrectly will produce a wrong hull.

7. **Point on boundary vs. interior**: Some problems treat boundary points as "inside", others do not. Read the problem statement carefully. Our `point_in_polygon` checks both.

8. **Sweep line event ordering**: When two events have the same x-coordinate, the tie-breaking order matters. For rectangle union area, process "start" events before "end" events at the same x. Getting this wrong leads to subtle bugs.
{% endhint %}

---

## Practice Problems

| # | Problem | Difficulty | Key Technique |
|---|---------|-----------|---------------|
| W1 | Cross Product & Orientation | Warmup | Cross product, orientation test |
| W2 | Convex Hull | Warmup | Andrew's Monotone Chain |
| W3 | Polygon Area (Shoelace) | Warmup | Shoelace formula |
| P1 | Closest Pair of Points | Practice | Divide and conquer |
| P2 | Line Segment Intersection | Practice | Cross product orientation test |
| P3 | Point in Polygon | Practice | Ray casting algorithm |
| P4 | Maximum Points on a Line | Practice | GCD-based slope counting |
| C1 | Convex Hull Perimeter | Challenge | Convex hull + perimeter calculation |
| C2 | Max Rectangle in Histogram | Challenge | Stack-based sweep |
| C3 | Rectangle Union Area | Challenge | Sweep line + coordinate compression |

---

## Language Idioms

{% tabs %}
{% tab title="Python" %}
```python
# Points as tuples for hashability and sorting
points = [(0, 0), (1, 1), (2, 0)]

# Cross product — the geometry Swiss Army knife
def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

# Distance — use squared distance for comparisons, sqrt only for final answer
import math
dist_sq = (a[0]-b[0])**2 + (a[1]-b[1])**2
dist = math.sqrt(dist_sq)

# Sorting by angle (for Graham scan):
import math
points.sort(key=lambda p: math.atan2(p[1] - pivot[1], p[0] - pivot[0]))
# Better: sort by cross product to avoid floating point
```
{% endtab %}
{% tab title="Java" %}
```java
// Points as int[] — lightweight for CP
int[] p = {x, y};

// Cross product with long to prevent overflow
long cross = (long)(a[0]-o[0]) * (b[1]-o[1])
           - (long)(a[1]-o[1]) * (b[0]-o[0]);

// Sorting points: comparator on int[]
Arrays.sort(points, (a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);

// Deque as stack for sweep line problems
Deque<Integer> stack = new ArrayDeque<>();
stack.push(i);   // push
stack.peek();    // top
stack.pop();     // pop
```
{% endtab %}
{% tab title="C++" %}
```cpp
// Points as vector<int> or pair<int,int>
// pair sorts lexicographically by default — convenient!
using pt = pair<int,int>;

// Cross product with long long
long long cross(pt o, pt a, pt b) {
    return (long long)(a.first-o.first) * (b.second-o.second)
         - (long long)(a.second-o.second) * (b.first-o.first);
}

// Sorting pairs — default < works for (x, y) ordering
sort(points.begin(), points.end());

// Stack for sweep line
stack<int> st;
st.push(i); st.top(); st.pop();
```
{% endtab %}
{% endtabs %}

---

## Breadcrumbs

### Looking Back
- **Ch 8** (Art of Sorting) taught you sorting — convex hull and sweep line both rely on sorting as a preprocessing step
- **Ch 16** (Binary Search Beyond) introduced binary search — useful for finding boundaries in sweep line problems
- **Ch 22** (Stacks & Queues) gave you the stack — the histogram problem uses a monotone stack, a technique you first met there
- **Ch 30** (Segment Trees) provided range query structures — sweep line for rectangle union area can use a segment tree for efficient y-interval tracking

### Looking Forward
- **Contest preparation**: Geometry appears in USACO Platinum problems. Build a geometry template library (cross product, convex hull, segment intersection) and reuse it.
- **USACO Platinum**: Problems like "Fencing the Cows" (convex hull), "Cow Rectangles" (sweep line), and many more use techniques from this chapter.

### Cross-Chapter Threads
- **"Sort first"**: Both convex hull (sort by x,y) and sweep line (sort events by x) are prime examples of the "sort first" pattern from Ch 8.
- **"Reduce to known"**: Many geometry problems reduce to cross product queries. "Is this point inside the polygon?" reduces to ray casting. "What is the boundary?" reduces to convex hull.
- **"Space-for-time"**: The grid hashing approach to closest pair trades O(n) space for O(n) expected time, versus the O(n log n) divide and conquer.

---

## Johari Window: After

Now fill out the **"After"** section of your [Johari Window worksheet](johari.md). Compare your "Before" and "After" answers — what surprised you? What do you still want to explore?

---

## Open Questions Beyond

1. **"What about 3D geometry?"** Everything we covered extends to 3D: cross products become 3D vectors, convex hulls become convex polyhedra, and the algorithms become significantly more complex. 3D convex hull algorithms like QuickHull run in O(n log n) expected time but are much harder to implement correctly.

2. **"What is a Voronoi diagram?"** Given n points, a Voronoi diagram partitions the plane into regions where each region contains all points closest to a particular input point. It is the "dual" of the Delaunay triangulation and has applications in nearest neighbor queries, facility placement, and computational biology.

3. **"Can we do better than O(n log n) for convex hull?"** For comparison-based algorithms, O(n log n) is a lower bound (like sorting). But if coordinates are integers in a bounded range, you can use integer sorting to achieve O(n) for the sort step. The hull construction itself is always O(n), so the bottleneck is sorting.

---

## What's Next

{% hint style="info" %}
**CONGRATULATIONS! YOU HAVE COMPLETED THE ENTIRE DSA WORKBOOK!**

Take a deep breath. Look back at where you started and where you are now.

**Part 0 — The Adventure Begins**: You set up your development environment and learned your coder's toolkit.

**Part I — Learning to Speak Code**: You wrote your first programs, learned loops, functions, collections, and how to analyze algorithm speed.

**Part II — The Bronze Forge**: You mastered number theory, sorting, searching, recursion, hashing, and bit manipulation. You became ready for USACO Bronze.

**Part III — The Silver Arena**: You conquered prefix sums, two pointers, binary search, heaps, greedy algorithms, graphs, linked lists, and stacks/queues. USACO Silver was within your reach.

**Part IV — The Gold Crucible**: You tackled dynamic programming (three chapters!), trees, shortest paths, topological sort, and Union-Find with MST. USACO Gold became achievable.

**Part V — The Platinum Summit**: You climbed the final peak — segment trees, advanced DP, string algorithms, advanced graph and tree algorithms, and now computational geometry with sweep line. You are ready for USACO Platinum.

**35 chapters. Hundreds of problems. Three languages. One incredible journey.**

You started as someone who knew basic Python and Java. Now you can write C++ templates for computational geometry, implement segment trees with lazy propagation, solve DP problems on bitmasks and trees, and build graph algorithms from scratch.

You are not the same programmer you were when you opened Chapter 0. You are a competitive programmer.

**Where to Go From Here:**

- **USACO**: Start submitting to [usaco.org](http://usaco.org). Begin with Bronze contests you have not tried, work through Silver and Gold, and attempt Platinum. The problems will feel familiar — you have seen the patterns.
- **Codeforces**: Create an account at [codeforces.com](http://codeforces.com). Participate in Div 2 and Div 1 contests. Rate yourself. Compete against the world.
- **AtCoder**: Try [atcoder.jp](http://atcoder.jp) for beautifully clean problems, especially the ABC (Beginner) and ARC (Regular) contests.
- **IOI Preparation**: If you aim for the International Olympiad in Informatics, study the IOI syllabus and past problems. You have the foundation — now deepen it.
- **Build your template library**: Take the code from this workbook and organize it into a personal template library. In contests, speed matters, and having pre-tested templates for Union-Find, segment trees, geometry, and string algorithms gives you an edge.

**One last thing:** The best competitive programmers are not the ones who memorize algorithms. They are the ones who understand WHY algorithms work and can adapt them to new situations. You have spent 35 chapters building that understanding. Trust it.

Now go compete. The summit is not the end — it is the beginning of a whole new landscape.

Good luck, and happy coding.
{% endhint %}
