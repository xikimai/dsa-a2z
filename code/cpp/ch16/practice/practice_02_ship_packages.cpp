/*
 * Practice 2: Ship Packages Within D Days
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: Min ship capacity to deliver all packages in d days.
 */

#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

int solve(vector<int> weights, int d) {
    // TODO: Replace this with your solution
    return 0;
}

int main() {
    int n;
    cin >> n;
    vector<int> weights(n);
    for (int i = 0; i < n; i++) cin >> weights[i];
    int d;
    cin >> d;
    cout << solve(weights, d) << endl;
    return 0;
}
