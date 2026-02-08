/*
 * Practice 4: Row with Maximum 1s
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: Binary matrix (rows sorted: 0s then 1s). Return row with max 1s, or -1.
 */

#include <iostream>
#include <vector>
using namespace std;

int solve(vector<vector<int>> matrix) {
    // TODO: Replace this with your solution
    return -1;
}

int main() {
    int rows, cols;
    cin >> rows >> cols;
    vector<vector<int>> matrix(rows, vector<int>(cols));
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            cin >> matrix[i][j];
    cout << solve(matrix) << endl;
    return 0;
}
