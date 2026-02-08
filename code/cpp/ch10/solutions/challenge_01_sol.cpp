/*
 * Solution -- Challenge 1: Fibonacci Three Ways
 * ================================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH:
 *   Naive: direct recursion, O(2^n) time.
 *   Memo:  unordered_map-based helper, O(n) time.
 *   Iter:  two-variable loop, O(n) time, O(1) space.
 */

#include <iostream>
#include <unordered_map>
using namespace std;

long long solve_naive(int n) {
    if (n <= 1) return n;
    return solve_naive(n - 1) + solve_naive(n - 2);
}

long long memo_helper(int n, unordered_map<int, long long>& memo) {
    if (n <= 1) return n;
    if (memo.count(n)) return memo[n];
    memo[n] = memo_helper(n - 1, memo) + memo_helper(n - 2, memo);
    return memo[n];
}

long long solve_memo(int n) {
    unordered_map<int, long long> memo;
    return memo_helper(n, memo);
}

long long solve_iter(int n) {
    if (n <= 1) return n;
    long long a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        long long temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

long long solve(int n) {
    return solve_iter(n);
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
