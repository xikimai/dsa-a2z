/*
 * Solution -- Practice 4: Recursive Binary Search
 * ==================================================
 * Chapter 10: The Magic of Recursion
 *
 * APPROACH: Helper with lo, hi parameters. Standard binary search logic
 *           but with recursive calls instead of a while loop.
 * TIME:  O(log n)
 * SPACE: O(log n) call stack
 */

#include <iostream>
#include <vector>
using namespace std;

int bs_helper(const vector<int>& arr, int target, int lo, int hi) {
    if (lo > hi) return -1;
    int mid = lo + (hi - lo) / 2;
    if (arr[mid] == target) return mid;
    if (arr[mid] < target) return bs_helper(arr, target, mid + 1, hi);
    return bs_helper(arr, target, lo, mid - 1);
}

int solve(vector<int> arr, int target) {
    return bs_helper(arr, target, 0, (int)arr.size() - 1);
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    int target;
    cin >> target;
    cout << solve(arr, target) << endl;
    return 0;
}
