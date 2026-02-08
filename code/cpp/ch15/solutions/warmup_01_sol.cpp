/* Solution: Warmup 1 — Pair Sum in Sorted Array (Ch 15) */
#include <vector>
using namespace std;
vector<int> solve(vector<int> arr, int target) {
    int left = 0, right = (int)arr.size() - 1;
    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == target) return {arr[left], arr[right]};
        else if (sum < target) left++;
        else right--;
    }
    return {-1, -1};
}
