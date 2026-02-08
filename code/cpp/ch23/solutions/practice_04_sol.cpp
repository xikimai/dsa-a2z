/*
 * Solution for Practice 4: Stock I
 * Chapter 23: Dynamic Programming I — The Foundation
 */

#include <algorithm>
#include <climits>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solve(vector<int> prices) {
    if (prices.empty()) return 0;
    int mn = prices[0], profit = 0;
    for (int i = 1; i < (int)prices.size(); i++) {
        profit = max(profit, prices[i] - mn);
        mn = min(mn, prices[i]);
    }
    return profit;
}

int main() {
    return 0;
}
