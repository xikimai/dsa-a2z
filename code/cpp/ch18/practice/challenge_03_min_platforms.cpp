/*
 * Challenge 3: Minimum Platforms
 * Chapter 18: Greedy Algorithms — The Smart Shortcut
 *
 * PROBLEM: Min platforms so no train waits.
 * EXAMPLES: solve({900,940,950,1100,1500,1800},{910,1200,1120,1130,1900,2000}) -> 3
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> arrivals, vector<int> departures) {
    // TODO: Replace this with your solution
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n; cin >> n;
    vector<int> arr(n), dep(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    for (int i = 0; i < n; i++) cin >> dep[i];
    cout << solve(arr, dep) << endl;
    return 0;
}
