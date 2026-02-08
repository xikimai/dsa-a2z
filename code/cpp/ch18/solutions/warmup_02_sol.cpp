#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

bool solve(vector<int> nums) {
    int maxReach = 0;
    for (int i = 0; i < (int)nums.size(); i++) {
        if (i > maxReach) return false;
        maxReach = max(maxReach, i + nums[i]);
    }
    return true;
}

int main() {
    int n; cin >> n;
    vector<int> nums(n); for (int i = 0; i < n; i++) cin >> nums[i];
    cout << (solve(nums) ? "true" : "false") << endl;
    return 0;
}
