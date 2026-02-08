/*
 * Solution for Warmup 4: Valid Anagram
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Count character frequencies for both strings using a map.
 *           Increment for s1, decrement for s2. All counts should be 0.
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

bool solve(string s1, string s2) {
    if (s1.size() != s2.size()) return false;
    unordered_map<char, int> freq;
    for (char c : s1) freq[c]++;
    for (char c : s2) freq[c]--;
    for (auto& [ch, cnt] : freq) {
        if (cnt != 0) return false;
    }
    return true;
}

// -- Do not change anything below this line --------------------------
int main() {
    string s1, s2;
    cin >> s1 >> s2;
    cout << (solve(s1, s2) ? "true" : "false") << endl;
    return 0;
}
