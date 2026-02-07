/*
 * Solution -- Practice 5: Trailing Zeros in Factorial
 * ====================================================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * APPROACH: Count factors of 5 in n!. Each multiple of 5 contributes one 5,
 *           each multiple of 25 contributes an extra, etc.
 *           count = n/5 + n/25 + n/125 + ...
 * TIME:  O(log_5(n))
 * SPACE: O(1)
 */

#include <iostream>
using namespace std;

int solve(int n) {
    int count = 0;
    long long p = 5;
    while (p <= n) {
        count += (int)(n / p);
        p *= 5;
    }
    return count;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
