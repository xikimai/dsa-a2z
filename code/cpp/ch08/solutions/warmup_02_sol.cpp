/*
 * Solution -- Warmup 2: Bubble Sort
 * ===================================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * APPROACH: Compare adjacent elements, swap if out of order.
 *           Use a "swapped" flag for early termination.
 * TIME:  O(n^2) worst, O(n) best (already sorted)
 * SPACE: O(1)
 */

#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> arr) {
    int n = (int)arr.size();
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
    return arr;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<int> result = solve(arr);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
