/*
 * Solution for Practice 5: Stock II
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
    int profit = 0;
    for (int i = 1; i < (int)prices.size(); i++)
        if (prices[i] > prices[i-1]) profit += prices[i] - prices[i-1];
    return profit;
}

int main() {
    return 0;
}
