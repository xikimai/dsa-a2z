/*
 * Solution for Warmup 3: First Non-Repeating Character
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Count character frequencies, then scan the string again
 *           to find the first character with count == 1.
 * TIME:  O(n)
 * SPACE: O(1) — at most 26 letters
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

string solve(string s) {
    unordered_map<char, int> freq;
    for (char c : s) {
        freq[c]++;
    }
    for (char c : s) {
        if (freq[c] == 1) {
            return string(1, c);
        }
    }
    return "_";
}

// -- Do not change anything below this line --------------------------
int main() {
    string s;
    getline(cin, s);
    cout << solve(s) << endl;
    return 0;
}
