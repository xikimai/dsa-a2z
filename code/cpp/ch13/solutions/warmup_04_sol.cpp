/*
 * Solution for Warmup 4: Count Binary Strings
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * APPROACH: Fibonacci-like DP. a = strings ending in 0, b = ending in 1.
 * TIME:  O(n)
 * SPACE: O(1)
 */

#include <iostream>
using namespace std;

int solve(int n) {
    if (n == 1) return 2;
    int a = 1, b = 1;  // n=1: "0" and "1"
    for (int i = 2; i <= n; i++) {
        int new_a = a + b;
        int new_b = a;
        a = new_a;
        b = new_b;
    }
    return a + b;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
