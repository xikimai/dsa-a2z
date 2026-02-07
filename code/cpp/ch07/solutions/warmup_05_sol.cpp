/*
 * Solution -- Warmup 5: Armstrong Number
 * ========================================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * APPROACH: Count the number of digits, then sum each digit raised
 *           to that power. Compare sum to original.
 * TIME:  O(d) where d = number of digits
 * SPACE: O(1)
 */

#include <cmath>
#include <iostream>
using namespace std;

bool solve(long long n) {
    if (n < 0) return false;

    // Count digits
    int numDigits = 0;
    long long temp = n;
    if (n == 0) {
        numDigits = 1;
    } else {
        while (temp > 0) {
            numDigits++;
            temp /= 10;
        }
    }

    // Sum of digits^numDigits
    temp = n;
    long long sum = 0;
    while (temp > 0) {
        long long d = temp % 10;
        sum += (long long)pow(d, numDigits);
        temp /= 10;
    }

    return sum == n;
}

// -- Do not change anything below this line --------------------------
int main() {
    long long n;
    cin >> n;
    cout << (solve(n) ? "true" : "false") << endl;
    return 0;
}
