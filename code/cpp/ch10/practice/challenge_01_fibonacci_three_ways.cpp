/*
 * Challenge 1: Fibonacci Three Ways
 * ====================================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM:
 *   Implement the nth Fibonacci number THREE different ways:
 *     solve_naive(n) -- pure recursion (exponential time)
 *     solve_memo(n)  -- recursion with memoization (linear time)
 *     solve_iter(n)  -- iterative with two variables (linear time)
 *     solve(n)       -- calls solve_iter (the best approach)
 *
 * EXAMPLES:
 *   solve_naive(10) -> 55
 *   solve_memo(30)  -> 832040
 *   solve_iter(30)  -> 832040
 *   solve(30)       -> 832040
 *
 * CONSTRAINTS:
 *   0 <= n <= 50 (for memo and iter)
 *   0 <= n <= 30 (for naive -- too slow beyond this!)
 *   Use long long to handle large values.
 *
 * INSTRUCTIONS:
 *   Replace all four function bodies with your solutions.
 */

#include <iostream>
#include <unordered_map>
using namespace std;

long long solve_naive(int n) {
    // TODO: Pure recursion (no optimization)
    return 0;
}

long long solve_memo(int n) {
    // TODO: Recursion with memoization (unordered_map)
    return 0;
}

long long solve_iter(int n) {
    // TODO: Iterative with two variables
    return 0;
}

long long solve(int n) {
    // TODO: Call solve_iter
    return solve_iter(n);
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
