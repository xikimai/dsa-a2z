/*
 * Tests for Chapter 34: Computational Geometry & Sweep Line
 * Build: g++ -std=c++17 -o /tmp/test_ch34 code/cpp/ch34/tests/test_ch34.cpp && /tmp/test_ch34
 */

#include <algorithm>
#include <cassert>
#include <cmath>
#include <climits>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <stack>
#include <string>
#include <tuple>
#include <vector>
using namespace std;

// =====================================================================
// Reference solutions (uniquely named with ref_ prefix)
// =====================================================================

// W1: Cross Product and Orientation
vector<int> ref_orientation(vector<vector<vector<int>>> queries) {
    vector<int> result;
    for (auto& q : queries) {
        auto& a = q[0]; auto& b = q[1]; auto& c = q[2];
        long long cp = (long long)(b[0] - a[0]) * (c[1] - a[1])
                     - (long long)(b[1] - a[1]) * (c[0] - a[0]);
        if (cp > 0) result.push_back(1);
        else if (cp < 0) result.push_back(-1);
        else result.push_back(0);
    }
    return result;
}

// W2: Convex Hull
long long ref_cross_w2(vector<int>& o, vector<int>& a, vector<int>& b) {
    return (long long)(a[0] - o[0]) * (b[1] - o[1])
         - (long long)(a[1] - o[1]) * (b[0] - o[0]);
}

vector<vector<int>> ref_convex_hull(vector<vector<int>> points) {
    sort(points.begin(), points.end());
    points.erase(unique(points.begin(), points.end()), points.end());
    int n = points.size();
    if (n <= 1) return points;

    vector<vector<int>> hull;
    for (auto& p : points) {
        while (hull.size() >= 2 && ref_cross_w2(hull[hull.size()-2], hull[hull.size()-1], p) <= 0)
            hull.pop_back();
        hull.push_back(p);
    }
    int lower = hull.size() + 1;
    for (int i = n - 2; i >= 0; i--) {
        while ((int)hull.size() >= lower && ref_cross_w2(hull[hull.size()-2], hull[hull.size()-1], points[i]) <= 0)
            hull.pop_back();
        hull.push_back(points[i]);
    }
    hull.pop_back();
    return hull;
}

// W3: Polygon Area
double ref_polygon_area(vector<vector<int>> polygon) {
    int n = polygon.size();
    long long area = 0;
    for (int i = 0; i < n; i++) {
        int j = (i + 1) % n;
        area += (long long)polygon[i][0] * polygon[j][1];
        area -= (long long)polygon[j][0] * polygon[i][1];
    }
    return abs(area) / 2.0;
}

// P1: Closest Pair
double ref_dist_p1(vector<int>& a, vector<int>& b) {
    return sqrt((double)(a[0]-b[0])*(a[0]-b[0]) + (double)(a[1]-b[1])*(a[1]-b[1]));
}

double ref_rec_p1(vector<vector<int>>& pts, int lo, int hi) {
    if (hi - lo < 3) {
        double best = 1e18;
        for (int i = lo; i <= hi; i++)
            for (int j = i + 1; j <= hi; j++)
                best = min(best, ref_dist_p1(pts[i], pts[j]));
        return best;
    }
    int mid = (lo + hi) / 2;
    int midX = pts[mid][0];
    double d = min(ref_rec_p1(pts, lo, mid), ref_rec_p1(pts, mid + 1, hi));
    vector<vector<int>> strip;
    for (int i = lo; i <= hi; i++)
        if (abs(pts[i][0] - midX) < d) strip.push_back(pts[i]);
    sort(strip.begin(), strip.end(), [](auto& a, auto& b) { return a[1] < b[1]; });
    for (int i = 0; i < (int)strip.size(); i++)
        for (int j = i + 1; j < (int)strip.size() && strip[j][1] - strip[i][1] < d; j++)
            d = min(d, ref_dist_p1(strip[i], strip[j]));
    return d;
}

double ref_closest_pair(vector<vector<int>> points) {
    sort(points.begin(), points.end());
    return ref_rec_p1(points, 0, points.size() - 1);
}

// P2: Segment Intersection
long long ref_cross_p2(vector<int>& o, vector<int>& a, vector<int>& b) {
    return (long long)(a[0] - o[0]) * (b[1] - o[1])
         - (long long)(a[1] - o[1]) * (b[0] - o[0]);
}

int ref_orient_p2(vector<int>& a, vector<int>& b, vector<int>& c) {
    long long cp = ref_cross_p2(a, b, c);
    if (cp > 0) return 1;
    if (cp < 0) return -1;
    return 0;
}

