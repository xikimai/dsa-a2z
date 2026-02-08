/*
 * Warmup 4: Is Array Prefix of Another
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Return true if arr1 is a prefix of arr2.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

bool solve(vector<int> arr1, vector<int> arr2) {
    // TODO: Replace this with your solution
    return false;
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
    cout << (solve(arr1, arr2) ? "true" : "false") << endl;
    return 0;
}
