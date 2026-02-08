/*
 * Practice 1: Daily Temperatures
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * PROBLEM: Given daily temperatures, return days until a warmer temperature.
 * EXAMPLES: solve({73,74,75,71,69,72,76,73}) -> {1,1,4,2,1,1,0,0}
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

vector<int> solve(vector<int> temperatures) {
    // TODO: Replace this with your solution
    return vector<int>(temperatures.size(), 0);
}

int main() {
    int n;
    cin >> n;
    vector<int> temps(n);
    for (int i = 0; i < n; i++) cin >> temps[i];
    vector<int> result = solve(temps);
    for (int x : result) cout << x << " ";
    cout << endl;
    return 0;
}