bool ref_onSeg_p2(vector<int>& p, vector<int>& q, vector<int>& r) {
    return q[0] >= min(p[0], r[0]) && q[0] <= max(p[0], r[0])
        && q[1] >= min(p[1], r[1]) && q[1] <= max(p[1], r[1]);
}

bool ref_intersects_p2(vector<int> a, vector<int> b, vector<int> c, vector<int> d) {
    int d1 = ref_orient_p2(c, d, a), d2 = ref_orient_p2(c, d, b);
    int d3 = ref_orient_p2(a, b, c), d4 = ref_orient_p2(a, b, d);
    if (d1 * d2 < 0 && d3 * d4 < 0) return true;
    if (d1 == 0 && ref_onSeg_p2(c, a, d)) return true;
    if (d2 == 0 && ref_onSeg_p2(c, b, d)) return true;
    if (d3 == 0 && ref_onSeg_p2(a, c, b)) return true;
    if (d4 == 0 && ref_onSeg_p2(a, d, b)) return true;
    return false;
}

vector<bool> ref_segment_intersect(vector<vector<vector<int>>> segments) {
    vector<bool> result;
    for (auto& seg : segments)
        result.push_back(ref_intersects_p2(seg[0], seg[1], seg[2], seg[3]));
    return result;
}

// P3: Point in Polygon
bool ref_pointInPoly(vector<vector<int>>& poly, int px, int py) {
    int n = poly.size();
    for (int i = 0; i < n; i++) {
        int j = (i + 1) % n;
        long long cp = (long long)(poly[j][0] - poly[i][0]) * (py - poly[i][1])
                     - (long long)(poly[j][1] - poly[i][1]) * (px - poly[i][0]);
        if (cp == 0
            && px >= min(poly[i][0], poly[j][0]) && px <= max(poly[i][0], poly[j][0])
            && py >= min(poly[i][1], poly[j][1]) && py <= max(poly[i][1], poly[j][1]))
            return true;
    }
    bool inside = false;
    for (int i = 0, j = n - 1; i < n; j = i++) {
        int yi = poly[i][1], yj = poly[j][1];
        int xi = poly[i][0], xj = poly[j][0];
        if ((yi > py) != (yj > py)) {
            double xIntersect = (double)(xj - xi) * (py - yi) / (yj - yi) + xi;
            if (px < xIntersect) inside = !inside;
        }
    }
    return inside;
}

vector<bool> ref_point_in_polygon(vector<vector<int>> polygon, vector<vector<int>> queries) {
    vector<bool> result;
    for (auto& q : queries) result.push_back(ref_pointInPoly(polygon, q[0], q[1]));
    return result;
}

// P4: Maximum Points on a Line
int ref_max_points(vector<vector<int>> points) {
    int n = points.size();
    if (n <= 2) return n;
    int best = 1;
    for (int i = 0; i < n; i++) {
        map<pair<int,int>, int> slopes;
        int dup = 1;
        for (int j = i + 1; j < n; j++) {
            int dx = points[j][0] - points[i][0];
            int dy = points[j][1] - points[i][1];
            if (dx == 0 && dy == 0) { dup++; continue; }
            int g = gcd(abs(dx), abs(dy));
            dx /= g; dy /= g;
            if (dx < 0 || (dx == 0 && dy < 0)) { dx = -dx; dy = -dy; }
            slopes[{dx, dy}]++;
        }
        int localMax = dup;
        for (auto& [k, cnt] : slopes) localMax = max(localMax, cnt + dup);
        best = max(best, localMax);
    }
    return best;
}

// C1: Convex Hull Perimeter
double ref_hull_perimeter(vector<vector<int>> points) {
    sort(points.begin(), points.end());
    points.erase(unique(points.begin(), points.end()), points.end());
    int n = points.size();
    if (n <= 1) return 0.0;
    if (n == 2) {
        return 2.0 * sqrt((double)(points[0][0]-points[1][0])*(points[0][0]-points[1][0])
                         + (double)(points[0][1]-points[1][1])*(points[0][1]-points[1][1]));
    }
    vector<vector<int>> hull;
    for (auto& p : points) {
        while (hull.size() >= 2 && ref_cross_w2(hull[hull.size()-2], hull[hull.size()-1], p) <= 0)
            hull.pop_back();
        hull.push_back(p);
    }
    int lower = hull.size() + 1;
    for (int i = n - 2; i >= 0; i--) {
        while ((int)hull.size() >= lower && ref_cross_w2(hull[hull.size()-2], hull[hull.size()-1], points[i]) <= 0)
            hull.pop_back();
        hull.push_back(points[i]);
    }
    hull.pop_back();
    int k = hull.size();
    double perimeter = 0.0;
    for (int i = 0; i < k; i++) {
        int j = (i + 1) % k;
        double dx = hull[i][0] - hull[j][0], dy = hull[i][1] - hull[j][1];
        perimeter += sqrt(dx * dx + dy * dy);
    }
    return perimeter;
}

