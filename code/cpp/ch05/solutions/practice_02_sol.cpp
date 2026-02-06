/*
 * Solution -- Practice 2: Anagram Check
 * =======================================
 * Chapter 5: Collections
 *
 * APPROACH:
 *   Convert both strings to lowercase, then compare character frequency
 *   arrays. If lengths differ, immediately return false. Use a fixed
 *   array of size 26 for counting (only lowercase letters after conversion).
 *
 * TIME COMPLEXITY:  O(n) where n = length of the strings
 * SPACE COMPLEXITY: O(1) — fixed 26-element array
 */

#include <iostream>
#include <string>
using namespace std;

bool solve(string s1, string s2) {
    if (s1.size() != s2.size()) return false;

    int freq[26] = {};
    for (int i = 0; i < (int)s1.size(); i++) {
        freq[tolower(s1[i]) - 'a']++;
        freq[tolower(s2[i]) - 'a']--;
    }
    for (int i = 0; i < 26; i++) {
        if (freq[i] != 0) return false;
    }
    return true;
}

// -- Do not change anything below this line --------------------------
int main() {
    string s1, s2;
    getline(cin, s1);
    getline(cin, s2);
    cout << (solve(s1, s2) ? "true" : "false") << endl;
    return 0;
}
