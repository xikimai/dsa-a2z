/*
 * Solution for Practice 1: Group Anagrams
 * Chapter 11: Hashing — The Secret Decoder Ring
 *
 * APPROACH: For each word, sort its characters to form a key.
 *           Group words by their sorted key using an unordered_map.
 *           Sort each group and sort the outer list by first element.
 * TIME:  O(n * k log k) where k = max word length
 * SPACE: O(n * k)
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

vector<vector<string>> solve(vector<string> strs) {
    unordered_map<string, vector<string>> groups;
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
    sort(result.begin(), result.end());
    return result;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<string> strs(n);
    for (int i = 0; i < n; i++) cin >> strs[i];
    vector<vector<string>> result = solve(strs);
    for (auto& group : result) {
        for (int i = 0; i < (int)group.size(); i++) {
            if (i > 0) cout << ",";
            cout << group[i];
        }
        cout << endl;
    }
    return 0;
}
