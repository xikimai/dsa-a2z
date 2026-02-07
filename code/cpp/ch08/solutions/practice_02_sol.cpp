/*
 * Solution -- Practice 2: Quick Sort
 * ====================================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * APPROACH: Lomuto partition scheme. Pick last element as pivot,
 *           partition so all elements <= pivot are on the left.
 * TIME:  O(n log n) average, O(n^2) worst
 * SPACE: O(log n) average (recursion stack)
 */

#include <iostream>
#include <vector>
using namespace std;

int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quick_sort(vector<int>& arr, int low, int high) {
    if (low >= high) return;
    int pi = partition(arr, low, high);
    quick_sort(arr, low, pi - 1);
    quick_sort(arr, pi + 1, high);
}

vector<int> solve(vector<int> arr) {
    if (arr.empty()) return arr;
    quick_sort(arr, 0, (int)arr.size() - 1);
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
