/*
 * Solution for Warmup 1: Climbing Stairs — return number of distinct ways to climb n stairs
 * Chapter 23: Dynamic Programming I — The Foundation
 */

#include <algorithm>
#include <climits>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solve(int n) {
    if (n <= 2) return n;
    int prev2 = 1, prev1 = 2;
    for (int i = 3; i <= n; i++) { int c = prev1 + prev2; prev2 = prev1; prev1 = c; }
    return prev1;
}

int main() {
    return 0;
}
