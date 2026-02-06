/*
 * Solution -- Warmup 5: Character Frequency
 * ===========================================
 * Chapter 5: Collections
 *
 * APPROACH:
 *   Use an unordered_map to count character frequencies.
 *   The m[k]++ pattern auto-creates keys with value 0 then increments.
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(k) where k = number of unique characters
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

unordered_map<char, int> solve(string s) {
    unordered_map<char, int> freq;
    for (char c : s) {
        freq[c]++;
    }
    return freq;
}

// -- Do not change anything below this line --------------------------
int main() {
    string s;
    getline(cin, s);
    unordered_map<char, int> result = solve(s);
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
