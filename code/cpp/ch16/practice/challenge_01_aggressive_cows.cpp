/*
 * Challenge 1: Aggressive Cows
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: Place c cows in stalls to maximize minimum distance between any two.
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int> stalls, int cows) {
    // TODO: Replace this with your solution
    return 0;
}

int main() {
    int n;
    cin >> n;
    vector<int> stalls(n);
    for (int i = 0; i < n; i++) cin >> stalls[i];
    int cows;
    cin >> cows;
    cout << solve(stalls, cows) << endl;
    return 0;
}
