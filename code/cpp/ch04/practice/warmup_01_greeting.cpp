/*
 * Warmup 1: Greeting
 * ==================
 * Chapter 4: Functions
 *
 * PROBLEM:
 *   Write a function that takes a person's name and returns a greeting string.
 *
 * EXAMPLES:
 *   solve("Maya")  -> "Hello, Maya!"
 *   solve("World") -> "Hello, World!"
 *   solve("")      -> "Hello, !"
 *
 * CONSTRAINTS:
 *   - name can be any string (including empty)
 *   - Return format is exactly: "Hello, {name}!"
 */

#include <iostream>
#include <string>
using namespace std;

/**
 * Returns a greeting string for the given name.
 */
string solve(string name) {
    // TODO: Replace this with your solution
    return "";
}

// -- Do not change anything below this line --------------------------
int main() {
    string name;
    getline(cin, name);
    cout << solve(name) << endl;
    return 0;
}
