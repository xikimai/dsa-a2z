/*
 * Solution -- Practice 4: Prime Factorization
 * =============================================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * APPROACH: Trial division up to sqrt(n). For each divisor d, count how
 *           many times it divides n. If n > 1 after the loop, the remaining
 *           value is a prime factor larger than sqrt(original n).
 * TIME:  O(sqrt(n))
 * SPACE: O(number of distinct prime factors)
 */

#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> solve(long long n) {
    vector<vector<int>> factors;
    for (long long d = 2; d * d <= n; d++) {
        if (n % d == 0) {
            int count = 0;
            while (n % d == 0) {
                count++;
                n /= d;
            }
            factors.push_back({(int)d, count});
        }
    }
    if (n > 1) {
        factors.push_back({(int)n, 1});
    }
    return factors;
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
