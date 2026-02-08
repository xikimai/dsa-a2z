/*
 * Solution for Challenge 2: Stock with Cooldown
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
    int held = -prices[0], sold = 0, rest = 0;
    for (int i = 1; i < (int)prices.size(); i++) {
        int ph = held;
        held = max(held, rest - prices[i]);
        rest = max(rest, sold);
        sold = ph + prices[i];
    }
    return max(sold, rest);
}

int main() {
    return 0;
}
