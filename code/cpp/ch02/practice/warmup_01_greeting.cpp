/*
 * Warmup 01: Greeting
 * ==============================
 * Chapter 2: Your First Programs
 *
 * PROBLEM
 * -------
 * Given a person's name, return a greeting message.
 *
 * INPUT FORMAT
 * ------------
 * A single line containing a name (may include spaces).
 *
 * OUTPUT FORMAT
 * -------------
 * Print "Hello, <name>!" (without quotes).
 *
 * CONSTRAINTS
 * -----------
 * 1 <= name.length() <= 100
 * Name contains only letters and spaces.
 *
 * EXAMPLES
 * --------
 * Input:  Maya
 * Output: Hello, Maya!
 *
 * Input:  Captain Hook
 * Output: Hello, Captain Hook!
 *
 * INSTRUCTIONS
 * ------------
 * Replace the "return "";" in the solve() function with your solution.
 * The main function handles input/output — don't change it.
 */

#include <iostream>
#include <string>
using namespace std;

/**
 * Return a greeting string for the given name.
 */
string solve(string name) {
    // TODO: Replace this with your solution
    return "";
}

// ── Do not change anything below this line ──────────────────────────
int main() {
    string name;
    getline(cin, name);
    cout << solve(name) << endl;
    return 0;
}
