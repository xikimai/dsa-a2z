/*
 * Practice 4: Custom Comparator Sort
 * ====================================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * PROBLEM:
 *   Sort a list of words first by length (shorter first),
 *   then alphabetically for words of the same length.
 *
 * EXAMPLES:
 *   solve({"banana","apple","kiwi","cherry","fig"})
 *       -> {"fig","kiwi","apple","banana","cherry"}
 *   solve({"cat","bat","ant"})
 *       -> {"ant","bat","cat"}
 *   solve({"a","bb","ccc","dd","e"})
 *       -> {"a","e","bb","dd","ccc"}
 *
 * CONSTRAINTS:
 *   0 <= words.size() <= 10^4
 *   1 <= words[i].length() <= 100
 *
 * INSTRUCTIONS:
 *   Replace the body with your solution.
 *   Use sort() with a lambda comparator.
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<string> solve(vector<string> words) {
    // TODO: Replace this with your solution
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
