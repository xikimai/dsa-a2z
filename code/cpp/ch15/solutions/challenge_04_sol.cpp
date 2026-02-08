/* Solution: Challenge 4 — Fruit Into Baskets (Ch 15) */
#include <algorithm>
#include <unordered_map>
#include <vector>
using namespace std;
int solve(vector<int> fruits) {
    unordered_map<int, int> freq;
    int left = 0, best = 0;
    for (int right = 0; right < (int)fruits.size(); right++) {
        freq[fruits[right]]++;
        while ((int)freq.size() > 2) {
            int lf = fruits[left];
            freq[lf]--;
            if (freq[lf] == 0) freq.erase(lf);
            left++;
        }
        best = max(best, right - left + 1);
    }
    return best;
}
