/*
 * Challenge 2: Count Inversions
 * ===============================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * PROBLEM:
 *   An inversion is a pair (i, j) where i < j but arr[i] > arr[j].
 *   Count the total number of inversions in the array.
 *
 *   A sorted array has 0 inversions.
 *   A reverse-sorted array of size n has n*(n-1)/2 inversions (the max).
 *
 * EXAMPLES:
 *   solve({2,4,1,3,5}) -> 3   (pairs: (2,1), (4,1), (4,3))
 *   solve({1,2,3,4,5}) -> 0
 *   solve({5,4,3,2,1}) -> 10
 *   solve({1})         -> 0
 *   solve({})          -> 0
 *
 * CONSTRAINTS:
 *   0 <= arr.size() <= 10^5
 *   -10^6 <= arr[i] <= 10^6
 *
 * INSTRUCTIONS:
 *   Replace "return 0LL;" with your solution.
 *   Hint: Modify merge sort to count inversions during the merge step.
 *   Use long long -- the count can be very large!
 */

#include <iostream>
#include <vector>
using namespace std;

long long solve(vector<int> arr) {
    // TODO: Replace this with your solution
    return 0LL;
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
