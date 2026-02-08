/*
 * Warmup 4: Valid Anagram
 * ========================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM:
 *   Given two strings s1 and s2, return true if s2 is an anagram of s1,
 *   false otherwise.
 *
 * EXAMPLES:
 *   solve("listen", "silent")  -> true
 *   solve("hello", "world")    -> false
 *   solve("", "")              -> true
 *   solve("ab", "ba")          -> true
 *
 * CONSTRAINTS:
 *   - 0 <= s1.length(), s2.length() <= 10^5
 *   - s1 and s2 contain only lowercase English letters
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

bool solve(string s1, string s2) {
    // TODO: Replace this with your solution
    return false;
}

// -- Do not change anything below this line --------------------------
int main() {
    string s1, s2;
    cin >> s1 >> s2;
    cout << (solve(s1, s2) ? "true" : "false") << endl;
    return 0;
}
