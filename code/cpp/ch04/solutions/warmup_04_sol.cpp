/*
 * Solution — Warmup 4: Repeat String
 * ===================================
 * Chapter 4: Functions
 *
 * APPROACH:
 *   Loop n times, appending the string each iteration.
 *   Add a space separator between repetitions (but not after the last one).
 *   Handle n=0 by returning empty string.
 *
 * TIME COMPLEXITY:  O(n * len(s))
 * SPACE COMPLEXITY: O(n * len(s)) for the result string
 */

#include <iostream>
#include <string>
using namespace std;

string solve(string s, int n = 3) {
    if (n <= 0) return "";
    string result = "";
    for (int i = 0; i < n; i++) {
        if (i > 0) result += " ";
        result += s;
    }
    return result;
}

// -- Do not change anything below this line --------------------------
int main() {
    string s;
    int n;
    cin >> s >> n;
    cout << solve(s, n) << endl;
    return 0;
}
