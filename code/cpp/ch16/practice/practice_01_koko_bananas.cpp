/*
 * Practice 1: Koko Eating Bananas
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: Min eating speed to finish all piles within h hours.
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> piles, int h) {
    // TODO: Replace this with your solution
    return 0;
}

int main() {
    int n;
    cin >> n;
    vector<int> piles(n);
    for (int i = 0; i < n; i++) cin >> piles[i];
    int h;
    cin >> h;
    cout << solve(piles, h) << endl;
    return 0;
}
