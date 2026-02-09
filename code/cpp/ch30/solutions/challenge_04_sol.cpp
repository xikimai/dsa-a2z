/*
 * Solution: Challenge 4 — Interval Scheduling
 */
#include <algorithm>
#include <vector>
using namespace std;
int solve(vector<vector<int>> intervals) {
    if (intervals.empty()) return 0;
    sort(intervals.begin(), intervals.end(), [](auto& a, auto& b) { return a[1] < b[1]; });
    int count = 1, lastEnd = intervals[0][1];
    for (int i = 1; i < (int)intervals.size(); i++) {
        if (intervals[i][0] >= lastEnd) { count++; lastEnd = intervals[i][1]; }
    }
    return count;
}
int main() { return 0; }
