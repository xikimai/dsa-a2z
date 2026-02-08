/* Solution: Challenge 3 — Longest Repeating Character Replacement (Ch 15) */
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;
int solve(string s, int k) {
    unordered_map<char, int> freq;
    int left = 0, maxFreq = 0, best = 0;
    for (int right = 0; right < (int)s.size(); right++) {
        freq[s[right]]++;
        maxFreq = max(maxFreq, freq[s[right]]);
        while ((right - left + 1) - maxFreq > k) {
            freq[s[left]]--;
            left++;
        }
        best = max(best, right - left + 1);
    }
    return best;
}
