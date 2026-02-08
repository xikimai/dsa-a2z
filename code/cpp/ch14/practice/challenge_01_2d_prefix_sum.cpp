/*
 * Challenge 1: 2D Prefix Sum and Range Query
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Build 2D prefix sum, answer rectangle queries [r1,c1,r2,c2].
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

vector<long long> solve(vector<vector<int>> matrix, vector<vector<int>> queries) {
    // TODO: Replace this with your solution
    return vector<long long>(queries.size(), 0);
}

// -- Do not change anything below this line --------------------------
int main() {
    int rows, cols;
    cin >> rows >> cols;
    vector<vector<int>> matrix(rows, vector<int>(cols));
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            cin >> matrix[i][j];
    int q;
    cin >> q;
    vector<vector<int>> queries(q, vector<int>(4));
    for (int i = 0; i < q; i++)
        cin >> queries[i][0] >> queries[i][1] >> queries[i][2] >> queries[i][3];
    auto result = solve(matrix, queries);
    for (int i = 0; i < (int)result.size(); i++)
        cout << result[i] << (i < (int)result.size()-1 ? " " : "\n");
    return 0;
}
