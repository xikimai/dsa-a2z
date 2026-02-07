/*
 * Solution -- Warmup 3: Sum of Digits
 * =====================================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * APPROACH: Take abs(n), then extract and sum each digit using mod-10/div-10.
 * TIME:  O(d) where d = number of digits
 * SPACE: O(1)
 */

#include <cstdlib>
#include <iostream>
using namespace std;

int solve(long long n) {
    n = abs(n);
    int sum = 0;
    while (n > 0) {
        sum += (int)(n % 10);
        n /= 10;
    }
    return sum;
}

// -- Do not change anything below this line --------------------------
int main() {
    long long n;
    cin >> n;
    cout << solve(n) << endl;
    return 0;
}
