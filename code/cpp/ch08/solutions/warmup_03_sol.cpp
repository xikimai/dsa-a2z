/*
 * Solution -- Warmup 3: Insertion Sort
 * ======================================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * APPROACH: Take each element and insert it in its correct position
 *           among the already-sorted elements to its left.
 * TIME:  O(n^2) worst, O(n) best (already sorted)
 * SPACE: O(1)
 */

#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> arr) {
    int n = (int)arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
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
