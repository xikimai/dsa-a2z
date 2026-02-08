/*
 * Warmup 3: First Non-Repeating Character
 * =========================================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM:
 *   Given a string, return the first character that appears exactly once.
 *   If no such character exists, return "_".
 *
 * EXAMPLES:
 *   solve("aabbcdd")  -> "c"
 *   solve("aabb")     -> "_"
 *   solve("a")        -> "a"
 *   solve("")         -> "_"
 *
 * CONSTRAINTS:
 *   - 0 <= s.length() <= 10^5
 *   - s contains only lowercase English letters
 *
 * INSTRUCTIONS:
 *   Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

string solve(string s) {
    // TODO: Replace this with your solution
    return "_";
}

// -- Do not change anything below this line --------------------------
int main() {
    string s;
    getline(cin, s);
    cout << solve(s) << endl;
    return 0;
}
