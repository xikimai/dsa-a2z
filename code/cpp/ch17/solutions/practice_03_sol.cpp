/*
 * Solution for Practice 3: Kth Smallest Element in a Sorted Matrix
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Use a min-heap. Push first element of each row (value, row, col).
 *           Pop k times, each time pushing next element from same row.
 *           The kth pop is the answer.
 * TIME:  O(k log n) where n = number of rows
 * SPACE: O(n) for the heap
 */

#include <iostream>
#include <queue>
#include <tuple>
#include <vector>
using namespace std;

int solve(vector<vector<int>> matrix, int k) {
    auto cmp = [](const tuple<int,int,int>& a, const tuple<int,int,int>& b) {
        return get<0>(a) > get<0>(b);  // min-heap
    };
    priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, decltype(cmp)> pq(cmp);

    int n = matrix.size();
    for (int r = 0; r < n; r++) {
        pq.push({matrix[r][0], r, 0});
    }

    int val = 0;
    for (int i = 0; i < k; i++) {
        auto [v, r, c] = pq.top();
        pq.pop();
        val = v;
        if (c + 1 < (int)matrix[r].size()) {
            pq.push({matrix[r][c + 1], r, c + 1});
        }
    }
    return val;
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
