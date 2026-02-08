/* Solution: Practice 5 — Minimum Pages Allocation (Ch 16) */
#include <algorithm>
#include <numeric>
#include <vector>
using namespace std;
int solve(vector<int> pages, int students) {
    if (students > (int)pages.size()) return -1;
    int lo = *max_element(pages.begin(), pages.end());
    int hi = accumulate(pages.begin(), pages.end(), 0);
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        int count = 1, current = 0;
        for (int p : pages) {
            if (current + p > mid) { count++; current = 0; }
            current += p;
        }
        if (count <= students) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
