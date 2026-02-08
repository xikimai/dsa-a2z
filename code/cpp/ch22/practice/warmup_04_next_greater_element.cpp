/*
 * Warmup 4: Next Greater Element
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * PROBLEM: For each element, find the next greater element to its right (-1 if none).
 * EXAMPLES: solve({4,5,2,10,8}) -> {5,10,10,-1,-1}
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

vector<int> solve(vector<int> arr) {
    // TODO: Replace this with your solution
    return vector<int>(arr.size(), -1);
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];
    vector<int> result = solve(arr);
    for (int x : result) cout << x << " ";
    cout << endl;
    return 0;
}
