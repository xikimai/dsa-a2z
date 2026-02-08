/*
 * Solution for Warmup 4: Check if Array is a Min-Heap
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Check every parent node against its children.
 *           Parent at index i must be <= left child (2i+1) and right child (2i+2).
 * TIME:  O(n)
 * SPACE: O(1)
 */

#include <iostream>
#include <vector>
using namespace std;

bool solve(vector<int> arr) {
    int n = arr.size();
    for (int i = 0; i < n / 2; i++) {
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        if (left < n && arr[i] > arr[left]) return false;
        if (right < n && arr[i] > arr[right]) return false;
    }
    return true;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    cout << (solve(arr) ? "true" : "false") << endl;
    return 0;
}
