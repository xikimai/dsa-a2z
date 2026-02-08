/*
 * Solution -- Warmup 3: Reverse String
 * =======================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Base case: string of length 0 or 1 returns itself.
 *           Otherwise: reverse the substring after the first char,
 *           then append the first char.
 * TIME:  O(n^2) due to substring creation
 * SPACE: O(n^2) due to substring copies on call stack
 */

#include <iostream>
#include <string>
using namespace std;

string solve(string s) {
    if (s.size() <= 1) return s;
    return solve(s.substr(1)) + s[0];
}

// -- Do not change anything below this line --------------------------
int main() {
    string s;
    getline(cin, s);
    cout << solve(s) << endl;
    return 0;
}
