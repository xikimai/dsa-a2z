/*
 * Solution -- Warmup 2: Sum of First N Natural Numbers
 * ======================================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Base case n==0 returns 0. Otherwise n + solve(n-1).
 * TIME:  O(n)
 * SPACE: O(n) call stack
 */

#include <iostream>
using namespace std;

int solve(int n) {
    if (n == 0) return 0;
    return n + solve(n - 1);
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
