/*
 * Practice 5: Merge Two Sorted Arrays
 * =====================================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * PROBLEM:
 *   Given two sorted arrays, merge them into a single sorted array.
 *   Use the two-pointer technique -- do NOT just concatenate and sort.
 *
 * EXAMPLES:
 *   solve({1,3,5}, {2,4,6})     -> {1,2,3,4,5,6}
 *   solve({1,2,3}, {})          -> {1,2,3}
 *   solve({}, {4,5,6})          -> {4,5,6}
 *   solve({1,1,1}, {1,1,1})     -> {1,1,1,1,1,1}
 *   solve({1,5,9}, {2,3,7,10})  -> {1,2,3,5,7,9,10}
 *
 * CONSTRAINTS:
 *   0 <= arr1.size(), arr2.size() <= 10^5
 *   -10^6 <= arr1[i], arr2[i] <= 10^6
 *   Both arrays are sorted in non-decreasing order.
 *
 * INSTRUCTIONS:
 *   Replace the body with your solution.
 *   Use two pointers, one for each array.
 */

#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> arr1, vector<int> arr2) {
    // TODO: Replace this with your solution
    return {};
}

// -- Do not change anything below this line --------------------------
int main() {
    int n1, n2;
    cin >> n1;
    vector<int> arr1(n1);
    for (int i = 0; i < n1; i++) cin >> arr1[i];
    cin >> n2;
    vector<int> arr2(n2);
    for (int i = 0; i < n2; i++) cin >> arr2[i];
    vector<int> result = solve(arr1, arr2);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << " ";
        cout << result[i];
    }
    cout << endl;
    return 0;
}
