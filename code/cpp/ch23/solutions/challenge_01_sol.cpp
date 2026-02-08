/*
 * Solution for Challenge 1: Stock III
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
    int b1 = -prices[0], s1 = 0, b2 = -prices[0], s2 = 0;
    for (int i = 1; i < (int)prices.size(); i++) {
        b1 = max(b1, -prices[i]);
        s1 = max(s1, b1 + prices[i]);
        b2 = max(b2, s1 - prices[i]);
        s2 = max(s2, b2 + prices[i]);
    }
    return s2;
}

int main() {
    return 0;
}
