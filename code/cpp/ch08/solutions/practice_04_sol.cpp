/*
 * Solution -- Practice 4: Custom Comparator Sort
 * ================================================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * APPROACH: sort() with a lambda that compares by length first,
 *           then alphabetically for same-length words.
 * TIME:  O(n log n * k) where k is average word length
 * SPACE: O(1) extra (sort is in-place)
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<string> solve(vector<string> words) {
    sort(words.begin(), words.end(), [](const string& a, const string& b) {
        if (a.size() != b.size()) return a.size() < b.size();
        return a < b;
    });
    return words;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<string> words(n);
    for (int i = 0; i < n; i++) cin >> words[i];
    vector<string> result = solve(words);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
