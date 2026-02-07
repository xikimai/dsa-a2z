/*
 * Challenge 2: Sieve of Eratosthenes
 * ====================================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * PROBLEM:
 *   Given a positive integer n, return a sorted vector of ALL prime
 *   numbers from 2 to n (inclusive).
 *
 *   Use the Sieve of Eratosthenes:
 *   1. Create a boolean array of size n+1, all set to true.
 *   2. Mark 0 and 1 as not prime.
 *   3. For each i from 2 to sqrt(n), if i is still marked prime,
 *      mark all multiples of i starting from i*i as not prime.
 *   4. Collect all numbers still marked prime.
 *
 * EXAMPLES:
 *   solve(10) -> [2, 3, 5, 7]
 *   solve(1)  -> []
 *   solve(2)  -> [2]
 *   solve(30) -> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
 *
 * CONSTRAINTS:
 *   0 <= n <= 10^7
 *
 * INSTRUCTIONS:
 *   Replace the body with your solution.
 */

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
