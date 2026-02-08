/* Solution: Warmup 2 — First and Last Position (Ch 16) */
#include <vector>
using namespace std;
vector<int> solve(vector<int> arr, int target) {
    if (arr.empty()) return {-1, -1};
    int first = -1, last = -1;
    int lo = 0, hi = (int)arr.size() - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] == target) { first = mid; hi = mid - 1; }
        else if (arr[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    if (first == -1) return {-1, -1};
    lo = first; hi = (int)arr.size() - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] == target) { last = mid; lo = mid + 1; }
        else if (arr[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return {first, last};
}
