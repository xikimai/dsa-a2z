/*
 * Practice 1: All Divisors
 * ========================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * PROBLEM:
 *   Given a positive integer n, return ALL its divisors in sorted order.
 *
 * EXAMPLES:
 *   solve(36) -> [1, 2, 3, 4, 6, 9, 12, 18, 36]
 *   solve(1)  -> [1]
 *   solve(7)  -> [1, 7]
 *   solve(12) -> [1, 2, 3, 4, 6, 12]
 *
 * CONSTRAINTS:
 *   1 <= n <= 10^9
 *
 * INSTRUCTIONS:
 *   Replace the body with your solution.
 *   Hint: You only need to check divisors up to sqrt(n).
 *   If i divides n, then both i and n/i are divisors.
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(int n) {
    // TODO: Replace this with your solution
    return {};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> result = solve(n);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
