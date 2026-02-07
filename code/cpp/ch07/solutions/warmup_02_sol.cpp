/*
 * Solution -- Warmup 2: Reverse Number
 * ======================================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * APPROACH: Extract last digit with mod-10, build reversed number
 *           by multiplying by 10 and adding. Preserve sign.
 * TIME:  O(d) where d = number of digits
 * SPACE: O(1)
 */

#include <cstdlib>
#include <iostream>
using namespace std;

long long solve(long long n) {
    long long sign = (n < 0) ? -1 : 1;
    n = abs(n);
    long long reversed = 0;
    while (n > 0) {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    return sign * reversed;
}

// -- Do not change anything below this line --------------------------
int main() {
    long long n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
