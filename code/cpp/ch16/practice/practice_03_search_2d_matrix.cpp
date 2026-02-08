/*
 * Practice 3: Search in 2D Matrix
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * PROBLEM: Find target in a fully sorted matrix. Return {row, col} or {-1, -1}.
 */

#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<vector<int>> matrix, int target) {
    // TODO: Replace this with your solution
    return {-1, -1};
}

int main() {
    int rows, cols;
    cin >> rows >> cols;
    vector<vector<int>> matrix(rows, vector<int>(cols));
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            cin >> matrix[i][j];
    int target;
    cin >> target;
    vector<int> result = solve(matrix, target);
    cout << result[0] << " " << result[1] << endl;
    return 0;
}
