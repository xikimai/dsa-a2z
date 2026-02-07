/*
 * Solution -- Warmup 4: Palindrome Number
 * =========================================
 * Chapter 7: Number Wizardry -- Math for Programmers
 *
 * APPROACH: Negative numbers are not palindromes. For non-negative,
 *           reverse the number and compare with the original.
 * TIME:  O(d) where d = number of digits
 * SPACE: O(1)
 */

#include <iostream>
using namespace std;

bool solve(long long n) {
    if (n < 0) return false;
    long long original = n;
    long long reversed = 0;
    while (n > 0) {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    return original == reversed;
}

// -- Do not change anything below this line --------------------------
int main() {
    long long n;
    cin >> n;
    cout << (solve(n) ? "true" : "false") << endl;
    return 0;
}
