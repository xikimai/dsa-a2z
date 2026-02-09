/*
 * Solution for Practice 2: Line Segment Intersection
 * Chapter 34: Computational Geometry & Sweep Line
 */
#include <algorithm>
#include <vector>
using namespace std;

long long cross_p2(vector<int>& o, vector<int>& a, vector<int>& b) {
    return (long long)(a[0] - o[0]) * (b[1] - o[1])
         - (long long)(a[1] - o[1]) * (b[0] - o[0]);
}

int orient_p2(vector<int>& a, vector<int>& b, vector<int>& c) {
    long long cp = cross_p2(a, b, c);
    if (cp > 0) return 1;
    if (cp < 0) return -1;
    return 0;
}

bool onSeg_p2(vector<int>& p, vector<int>& q, vector<int>& r) {
    return q[0] >= min(p[0], r[0]) && q[0] <= max(p[0], r[0])
        && q[1] >= min(p[1], r[1]) && q[1] <= max(p[1], r[1]);
}

bool intersects_p2(vector<int>& a, vector<int>& b, vector<int>& c, vector<int>& d) {
    int d1 = orient_p2(c, d, a), d2 = orient_p2(c, d, b);
    int d3 = orient_p2(a, b, c), d4 = orient_p2(a, b, d);
    if (d1 * d2 < 0 && d3 * d4 < 0) return true;
    if (d1 == 0 && onSeg_p2(c, a, d)) return true;
    if (d2 == 0 && onSeg_p2(c, b, d)) return true;
    if (d3 == 0 && onSeg_p2(a, c, b)) return true;
    if (d4 == 0 && onSeg_p2(a, d, b)) return true;
    return false;
}

vector<bool> solve(vector<vector<vector<int>>>& segments) {
    vector<bool> result;
    for (auto& seg : segments) {
        auto a = seg[0], b = seg[1], c = seg[2], d = seg[3];
        result.push_back(intersects_p2(a, b, c, d));
    }
    return result;
}

int main() { return 0; }