// C2: Maximum Rectangle in Histogram
int ref_max_rect_histogram(vector<int> heights) {
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

// C3: Rectangle Union Area
int ref_rect_union_area(vector<vector<int>> rectangles) {
    if (rectangles.empty()) return 0;
    set<int> ySet;
    vector<tuple<int,int,int,int>> events;
    for (auto& r : rectangles) {
        ySet.insert(r[1]); ySet.insert(r[3]);
        events.push_back({r[0], 0, r[1], r[3]});
        events.push_back({r[2], 1, r[1], r[3]});
    }
    sort(events.begin(), events.end());
    vector<int> ys(ySet.begin(), ySet.end());
    map<int, int> yIndex;
    for (int i = 0; i < (int)ys.size(); i++) yIndex[ys[i]] = i;
    int m = ys.size() - 1;
    if (m <= 0) return 0;
    vector<int> count(m, 0);
    long long area = 0;
    int prevX = get<0>(events[0]);
    for (auto& [x, typ, y1, y2] : events) {
        long long activeY = 0;
        for (int i = 0; i < m; i++)
            if (count[i] > 0) activeY += ys[i + 1] - ys[i];
        area += (long long)(x - prevX) * activeY;
        prevX = x;
        int i1 = yIndex[y1], i2 = yIndex[y2];
        int delta = (typ == 0) ? 1 : -1;
        for (int i = i1; i < i2; i++) count[i] += delta;
    }
    return (int)area;
}

// =====================================================================
// Test runner
// =====================================================================

int passed = 0, failed_count = 0;

void check(int expected, int actual, const string& msg) {
    if (expected == actual) { passed++; }
    else { failed_count++; cout << "FAIL: " << msg << " — expected " << expected << ", got " << actual << endl; }
}

void check_double(double expected, double actual, const string& msg) {
    if (abs(expected - actual) < 1e-6) { passed++; }
    else { failed_count++; cout << "FAIL: " << msg << " — expected " << expected << ", got " << actual << endl; }
}

void check_vec(vector<int> expected, vector<int> actual, const string& msg) {
    if (expected == actual) { passed++; }
    else {
        failed_count++;
        cout << "FAIL: " << msg << " — expected [";
        for (int i = 0; i < (int)expected.size(); i++) cout << (i?",":"") << expected[i];
        cout << "], got [";
        for (int i = 0; i < (int)actual.size(); i++) cout << (i?",":"") << actual[i];
        cout << "]" << endl;
    }
}

void check_bool_vec(vector<bool> expected, vector<bool> actual, const string& msg) {
    if (expected == actual) { passed++; }
    else {
        failed_count++;
        cout << "FAIL: " << msg << " — mismatch" << endl;
    }
}

void check_2d(vector<vector<int>> expected, vector<vector<int>> actual, const string& msg) {
    if (expected == actual) { passed++; }
    else {
        failed_count++;
        cout << "FAIL: " << msg << " — mismatch" << endl;
    }
}

int main() {
    cout << "Chapter 34: Computational Geometry & Sweep Line" << endl;
    cout << "================================================================" << endl << endl;

    // W1: Orientation
    check_vec({1,-1,0}, ref_orientation({{{0,0},{4,4},{1,2}},{{0,0},{4,4},{1,0}},{{0,0},{4,4},{2,2}}}), "W1: mixed");
    check_vec({1}, ref_orientation({{{0,0},{1,0},{0,1}}}), "W1: ccw");
    check_vec({0,0}, ref_orientation({{{0,0},{1,1},{2,2}},{{0,0},{5,5},{10,10}}}), "W1: collinear");
    check_vec({-1}, ref_orientation({{{0,0},{0,1},{1,0}}}), "W1: cw");

    // W2: Convex Hull
    check_2d({{0,0},{2,0},{2,2},{0,2}}, ref_convex_hull({{0,0},{2,0},{0,2},{2,2},{1,1}}), "W2: square");
    check_2d({{0,0},{2,0}}, ref_convex_hull({{0,0},{1,0},{2,0}}), "W2: collinear");
    check_2d({{0,0},{4,0},{2,3}}, ref_convex_hull({{0,0},{4,0},{2,3}}), "W2: triangle");

    // W3: Polygon Area
    check_double(12.0, ref_polygon_area({{0,0},{4,0},{4,3},{0,3}}), "W3: rectangle");
    check_double(0.5, ref_polygon_area({{0,0},{1,0},{0,1}}), "W3: triangle");
    check_double(4.0, ref_polygon_area({{0,0},{2,0},{2,2},{0,2}}), "W3: square");
    check_double(12.0, ref_polygon_area({{0,3},{4,3},{4,0},{0,0}}), "W3: reverse");

    // P1: Closest Pair
    check_double(sqrt(2), ref_closest_pair({{0,0},{3,4},{1,1},{5,5}}), "P1: basic");
    check_double(1.0, ref_closest_pair({{0,0},{1,0},{0,1}}), "P1: unit");
    check_double(sqrt(200), ref_closest_pair({{0,0},{10,10}}), "P1: two");
    check_double(2.0, ref_closest_pair({{0,0},{2,0},{5,0}}), "P1: collinear");

    // P2: Segment Intersection
    check_bool_vec({true,false,false}, ref_segment_intersect({{{0,0},{2,2},{0,2},{2,0}},{{0,0},{1,0},{2,0},{3,0}},{{0,0},{1,1},{2,2},{3,3}}}), "P2: mixed");
    check_bool_vec({true}, ref_segment_intersect({{{0,0},{1,1},{1,1},{2,0}}}), "P2: touching");
    check_bool_vec({true}, ref_segment_intersect({{{0,0},{2,0},{1,0},{3,0}}}), "P2: overlap");

    // P3: Point in Polygon
    check_bool_vec({true,false,true,true}, ref_point_in_polygon({{0,0},{4,0},{4,4},{0,4}}, {{2,2},{5,5},{0,0},{4,2}}), "P3: square");
    check_bool_vec({true,false}, ref_point_in_polygon({{0,0},{2,0},{1,2}}, {{1,1},{3,3}}), "P3: triangle");
    check_bool_vec({true,true,true}, ref_point_in_polygon({{0,0},{4,0},{4,4},{0,4}}, {{2,0},{0,2},{4,4}}), "P3: boundary");

    // P4: Max Points on a Line
    check(3, ref_max_points({{1,1},{2,2},{3,3},{4,1}}), "P4: three");
    check(4, ref_max_points({{1,1},{3,2},{5,3},{4,1},{2,3},{1,4}}), "P4: four");
    check(1, ref_max_points({{0,0}}), "P4: single");
    check(2, ref_max_points({{0,0},{1,1}}), "P4: two");

    // C1: Hull Perimeter
    check_double(14.0, ref_hull_perimeter({{0,0},{4,0},{4,3},{0,3},{2,1}}), "C1: rectangle");
    check_double(2 + sqrt(2), ref_hull_perimeter({{0,0},{1,0},{0,1}}), "C1: triangle");
    check_double(0.0, ref_hull_perimeter({{5,5}}), "C1: single");
    check_double(10.0, ref_hull_perimeter({{0,0},{3,4}}), "C1: two points");

    // C2: Max Rectangle in Histogram
    check(10, ref_max_rect_histogram({2,1,5,6,2,3}), "C2: basic");
    check(4, ref_max_rect_histogram({2,4}), "C2: two bars");
    check(1, ref_max_rect_histogram({1}), "C2: single");
    check(9, ref_max_rect_histogram({1,2,3,4,5}), "C2: increasing");
    check(12, ref_max_rect_histogram({3,3,3,3}), "C2: all same");

    // C3: Rectangle Union Area
    check(7, ref_rect_union_area({{0,0,2,2},{1,1,3,3}}), "C3: overlapping");
    check(2, ref_rect_union_area({{0,0,1,1},{2,2,3,3}}), "C3: disjoint");
    check(100, ref_rect_union_area({{0,0,10,10},{1,1,9,9}}), "C3: contained");
    check(25, ref_rect_union_area({{0,0,5,5}}), "C3: single");
    check(19, ref_rect_union_area({{0,0,3,3},{1,1,4,4},{2,2,5,5}}), "C3: three overlap");

    cout << endl;
    if (failed_count == 0) {
        printf("All %d ch34 C++ tests passed!\n", passed);
    } else {
        printf("%d passed, %d failed.\n", passed, failed_count);
        return 1;
    }
    return 0;
}
