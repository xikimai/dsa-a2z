/*
 * Practice 2: Anagram Check
 * =========================
 * Chapter 5: Collections
 *
 * PROBLEM:
 *   Determine if two strings are anagrams of each other.
 *   The comparison should be case-insensitive.
 *
 * EXAMPLES:
 *   solve("listen", "silent") -> true
 *   solve("hello", "world")   -> false
 *   solve("Dormitory", "dirty room") -> false  (spaces count!)
 *
 * CONSTRAINTS:
 *   - 0 <= s1.length(), s2.length() <= 10^5
 *   - Strings contain printable ASCII characters
 */

#include <iostream>
#include <string>
using namespace std;

/**
 * Returns true if s1 and s2 are anagrams (case-insensitive).
 */
bool solve(string s1, string s2) {
    // TODO: Replace this with your solution
    return false;
}

// -- Do not change anything below this line --------------------------
int main() {
    string s1, s2;
    getline(cin, s1);
    getline(cin, s2);
    cout << (solve(s1, s2) ? "true" : "false") << endl;
    return 0;
}
