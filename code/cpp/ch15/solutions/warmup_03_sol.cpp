/* Solution: Warmup 3 — Max Sum of Fixed Window (Ch 15) */
#include <algorithm>
#include <vector>
using namespace std;
int solve(vector<int> arr, int k) {
    if ((int)arr.size() < k) return 0;
    int windowSum = 0;
    for (int i = 0; i < k; i++) windowSum += arr[i];
    int best = windowSum;
    for (int i = k; i < (int)arr.size(); i++) {
        windowSum += arr[i] - arr[i - k];
        best = max(best, windowSum);
    }
    return best;
}
