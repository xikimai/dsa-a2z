/*
 * Solution for Practice 2: Merge K Sorted Arrays
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Use a min-heap of (value, array_index, element_index). Pop the
 *           minimum, append to result, push the next element from same array.
 * TIME:  O(N log K) where N = total elements, K = number of arrays
 * SPACE: O(K) for the heap + O(N) for the result
 */

#include <algorithm>
#include <iostream>
#include <queue>
#include <tuple>
#include <vector>
using namespace std;

vector<int> solve(vector<vector<int>> arrays) {
    auto cmp = [](const tuple<int,int,int>& a, const tuple<int,int,int>& b) {
        return get<0>(a) > get<0>(b);  // min-heap by value
    };
    priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, decltype(cmp)> pq(cmp);

    for (int i = 0; i < (int)arrays.size(); i++) {
        if (!arrays[i].empty()) {
            pq.push({arrays[i][0], i, 0});
        }
    }

    vector<int> result;
    while (!pq.empty()) {
        auto [val, ai, ei] = pq.top();
        pq.pop();
        result.push_back(val);
        if (ei + 1 < (int)arrays[ai].size()) {
            pq.push({arrays[ai][ei + 1], ai, ei + 1});
        }
    }
    return result;
}

// -- Do not change anything below this line --------------------------
int main() {
    int k;
    cin >> k;
    vector<vector<int>> arrays(k);
    for (int i = 0; i < k; i++) {
        int n;
        cin >> n;
        arrays[i].resize(n);
        for (int j = 0; j < n; j++) cin >> arrays[i][j];
    }
    vector<int> result = solve(arrays);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
