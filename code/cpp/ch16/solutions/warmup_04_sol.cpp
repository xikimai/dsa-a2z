/* Solution: Warmup 4 — Peak Element (Ch 16) */
#include <vector>
using namespace std;
int solve(vector<int> arr) {
    if (arr.empty()) return -1;
    if (arr.size() == 1) return 0;
    int lo = 0, hi = (int)arr.size() - 1;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] < arr[mid + 1]) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}
