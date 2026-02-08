/*
 * Solution for Practice 6: Tribonacci Number
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
    if (n == 0) return 0;
    if (n <= 2) return 1;
    int a = 0, b = 1, c = 1;
    for (int i = 3; i <= n; i++) { int next = a+b+c; a = b; b = c; c = next; }
    return c;
}

int main() {
    return 0;
}
