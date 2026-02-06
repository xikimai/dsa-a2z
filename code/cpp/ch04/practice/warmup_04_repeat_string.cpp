/*
 * Warmup 4: Repeat String
 * =======================
 * Chapter 4: Functions
 *
 * PROBLEM:
 *   Repeat a string n times, separated by spaces.
 *   The parameter n has a default value of 3.
 *
 * EXAMPLES:
 *   solve("ha", 3)   -> "ha ha ha"
 *   solve("yo", 2)   -> "yo yo"
 *   solve("ok", 1)   -> "ok"
 *   solve("abc")      -> "abc abc abc"  (uses default n=3)
 *   solve("hi", 0)   -> ""
 *
 * CONSTRAINTS:
 *   - n >= 0
 *   - s can be any string
 */

#include <iostream>
#include <string>
using namespace std;

/**
 * Returns s repeated n times, separated by spaces.
 */
string solve(string s, int n = 3) {
    // TODO: Replace this with your solution
    return "";
}

// -- Do not change anything below this line --------------------------
int main() {
    string s;
    int n;
    cin >> s >> n;
    cout << solve(s, n) << endl;
    return 0;
}
