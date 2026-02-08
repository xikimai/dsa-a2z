/*
 * Solution for Warmup 3: Min Cost Climbing Stairs
 * Chapter 23: Dynamic Programming I — The Foundation
 */

#include <algorithm>
#include <climits>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solve(vector<int> cost) {
    int n = cost.size();
    int prev2 = 0, prev1 = 0;
    for (int i = 2; i <= n; i++) {
        int c = min(prev1 + cost[i-1], prev2 + cost[i-2]);
        prev2 = prev1; prev1 = c;
    }
    return prev1;
}

int main() {
    return 0;
}
