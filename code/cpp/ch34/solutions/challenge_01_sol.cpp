/*
 * Solution for Challenge 1: Convex Hull Perimeter
 * Chapter 34: Computational Geometry & Sweep Line
 */
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;

long long cross_c1(vector<int>& o, vector<int>& a, vector<int>& b) {
    return (long long)(a[0] - o[0]) * (b[1] - o[1])
         - (long long)(a[1] - o[1]) * (b[0] - o[0]);
}

double solve(vector<vector<int>>& points) {
    auto pts = points;
    sort(pts.begin(), pts.end());
    pts.erase(unique(pts.begin(), pts.end()), pts.end());
    int n = pts.size();

    if (n <= 1) return 0.0;
    if (n == 2) {
        return 2.0 * sqrt((double)(pts[0][0]-pts[1][0])*(pts[0][0]-pts[1][0])
                         + (double)(pts[0][1]-pts[1][1])*(pts[0][1]-pts[1][1]));
    }

    vector<vector<int>> hull;
    for (auto& p : pts) {
        while (hull.size() >= 2 && cross_c1(hull[hull.size()-2], hull[hull.size()-1], p) <= 0)
            hull.pop_back();
        hull.push_back(p);
    }
    int lower = hull.size() + 1;
    for (int i = n - 2; i >= 0; i--) {
        while ((int)hull.size() >= lower && cross_c1(hull[hull.size()-2], hull[hull.size()-1], pts[i]) <= 0)
            hull.pop_back();
        hull.push_back(pts[i]);
    }
    hull.pop_back();

    int k = hull.size();
    double perimeter = 0.0;
    for (int i = 0; i < k; i++) {
        int j = (i + 1) % k;
        double dx = hull[i][0] - hull[j][0];
        double dy = hull[i][1] - hull[j][1];
        perimeter += sqrt(dx * dx + dy * dy);
    }
    return perimeter;
}

int main() { return 0; }
