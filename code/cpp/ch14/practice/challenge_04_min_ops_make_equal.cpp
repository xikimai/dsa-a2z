/*
 * Challenge 4: Minimum Operations to Make All Elements Equal
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Given a sorted array, find min operations to make all equal.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

long long solve(vector<int> arr) {
    // TODO: Replace this with your solution
    return 0;
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
