/*
 * Warmup 3: Max Sum of Fixed Window
 * Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method
 *
 * PROBLEM: Find the max sum of k consecutive elements. Return 0 if len < k.
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> arr, int k) {
    // TODO: Replace this with your solution
    return 0;
}

int main() {
    int n, k;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    cin >> k;
    cout << solve(arr, k) << endl;
    return 0;
}
