/*
 * Challenge 3: Online Stock Span
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * PROBLEM: For each day's price, return consecutive days with price <= today.
 * EXAMPLES: solve({100,80,60,70,60,75,85}) -> {1,1,1,2,1,4,6}
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

vector<int> solve(vector<int> prices) {
    // TODO: Replace this with your solution
    return vector<int>(prices.size(), 1);
}

int main() {
    int n;
    cin >> n;
    vector<int> prices(n);
    for (int i = 0; i < n; i++) cin >> prices[i];
    vector<int> result = solve(prices);
    for (int x : result) cout << x << " ";
    cout << endl;
    return 0;
}
