/*
 * Warmup 1: Pair Sum in Sorted Array
 * Chapter 15: Two Pointers & Sliding Window — The Caterpillar Method
 *
 * PROBLEM: Given a sorted array and target, find pair summing to target.
 *          Return {a, b} with a <= b. Return {-1, -1} if none.
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> arr, int target) {
    // TODO: Replace this with your solution
    return {-1, -1};
}

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    int target;
    cin >> target;
    vector<int> result = solve(arr, target);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}
