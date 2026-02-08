#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> nums) {
    if (nums.size() <= 1) return 0;
    int jumps = 0, currentEnd = 0, farthest = 0;
    for (int i = 0; i < (int)nums.size() - 1; i++) {
        farthest = max(farthest, i + nums[i]);
        if (i == currentEnd) {
            jumps++;
            currentEnd = farthest;
            if (currentEnd >= (int)nums.size() - 1) break;
        }
    }
    return jumps;
}

int main() {
    int n; cin >> n;
    vector<int> nums(n); for (int i = 0; i < n; i++) cin >> nums[i];
    cout << solve(nums) << endl;
    return 0;
}
