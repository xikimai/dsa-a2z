/*
 * Solution -- Warmup 1: Count Digits
 * ====================================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * APPROACH: mod-10/div-10 loop with abs(n). 0 is special case.
 * TIME:  O(d) where d = number of digits
 * SPACE: O(1)
 */

#include <cstdlib>
#include <iostream>
using namespace std;

int solve(long long n) {
    n = abs(n);
    if (n == 0) return 1;
    int count = 0;
    while (n > 0) {
        count++;
        n /= 10;
    }
    return count;
}

// -- Do not change anything below this line --------------------------
int main() {
    long long n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
