/*
 * Example 02: Sliding Window Patterns
 * =====================================
 * Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method
 *
 * Demonstrates fixed-size and variable-size sliding windows.
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

int main() {
    // Part 1: Fixed-size window — max sum of k elements
    cout << "=== Part 1: Fixed-Size Window ===" << endl;
    vector<int> arr = {2, 1, 5, 1, 3, 2, 8, 1};
    int k = 3;

    int windowSum = 0;
    for (int i = 0; i < k; i++) windowSum += arr[i];
    int best = windowSum;

    for (int i = k; i < (int)arr.size(); i++) {
        windowSum += arr[i] - arr[i - k];
        best = max(best, windowSum);
        cout << "  Window [" << i - k + 1 << ".." << i << "] sum=" << windowSum
             << (windowSum == best ? " <- best" : "") << endl;
    }
    cout << "Best sum: " << best << endl;

    // Part 2: Variable window — longest substring without repeats
    cout << "\n=== Part 2: Variable Window + HashMap ===" << endl;
    string s = "abcabcbb";
    cout << "String: \"" << s << "\"" << endl;

    unordered_map<char, int> charIndex;
    int left = 0, bestLen = 0;

    for (int right = 0; right < (int)s.size(); right++) {
        char ch = s[right];
        if (charIndex.count(ch) && charIndex[ch] >= left) {
            left = charIndex[ch] + 1;
        }
        charIndex[ch] = right;
        bestLen = max(bestLen, right - left + 1);
        cout << "  right=" << right << " '" << ch
             << "' window=\"" << s.substr(left, right - left + 1)
             << "\" len=" << right - left + 1 << endl;
    }
    cout << "Longest substring without repeating: " << bestLen << endl;

    return 0;
}
