/*
 * Practice 5: Sort Characters by Frequency
 * ==========================================
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * PROBLEM:
 *   Given a string, sort it in decreasing order based on the frequency
 *   of each character. If two characters have the same frequency,
 *   sort them alphabetically (ascending).
 *
 * EXAMPLES:
 *   solve("tree")    -> "eert"
 *   solve("cccaaa")  -> "aaaccc"
 *   solve("aab")     -> "aab"
 *   solve("hello")   -> "lleho"
 *
 * CONSTRAINTS:
 *   - 0 <= s.length() <= 10^5
 *   - s contains printable ASCII characters
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
    return "";
}

// -- Do not change anything below this line --------------------------
int main() {
    string s;
    getline(cin, s);
    cout << solve(s) << endl;
    return 0;
}
