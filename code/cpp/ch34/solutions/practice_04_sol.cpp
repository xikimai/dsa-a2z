/*
 * Solution for Practice 4: Maximum Points on a Line
 * Chapter 34: Computational Geometry & Sweep Line
 */
#include <algorithm>
#include <map>
#include <numeric>
#include <vector>
using namespace std;

int solve(vector<vector<int>>& points) {
    int n = points.size();
    if (n <= 2) return n;

    int best = 1;
    for (int i = 0; i < n; i++) {
        map<pair<int,int>, int> slopes;
        int dup = 1;
        for (int j = i + 1; j < n; j++) {
            int dx = points[j][0] - points[i][0];
            int dy = points[j][1] - points[i][1];

            if (dx == 0 && dy == 0) {
                dup++;
                continue;
            }

            int g = gcd(abs(dx), abs(dy));
            dx /= g;
            dy /= g;
            if (dx < 0 || (dx == 0 && dy < 0)) {
                dx = -dx;
                dy = -dy;
            }

            slopes[{dx, dy}]++;
        }

        int localMax = dup;
        for (auto& [k, cnt] : slopes) {
            localMax = max(localMax, cnt + dup);
        }
        best = max(best, localMax);
    }
    return best;
}

int main() { return 0; }
