/*
 * Solution -- Challenge 2: Count Inversions
 * ===========================================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * APPROACH: Modified merge sort. During the merge step, when we pick
 *           an element from the right half, all remaining elements in
 *           the left half form inversions with it.
 * TIME:  O(n log n)
 * SPACE: O(n)
 */

#include <iostream>
#include <vector>
using namespace std;

long long merge_count(vector<int>& arr, int left, int mid, int right) {
    vector<int> L(arr.begin() + left, arr.begin() + mid + 1);
    vector<int> R(arr.begin() + mid + 1, arr.begin() + right + 1);

    long long inversions = 0;
    int i = 0, j = 0, k = left;
    while (i < (int)L.size() && j < (int)R.size()) {
        if (L[i] <= R[j]) {
            arr[k++] = L[i++];
        } else {
            // All remaining elements in L are greater than R[j]
            inversions += (int)L.size() - i;
            arr[k++] = R[j++];
        }
    }
    while (i < (int)L.size()) arr[k++] = L[i++];
    while (j < (int)R.size()) arr[k++] = R[j++];
    return inversions;
}

long long merge_sort_count(vector<int>& arr, int left, int right) {
    if (left >= right) return 0;
    int mid = left + (right - left) / 2;
    long long count = 0;
    count += merge_sort_count(arr, left, mid);
    count += merge_sort_count(arr, mid + 1, right);
    count += merge_count(arr, left, mid, right);
    return count;
}

long long solve(vector<int> arr) {
    if (arr.size() <= 1) return 0LL;
    return merge_sort_count(arr, 0, (int)arr.size() - 1);
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << solve(arr) << endl;
    return 0;
}
