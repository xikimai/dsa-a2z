/*
 * Solution -- Challenge 2: Group Anagrams
 * ========================================
 * Chapter 5: Collections
 *
 * APPROACH:
 *   For each string, sort its characters to create a canonical key.
 *   All anagrams share the same sorted key. Group strings by their key
 *   using a map. Then sort each inner group and sort the outer groups
 *   by their first element.
 *
 * TIME COMPLEXITY:  O(n * k * log(k)) where n = number of strings, k = max string length
 * SPACE COMPLEXITY: O(n * k)
 */

#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

vector<vector<string>> solve(vector<string>& strs) {
    map<string, vector<string>> groups;
    for (const string& s : strs) {
        string key = s;
        sort(key.begin(), key.end());
        groups[key].push_back(s);
    }

    vector<vector<string>> result;
    for (auto& [key, group] : groups) {
        sort(group.begin(), group.end());
        result.push_back(group);
    }
    sort(result.begin(), result.end(), [](const vector<string>& a, const vector<string>& b) {
        return a[0] < b[0];
    });
    return result;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    cin.ignore();
    vector<string> strs(n);
    for (int i = 0; i < n; i++) getline(cin, strs[i]);
    vector<vector<string>> result = solve(strs);
    for (const auto& group : result) {
        for (int i = 0; i < (int)group.size(); i++) {
            if (i > 0) cout << " ";
            cout << group[i];
        }
        cout << endl;
    }
    return 0;
}
