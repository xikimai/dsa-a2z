#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

pair<int,int> solve(vector<vector<int>> jobs) {
    if (jobs.empty()) return {0, 0};
    sort(jobs.begin(), jobs.end(),
         [](auto& a, auto& b) { return a[2] > b[2]; });
    int maxDeadline = 0;
    for (auto& j : jobs) maxDeadline = max(maxDeadline, j[1]);
    vector<bool> slots(maxDeadline + 1, false);
    int count = 0, totalProfit = 0;
    for (auto& job : jobs) {
        for (int t = job[1]; t >= 1; t--) {
            if (!slots[t]) {
                slots[t] = true;
                count++;
                totalProfit += job[2];
                break;
            }
        }
    }
    return {count, totalProfit};
}

int main() {
    int n; cin >> n;
    vector<vector<int>> jobs(n, vector<int>(3));
    for (int i = 0; i < n; i++) cin >> jobs[i][0] >> jobs[i][1] >> jobs[i][2];
    auto [count, profit] = solve(jobs);
    cout << count << " " << profit << endl;
    return 0;
}
