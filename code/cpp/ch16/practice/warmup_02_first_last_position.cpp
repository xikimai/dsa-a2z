/*
 * Warmup 2: First and Last Position
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: Given sorted array and target, return {first, last} indices.
 *          Return {-1, -1} if not found.
 */

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
