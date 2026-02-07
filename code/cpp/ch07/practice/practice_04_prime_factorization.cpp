/*
 * Practice 4: Prime Factorization
 * ================================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * PROBLEM:
 *   Given a positive integer n, return its prime factorization as a
 *   vector of {prime, exponent} pairs in ascending order of prime.
 *
 *   Return an empty vector if n <= 1.
 *
 * EXAMPLES:
 *   solve(12)  -> [[2,2], [3,1]]       (12 = 2^2 * 3^1)
 *   solve(1)   -> []
 *   solve(7)   -> [[7,1]]              (7 is prime)
 *   solve(360) -> [[2,3], [3,2], [5,1]] (360 = 2^3 * 3^2 * 5^1)
 *
 * CONSTRAINTS:
 *   1 <= n <= 10^12
 *
 * INSTRUCTIONS:
 *   Replace the body with your solution.
 *   Hint: Trial division up to sqrt(n). If anything remains after
 *   the loop, it's a prime factor > sqrt(n).
 */

#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> solve(long long n) {
    // TODO: Replace this with your solution
    return {};
}

// -- Do not change anything below this line --------------------------
int main() {
    long long n;
    cin >> n;
    vector<vector<int>> result = solve(n);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i][0] << "^" << result[i][1];
    }
    cout << endl;
    return 0;
}
