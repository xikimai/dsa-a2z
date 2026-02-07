/*
 * Challenge 3: Sort by Frequency
 * ================================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * PROBLEM:
 *   Sort the array by frequency (most frequent first).
 *   If two elements have the same frequency, the smaller element
 *   comes first.
 *
 * EXAMPLES:
 *   solve({1,1,2,2,2,3})   -> {2,2,2,1,1,3}
 *   solve({4,4,4,5,5,6})   -> {4,4,4,5,5,6}
 *   solve({1,2,3})         -> {1,2,3}
 *   solve({5})             -> {5}
 *   solve({3,3,1,1,2,2})   -> {1,1,2,2,3,3}
 *
 * CONSTRAINTS:
 *   0 <= arr.size() <= 10^5
 *   -10^6 <= arr[i] <= 10^6
 *
 * INSTRUCTIONS:
 *   Replace the body with your solution.
 *   Hint: Count frequencies with a map, then sort with a custom comparator.
 */

#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

vector<int> solve(vector<int> arr) {
    // TODO: Replace this with your solution
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
