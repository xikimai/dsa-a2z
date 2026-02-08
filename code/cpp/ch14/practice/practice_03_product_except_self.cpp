/*
 * Practice 3: Product of Array Except Self
 * Chapter 14: Prefix Sums — The Running Total Trick
 *
 * PROBLEM: Return array where result[i] = product of all elements except arr[i].
 *          Do NOT use division.
 *
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */

#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

vector<long long> solve(vector<int> arr) {
    // TODO: Replace this with your solution
    return vector<long long>(arr.size(), 0);
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    auto result = solve(arr);
    for (int i = 0; i < (int)result.size(); i++)
        cout << result[i] << (i < (int)result.size()-1 ? " " : "\n");
    return 0;
}
