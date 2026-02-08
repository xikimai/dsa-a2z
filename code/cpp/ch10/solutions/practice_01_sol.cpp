/*
 * Solution -- Practice 1: Fibonacci Number
 * ==========================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Memoized recursion using unordered_map.
 *           Helper takes map by reference to cache results.
 * TIME:  O(n)
 * SPACE: O(n) for the map + call stack
 */

#include <iostream>
#include <unordered_map>
using namespace std;

int fib_helper(int n, unordered_map<int, int>& memo) {
    if (n <= 1) return n;
    if (memo.count(n)) return memo[n];
    memo[n] = fib_helper(n - 1, memo) + fib_helper(n - 2, memo);
    return memo[n];
}

int solve(int n) {
    unordered_map<int, int> memo;
    return fib_helper(n, memo);
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
