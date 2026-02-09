/*
 * Solution for Warmup 3: Polygon Area (Shoelace Formula)
 * Chapter 34: Computational Geometry & Sweep Line
 */
#include <cmath>
#include <vector>
using namespace std;

double solve(vector<vector<int>>& polygon) {
    int n = polygon.size();
    long long area = 0;
    for (int i = 0; i < n; i++) {
        int j = (i + 1) % n;
        area += (long long)polygon[i][0] * polygon[j][1];
        area -= (long long)polygon[j][0] * polygon[i][1];
    }
    return abs(area) / 2.0;
}

int main() { return 0; }
