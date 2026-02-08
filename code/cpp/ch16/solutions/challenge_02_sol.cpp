/* Solution: Challenge 2 — Painter's Partition (Ch 16) */
#include <algorithm>
#include <numeric>
#include <vector>
using namespace std;
int solve(vector<int> boards, int k) {
    int lo = *max_element(boards.begin(), boards.end());
    int hi = accumulate(boards.begin(), boards.end(), 0);
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        int painters = 1, current = 0;
        for (int b : boards) {
            if (current + b > mid) { painters++; current = 0; }
            current += b;
        }
        if (painters <= k) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
