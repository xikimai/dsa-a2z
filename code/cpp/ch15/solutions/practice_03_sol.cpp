/* Solution: Practice 3 — Minimum Window Substring (Ch 15) */
#include <algorithm>
#include <climits>
#include <string>
#include <unordered_map>
using namespace std;
string solve(string s, string t) {
    if (s.empty() || t.empty()) return "";
    unordered_map<char, int> need;
    for (char c : t) need[c]++;
    int required = need.size();
    int formed = 0;
    unordered_map<char, int> window;
    int left = 0, bestLen = INT_MAX, bestStart = 0;

    for (int right = 0; right < (int)s.size(); right++) {
        char ch = s[right];
        window[ch]++;
        if (need.count(ch) && window[ch] == need[ch]) formed++;

        while (formed == required) {
            if (right - left + 1 < bestLen) {
                bestLen = right - left + 1;
                bestStart = left;
            }
            char out = s[left];
            window[out]--;
            if (need.count(out) && window[out] < need[out]) formed--;
            left++;
        }
    }
    return bestLen == INT_MAX ? "" : s.substr(bestStart, bestLen);
}
