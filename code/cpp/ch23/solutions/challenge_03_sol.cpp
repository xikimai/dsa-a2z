/*
 * Solution for Challenge 3: Stock with Transaction Fee
 * Chapter 23: Dynamic Programming I — The Foundation
 */

#include <algorithm>
#include <climits>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solve(vector<int> prices, int fee) {
    if (prices.empty()) return 0;
    int cash = 0, hold = -prices[0];
    for (int i = 1; i < (int)prices.size(); i++) {
        cash = max(cash, hold + prices[i] - fee);
        hold = max(hold, cash - prices[i]);
    }
    return cash;
}

int main() {
    return 0;
}
