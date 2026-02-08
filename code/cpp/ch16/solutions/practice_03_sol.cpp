/* Solution: Practice 3 — Search in 2D Matrix (Ch 16) */
#include <vector>
using namespace std;
vector<int> solve(vector<vector<int>> matrix, int target) {
    if (matrix.empty() || matrix[0].empty()) return {-1, -1};
    int rows = matrix.size(), cols = matrix[0].size();
    int lo = 0, hi = rows * cols - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        int val = matrix[mid / cols][mid % cols];
        if (val == target) return {mid / cols, mid % cols};
        else if (val < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return {-1, -1};
}
