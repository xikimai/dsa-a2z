/*
 * Warmup 4: Check Palindrome
 * ============================
 * Chapter 10: The Magic of Recursion
 *
 * PROBLEM:
 *   Given a string s, return true if it is a palindrome, false otherwise.
 *   Use recursion (compare first and last characters, then recurse on
 *   the middle substring).
 *
 * EXAMPLES:
 *   solve("racecar") -> true
 *   solve("hello")   -> false
 *   solve("")         -> true
 *   solve("a")        -> true
 *   solve("aa")       -> true
 *   solve("ab")       -> false
 *
 * CONSTRAINTS:
 *   0 <= s.length() <= 10^4
 *
 * INSTRUCTIONS:
 *   Replace the body with your recursive solution.
 */

#include <iostream>
#include <string>
using namespace std;

bool solve(string s) {
    // TODO: Replace this with your solution
    return false;
}

// -- Do not change anything below this line --------------------------
int main() {
    string s;
    getline(cin, s);
    cout << (solve(s) ? "true" : "false") << endl;
    return 0;
}
