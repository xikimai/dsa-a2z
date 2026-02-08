#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<vector<int>> intervals) {
    if (intervals.empty()) return 0;
    sort(intervals.begin(), intervals.end(),
         [](auto& a, auto& b) { return a[1] < b[1]; });
    int keep = 0, lastEnd = INT_MIN;
    for (auto& iv : intervals) {
        if (iv[0] >= lastEnd) { keep++; lastEnd = iv[1]; }
    }
    return (int)intervals.size() - keep;
}

int main() {
    int n; cin >> n;
    vector<vector<int>> intervals(n, vector<int>(2));
    for (int i = 0; i < n; i++) cin >> intervals[i][0] >> intervals[i][1];
    cout << solve(intervals) << endl;
    return 0;
}
