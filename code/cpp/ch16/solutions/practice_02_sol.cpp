/* Solution: Practice 2 — Ship Packages Within D Days (Ch 16) */
#include <algorithm>
#include <numeric>
#include <vector>
using namespace std;
int solve(vector<int> weights, int d) {
    int lo = *max_element(weights.begin(), weights.end());
    int hi = accumulate(weights.begin(), weights.end(), 0);
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        int days = 1, load = 0;
        for (int w : weights) {
            if (load + w > mid) { days++; load = 0; }
            load += w;
        }
        if (days <= d) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
