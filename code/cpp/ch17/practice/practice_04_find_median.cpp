/*
 * Practice 4: Find Median from Data Stream
 * ===========================================
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * PROBLEM:
 *   Given a stream of integers (as an array), return a list of medians
 *   after adding each number. Use the two-heap technique.
 *
 * EXAMPLES:
 *   solve({5,15,1,3})  -> {5.0, 10.0, 5.0, 4.0}
 *   solve({2,3,4})     -> {2.0, 2.5, 3.0}
 *
 * CONSTRAINTS:
 *   - 1 <= nums.size() <= 10^5
 *   - -10^5 <= nums[i] <= 10^5
 *
 * INSTRUCTIONS:
 *   Replace the body of solve() with your solution.
 */

#include <functional>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<double> solve(vector<int> nums) {
    // TODO: Replace this with your solution
    return {};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) cin >> nums[i];
    vector<double> result = solve(nums);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
