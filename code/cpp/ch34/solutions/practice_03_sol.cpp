/*
 * Solution for Practice 3: Point in Polygon
 * Chapter 34: Computational Geometry & Sweep Line
 */
#include <algorithm>
#include <vector>
using namespace std;

bool pointInPoly_p3(vector<vector<int>>& poly, int px, int py) {
    int n = poly.size();

    // Boundary check
    for (int i = 0; i < n; i++) {
        int j = (i + 1) % n;
        long long cp = (long long)(poly[j][0] - poly[i][0]) * (py - poly[i][1])
                     - (long long)(poly[j][1] - poly[i][1]) * (px - poly[i][0]);
        if (cp == 0
            && px >= min(poly[i][0], poly[j][0])
            && px <= max(poly[i][0], poly[j][0])
            && py >= min(poly[i][1], poly[j][1])
            && py <= max(poly[i][1], poly[j][1]))
            return true;
    }

    // Ray casting
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

vector<bool> solve(vector<vector<int>>& polygon, vector<vector<int>>& queries) {
    vector<bool> result;
    for (auto& q : queries) {
        result.push_back(pointInPoly_p3(polygon, q[0], q[1]));
    }
    return result;
}

int main() { return 0; }
