/*
 * Solution -- Challenge 1: Sort Three Ways
 * ==========================================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * Three sorting implementations:
 *   1. solve_bubble -- Bubble sort. O(n^2) worst, O(n) best.
 *   2. solve_merge  -- Merge sort. O(n log n) always.
 *   3. solve_builtin -- std::sort. O(n log n) average.
 *
 * TIME:  See above per method
 * SPACE: O(1) for bubble, O(n) for merge, O(log n) for builtin
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<int> solve_bubble(vector<int> arr) {
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

void merge_helper(vector<int>& arr, int left, int mid, int right) {
    vector<int> L(arr.begin() + left, arr.begin() + mid + 1);
    vector<int> R(arr.begin() + mid + 1, arr.begin() + right + 1);

    int i = 0, j = 0, k = left;
    while (i < (int)L.size() && j < (int)R.size()) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }
    while (i < (int)L.size()) arr[k++] = L[i++];
    while (j < (int)R.size()) arr[k++] = R[j++];
}

void merge_sort_helper(vector<int>& arr, int left, int right) {
    if (left >= right) return;
    int mid = left + (right - left) / 2;
    merge_sort_helper(arr, left, mid);
    merge_sort_helper(arr, mid + 1, right);
    merge_helper(arr, left, mid, right);
}

vector<int> solve_merge(vector<int> arr) {
    if (arr.empty()) return arr;
    merge_sort_helper(arr, 0, (int)arr.size() - 1);
    return arr;
}

vector<int> solve_builtin(vector<int> arr) {
    sort(arr.begin(), arr.end());
    return arr;
}

vector<int> solve(vector<int> arr) {
    return solve_merge(arr);
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    vector<int> r1 = solve_bubble(arr);
    vector<int> r2 = solve_merge(arr);
    vector<int> r3 = solve_builtin(arr);

    cout << "bubble:  ";
    for (int i = 0; i < (int)r1.size(); i++) { if (i > 0) cout << " "; cout << r1[i]; }
    cout << endl;

    cout << "merge:   ";
    for (int i = 0; i < (int)r2.size(); i++) { if (i > 0) cout << " "; cout << r2[i]; }
    cout << endl;

    cout << "builtin: ";
    for (int i = 0; i < (int)r3.size(); i++) { if (i > 0) cout << " "; cout << r3[i]; }
    cout << endl;
    return 0;
}
