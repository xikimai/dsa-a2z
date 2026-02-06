/*
 * Solution — Warmup 1: Greeting
 * =============================
 * Chapter 4: Functions
 *
 * APPROACH:
 *   Simple string concatenation. No edge cases to worry about — even
 *   an empty name produces "Hello, !".
 *
 * TIME COMPLEXITY:  O(n) where n = length of name (string concatenation)
 * SPACE COMPLEXITY: O(n) for the returned string
 */

#include <iostream>
#include <string>
using namespace std;

string solve(string name) {
    return "Hello, " + name + "!";
}

// -- Do not change anything below this line --------------------------
int main() {
    string name;
    getline(cin, name);
    cout << solve(name) << endl;
    return 0;
}
