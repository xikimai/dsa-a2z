/*
 * Solution -- Practice 5: Merge Two Sorted Arrays
 * =================================================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * APPROACH: Two-pointer merge. Walk through both arrays
 *           simultaneously, always picking the smaller element.
 * TIME:  O(n + m) where n, m are array sizes
 * SPACE: O(n + m) for the result
 */

#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(vector<int> arr1, vector<int> arr2) {
    vector<int> result;
    int i = 0, j = 0;
    while (i < (int)arr1.size() && j < (int)arr2.size()) {
        if (arr1[i] <= arr2[j]) result.push_back(arr1[i++]);
        else result.push_back(arr2[j++]);
    }
    while (i < (int)arr1.size()) result.push_back(arr1[i++]);
    while (j < (int)arr2.size()) result.push_back(arr2[j++]);
    return result;
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
