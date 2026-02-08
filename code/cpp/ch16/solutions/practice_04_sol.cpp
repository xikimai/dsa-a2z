/* Solution: Practice 4 — Row with Maximum 1s (Ch 16) */
#include <vector>
using namespace std;
int solve(vector<vector<int>> matrix) {
    if (matrix.empty() || matrix[0].empty()) return -1;
    int bestRow = -1, bestCount = 0;
    int cols = matrix[0].size();
    for (int i = 0; i < (int)matrix.size(); i++) {
        int lo = 0, hi = cols;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (matrix[i][mid] == 1) hi = mid;
            else lo = mid + 1;
        }
        int count = cols - lo;
        if (count > bestCount) { bestCount = count; bestRow = i; }
    }
    return bestRow;
}
