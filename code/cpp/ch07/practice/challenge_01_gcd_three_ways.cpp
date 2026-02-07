/*
 * Challenge 1: GCD Three Ways
 * ============================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * PROBLEM:
 *   Implement three different GCD algorithms:
 *
 *   1. solve_subtract(a, b) -- Repeated subtraction
 *      While a != b, subtract the smaller from the larger.
 *
 *   2. solve_euclidean(a, b) -- Euclidean algorithm
 *      While b != 0, replace (a, b) with (b, a % b).
 *
 *   3. solve_extended(a, b) -- Extended Euclidean algorithm
 *      Returns {gcd, x, y} such that a*x + b*y = gcd.
 *
 *   solve(a, b) calls solve_euclidean.
 *
 * EXAMPLES:
 *   solve_subtract(48, 18)   -> 6
 *   solve_euclidean(48, 18)  -> 6
 *   solve_extended(35, 15)   -> {5, 1, -2}  (35*1 + 15*(-2) = 5)
 *
 * CONSTRAINTS:
 *   0 <= a, b <= 10^18
 *   For solve_subtract: a, b > 0
 *
 * INSTRUCTIONS:
 *   Replace each "return 0;" / "return {0,0,0};" with your solution.
 */

#include <iostream>
#include <vector>
using namespace std;

long long solve_subtract(long long a, long long b) {
    // TODO: Replace this with your solution
    return 0;
}

long long solve_euclidean(long long a, long long b) {
    // TODO: Replace this with your solution
    return 0;
}

vector<long long> solve_extended(long long a, long long b) {
    // TODO: Replace this with your solution
    return {0, 0, 0};
}

long long solve(long long a, long long b) {
    return solve_euclidean(a, b);
}

// -- Do not change anything below this line --------------------------
int main() {
    long long a, b;
    cin >> a >> b;
    cout << "subtract:  " << solve_subtract(a, b) << endl;
    cout << "euclidean: " << solve_euclidean(a, b) << endl;
    vector<long long> ext = solve_extended(a, b);
    cout << "extended:  gcd=" << ext[0]
         << " x=" << ext[1] << " y=" << ext[2] << endl;
    return 0;
}
