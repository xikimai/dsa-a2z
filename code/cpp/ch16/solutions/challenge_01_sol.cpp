/* Solution: Challenge 1 — Aggressive Cows (Ch 16) */
#include <algorithm>
#include <vector>
using namespace std;
int solve(vector<int> stalls, int cows) {
    sort(stalls.begin(), stalls.end());
    int lo = 1, hi = stalls.back() - stalls[0];
    while (lo < hi) {
        int mid = lo + (hi - lo + 1) / 2;
        int count = 1, last = stalls[0];
        bool ok = false;
        for (int i = 1; i < (int)stalls.size(); i++) {
            if (stalls[i] - last >= mid) {
                count++;
                last = stalls[i];
                if (count >= cows) { ok = true; break; }
            }
        }
        if (ok) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}
