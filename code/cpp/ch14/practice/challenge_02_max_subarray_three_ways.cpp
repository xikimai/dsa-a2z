/*
 * Challenge 2: Maximum Subarray Sum Three Ways (AOPS)
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Find max subarray sum using brute O(n^3), prefix O(n^2), Kadane's O(n).
 *
 * INSTRUCTIONS: Replace the body of each solve function with your solution.
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

long long solve_brute(vector<int> arr) {
    // TODO: O(n^3) brute force
    return 0;
}

long long solve_prefix(vector<int> arr) {
    // TODO: O(n^2) prefix sum
    return 0;
}

long long solve_kadane(vector<int> arr) {
    // TODO: O(n) Kadane's
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << "brute=" << solve_brute(arr) << " prefix=" << solve_prefix(arr)
         << " kadane=" << solve_kadane(arr) << endl;
    return 0;
}
