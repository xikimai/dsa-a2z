/* Solution: Practice 4 — Subarray Sum Equals K (Ch 15) */
#include <vector>
using namespace std;
int solve(vector<int> arr, int k) {
    int left = 0, currentSum = 0, count = 0;
    for (int right = 0; right < (int)arr.size(); right++) {
        currentSum += arr[right];
        while (currentSum > k && left <= right) {
            currentSum -= arr[left];
            left++;
        }
        if (currentSum == k) count++;
    }
    return count;
}
