/*
 * Warmup 5: Character Frequency
 * ==============================
 * Chapter 5: Collections
 *
 * PROBLEM:
 *   Given a string, return an unordered_map of character frequencies.
 *
 * EXAMPLES:
 *   solve("aab") -> {{'a', 2}, {'b', 1}}
 *   solve("")    -> {}
 *
 * CONSTRAINTS:
 *   - 0 <= s.length() <= 10^5
 *
 * OUTPUT FORMAT:
 *   Print each char:count pair on the same line, sorted by character,
 *   separated by spaces. Example: "a:2 b:1"
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

/**
 * Returns a map of character frequencies.
 */
unordered_map<char, int> solve(string s) {
    // TODO: Replace this with your solution
    return {};
}

// -- Do not change anything below this line --------------------------
int main() {
    string s;
    getline(cin, s);
    unordered_map<char, int> result = solve(s);
    // Sort keys for consistent output
    vector<char> keys;
    for (const auto& [ch, cnt] : result) keys.push_back(ch);
    sort(keys.begin(), keys.end());
    for (int i = 0; i < (int)keys.size(); i++) {
        if (i > 0) cout << " ";
        cout << keys[i] << ":" << result[keys[i]];
    }
    cout << endl;
    return 0;
}
