/*
 * Practice 1: Equilibrium Index
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Find first index where left sum == right sum. Return -1 if none.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> arr) {
    // TODO: Replace this with your solution
    return -1;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << solve(arr) << endl;
    return 0;
}
