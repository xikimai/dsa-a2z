#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

int solve(vector<int> gas, vector<int> cost) {
    int totalGas = 0, totalCost = 0;
    for (int i = 0; i < (int)gas.size(); i++) {
        totalGas += gas[i]; totalCost += cost[i];
    }
    if (totalGas < totalCost) return -1;
    int start = 0, tank = 0;
    for (int i = 0; i < (int)gas.size(); i++) {
        tank += gas[i] - cost[i];
        if (tank < 0) { start = i + 1; tank = 0; }
    }
    return start;
}

int main() {
    int n; cin >> n;
    vector<int> gas(n), cost(n);
    for (int i = 0; i < n; i++) cin >> gas[i];
    for (int i = 0; i < n; i++) cin >> cost[i];
    cout << solve(gas, cost) << endl;
    return 0;
}
