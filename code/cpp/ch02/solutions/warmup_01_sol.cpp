/*
 * Solution for Warmup 01: Greeting
 * ==================================
 * Chapter 2: Your First Programs
 *
 * This is the reference solution. Try to solve the problem yourself before
 * looking at this!
 *
 * APPROACH
 * --------
 * Use string concatenation to build the greeting.
 * In C++, you can concatenate strings with the + operator.
 *
 * TIME COMPLEXITY:  O(n) — where n is the length of the name
 * SPACE COMPLEXITY: O(n) — for the new string
 */

#include <iostream>
#include <string>
using namespace std;

/**
 * Return a greeting string for the given name.
 */
string solve(string name) {
    return "Hello, " + name + "!";
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    string name;
    getline(cin, name);
    cout << solve(name) << endl;
    return 0;
}
