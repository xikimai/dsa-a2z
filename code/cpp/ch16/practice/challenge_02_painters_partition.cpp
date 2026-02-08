/*
 * Challenge 2: Painter's Partition
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: k painters paint contiguous boards. Minimize max section length.
 */

#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

int solve(vector<int> boards, int k) {
    // TODO: Replace this with your solution
    return 0;
}

int main() {
    int n;
    cin >> n;
    vector<int> boards(n);
    for (int i = 0; i < n; i++) cin >> boards[i];
    int k;
    cin >> k;
    cout << solve(boards, k) << endl;
    return 0;
}
