/*
 * Solution for Challenge 3: Ninja Training
 * Chapter 24: Dynamic Programming II — Grids and Paths
 */

#include <algorithm>
#include <climits>
#include <vector>
using namespace std;

int solve(vector<vector<int>>& points) {
    int prev[3] = {points[0][0], points[0][1], points[0][2]};
    for (int i = 1; i < (int)points.size(); i++) {
        int curr[3] = {0, 0, 0};
        for (int j = 0; j < 3; j++)
            for (int k = 0; k < 3; k++)
                if (k != j)
                    curr[j] = max(curr[j], prev[k] + points[i][j]);
        prev[0] = curr[0]; prev[1] = curr[1]; prev[2] = curr[2];
    }
    return max({prev[0], prev[1], prev[2]});
}

int main() { return 0; }
