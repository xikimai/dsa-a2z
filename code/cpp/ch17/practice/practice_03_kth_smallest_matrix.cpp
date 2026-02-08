/*
 * Practice 3: Kth Smallest Element in a Sorted Matrix
 * =====================================================
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * PROBLEM:
 *   Given an n x n matrix where each row and column is sorted in
 *   ascending order, return the kth smallest element.
 *
 * EXAMPLES:
 *   solve({{1,5,9},{10,11,13},{12,13,15}}, 8)  -> 13
 *   solve({{-5}}, 1)                            -> -5
 *
 * CONSTRAINTS:
 *   - 1 <= n <= 300
 *   - 1 <= k <= n^2
 *   - matrix[i][j] can be any integer
 *
 * INSTRUCTIONS:
 *   Replace the body of solve() with your solution.
 */

#include <iostream>
#include <queue>
#include <tuple>
#include <vector>
using namespace std;

int solve(vector<vector<int>> matrix, int k) {
    // TODO: Replace this with your solution
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n, k;
    cin >> n;
    vector<vector<int>> matrix(n, vector<int>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> matrix[i][j];
    cin >> k;
    cout << solve(matrix, k) << endl;
    return 0;
}
