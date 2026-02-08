/*
 * Solution -- Warmup 1: Factorial
 * =================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Base case n==0 returns 1. Otherwise n * solve(n-1).
 * TIME:  O(n)
 * SPACE: O(n) call stack
 */

#include <iostream>
using namespace std;

long long solve(int n) {
    if (n == 0) return 1;
    return (long long)n * solve(n - 1);
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
