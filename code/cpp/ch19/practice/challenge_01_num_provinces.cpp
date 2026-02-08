/*
 * Challenge 1: Number of Provinces
 * Chapter 19: Graphs I — Exploring Networks
 *
 * PROBLEM: Given an adjacency matrix, count provinces (connected components).
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int solve(vector<vector<int>>& isConnected) {
    // TODO: Replace this with your solution
    return 0;
}

int main() {
    int n; cin >> n;
    vector<vector<int>> isConnected(n, vector<int>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) cin >> isConnected[i][j];
    cout << solve(isConnected) << endl;
    return 0;
}
