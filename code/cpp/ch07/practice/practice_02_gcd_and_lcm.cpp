/*
 * Practice 2: GCD and LCM
 * =======================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * PROBLEM:
 *   Given two non-negative integers a and b, return a vector
 *   containing {gcd(a, b), lcm(a, b)}.
 *
 *   Use the Euclidean algorithm for GCD.
 *   LCM can be computed as: lcm(a, b) = a / gcd(a, b) * b
 *   (divide first to avoid overflow!)
 *
 *   If either is 0, the LCM is 0.
 *
 * EXAMPLES:
 *   solve(12, 18)  -> [6, 36]
 *   solve(7, 13)   -> [1, 91]
 *   solve(0, 5)    -> [5, 0]
 *   solve(100, 75) -> [25, 300]
 *
 * CONSTRAINTS:
 *   0 <= a, b <= 10^18
 *
 * INSTRUCTIONS:
 *   Replace the body with your solution.
 */

#include <iostream>
#include <vector>
using namespace std;

vector<long long> solve(long long a, long long b) {
    // TODO: Replace this with your solution
    return {0, 0};
}

// -- Do not change anything below this line --------------------------
int main() {
    long long a, b;
    cin >> a >> b;
    vector<long long> result = solve(a, b);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}
