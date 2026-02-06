/*
 * Solution -- Warmup 3: Count Vowels
 * ====================================
 * Chapter 5: Collections
 *
 * APPROACH:
 *   Use an unordered_set of vowel characters for O(1) lookup.
 *   Convert each character to lowercase before checking.
 *
 * TIME COMPLEXITY:  O(n)
 * SPACE COMPLEXITY: O(1) — the vowel set is constant size
 */

#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

int solve(string s) {
    unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
    int count = 0;
    for (char c : s) {
        if (vowels.count(tolower(c))) {
            count++;
        }
    }
    return count;
}

// -- Do not change anything below this line --------------------------
int main() {
    string s;
    getline(cin, s);
    cout << solve(s) << endl;
    return 0;
}
