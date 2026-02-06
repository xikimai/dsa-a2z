/*
 * Practice 2: Password Strength
 * =============================
 * Chapter 4: Functions
 *
 * PROBLEM:
 *   Evaluate password strength using helper functions.
 *   Write helpers: has_digit(string), has_upper(string).
 *
 *   Rules:
 *     "weak"   — length < 8
 *     "medium" — length >= 8, but missing digit OR uppercase
 *     "strong" — length >= 8 AND has digit AND has uppercase
 *
 * EXAMPLES:
 *   solve("hi")          -> "weak"     (too short)
 *   solve("abcdefgh")    -> "medium"   (no digit, no uppercase)
 *   solve("abcdefg1")    -> "medium"   (has digit, no uppercase)
 *   solve("Abcdefgh")    -> "medium"   (has uppercase, no digit)
 *   solve("Abcdefg1")    -> "strong"   (has both)
 *   solve("PASSWORD1")   -> "strong"
 *
 * CONSTRAINTS:
 *   - password is a non-empty string
 *   - Only check length, digits, and uppercase letters
 */

#include <iostream>
#include <string>
using namespace std;

// TODO: Write helper functions: has_digit(string), has_upper(string)

/**
 * Returns "weak", "medium", or "strong" based on the password rules.
 */
string solve(string password) {
    // TODO: Replace this with your solution
    return "";
}

// -- Do not change anything below this line --------------------------
int main() {
    string password;
    getline(cin, password);
    cout << solve(password) << endl;
    return 0;
}
