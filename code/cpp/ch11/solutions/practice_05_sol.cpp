/*
 * Solution for Practice 5: Sort Characters by Frequency
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: Count character frequencies, sort characters by frequency
 *           descending (tiebreak alphabetically ascending), then build
 *           the result string.
 * TIME:  O(n + k log k) where k = unique characters
 * SPACE: O(n)
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
    for (char c : s) freq[c]++;

    // Collect unique characters with their frequencies
    vector<pair<char, int>> chars;
    for (auto& [ch, cnt] : freq) {
        chars.push_back({ch, cnt});
    }

    // Sort by frequency desc, then alphabetically asc
    sort(chars.begin(), chars.end(), [](const pair<char,int>& a, const pair<char,int>& b) {
        if (a.second != b.second) return a.second > b.second;
        return a.first < b.first;
    });

    string result;
    for (auto& [ch, cnt] : chars) {
        result += string(cnt, ch);
    }
    return result;
}

// -- Do not change anything below this line --------------------------
int main() {
    string s;
    getline(cin, s);
    cout << solve(s) << endl;
    return 0;
}
