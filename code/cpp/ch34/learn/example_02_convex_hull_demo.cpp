/*
 * Example 02: Convex Hull Demo — Andrew's Monotone Chain
 * =======================================================
 * Chapter 34: Computational Geometry & Sweep Line
 *
 * Demonstrates convex hull construction step by step.
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

long long cross(vector<int>& o, vector<int>& a, vector<int>& b) {
    return (long long)(a[0] - o[0]) * (b[1] - o[1])
         - (long long)(a[1] - o[1]) * (b[0] - o[0]);
}

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

    hull.pop_back();
    return hull;
}

int main() {
    cout << string(60, '=') << endl;
    cout << "CONVEX HULL: Andrew's Monotone Chain" << endl;
    cout << string(60, '=') << endl;

    vector<vector<int>> points = {{0,0},{2,0},{2,2},{0,2},{1,1}};
    cout << "\nInput: (0,0),(2,0),(2,2),(0,2),(1,1)" << endl;

    auto hull = convexHull(points);
    cout << "Hull: ";
    for (auto& p : hull) cout << "(" << p[0] << "," << p[1] << ") ";
    cout << endl;
    cout << "Point (1,1) is interior — not on hull!" << endl;

    return 0;
}
