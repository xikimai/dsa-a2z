/* Solution: Practice 1 — Container With Most Water (Ch 15) */
#include <algorithm>
#include <vector>
using namespace std;
int solve(vector<int> heights) {
    int left = 0, right = (int)heights.size() - 1;
    int best = 0;
    while (left < right) {
        int w = right - left;
        int h = min(heights[left], heights[right]);
        best = max(best, w * h);
        if (heights[left] < heights[right]) left++;
        else right--;
    }
    return best;
}
