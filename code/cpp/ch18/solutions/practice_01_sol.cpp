#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<vector<int>> activities) {
    if (activities.empty()) return 0;
    sort(activities.begin(), activities.end(),
         [](auto& a, auto& b) { return a[1] < b[1]; });
    int count = 0, lastEnd = 0;
    for (auto& act : activities) {
        if (act[0] >= lastEnd) { count++; lastEnd = act[1]; }
    }
    return count;
}

int main() {
    int n; cin >> n;
    vector<vector<int>> activities(n, vector<int>(2));
    for (int i = 0; i < n; i++) cin >> activities[i][0] >> activities[i][1];
    cout << solve(activities) << endl;
    return 0;
}
