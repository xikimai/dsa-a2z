/*
 * Solution -- Warmup 5: Sort by Absolute Value
 * ==============================================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * APPROACH: Use sort() with a custom comparator comparing abs(a) < abs(b).
 * TIME:  O(n log n)
 * SPACE: O(1) extra (sort is in-place)
 */

#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> arr) {
    sort(arr.begin(), arr.end(), [](int a, int b) {
        return abs(a) < abs(b);
    });
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
