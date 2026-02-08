/* Solution: Practice 2 — Longest Substring Without Repeating (Ch 15) */
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;
int solve(string s) {
    unordered_map<char, int> charIndex;
    int left = 0, best = 0;
    for (int right = 0; right < (int)s.size(); right++) {
        char ch = s[right];
        if (charIndex.count(ch) && charIndex[ch] >= left) {
            left = charIndex[ch] + 1;
        }
        charIndex[ch] = right;
        best = max(best, right - left + 1);
    }
    return best;
}
