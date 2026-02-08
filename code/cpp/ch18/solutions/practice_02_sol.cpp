#include <algorithm>
#include <iomanip>
#include <iostream>
#include <vector>
using namespace std;

double solve(int capacity, vector<pair<int,int>> items) {
    if (capacity == 0 || items.empty()) return 0.0;
    sort(items.begin(), items.end(), [](auto& a, auto& b) {
        return (double)a.second / a.first > (double)b.second / b.first;
    });
    double totalValue = 0.0;
    int remaining = capacity;
    for (auto& [w, v] : items) {
        if (remaining <= 0) break;
        int take = min(w, remaining);
        totalValue += take * ((double)v / w);
        remaining -= take;
    }
    return totalValue;
}

int main() {
    int cap, n; cin >> cap >> n;
    vector<pair<int,int>> items(n);
    for (int i = 0; i < n; i++) cin >> items[i].first >> items[i].second;
    cout << fixed << setprecision(4) << solve(cap, items) << endl;
    return 0;
}
