/*
 * Challenge 1: Three Sum
 * Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method
 */
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> solve(vector<int> nums) {
    // TODO: Replace this with your solution
    return {};
}

int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    auto result = solve(nums);
    for (auto& t : result) {
        cout << t[0] << " " << t[1] << " " << t[2] << endl;
    }
    return 0;
}
