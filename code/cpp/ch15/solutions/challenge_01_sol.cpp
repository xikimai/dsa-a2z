/* Solution: Challenge 1 — Three Sum (Ch 15) */
#include <algorithm>
#include <vector>
using namespace std;
vector<vector<int>> solve(vector<int> nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    int n = nums.size();
    for (int i = 0; i < n - 2; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue;
        if (nums[i] > 0) break;
        int target = -nums[i];
        int left = i + 1, right = n - 1;
        while (left < right) {
            int twoSum = nums[left] + nums[right];
            if (twoSum == target) {
                result.push_back({nums[i], nums[left], nums[right]});
                while (left < right && nums[left] == nums[left + 1]) left++;
                while (left < right && nums[right] == nums[right - 1]) right--;
                left++; right--;
            } else if (twoSum < target) {
                left++;
            } else {
                right--;
            }
        }
    }
    return result;
}
