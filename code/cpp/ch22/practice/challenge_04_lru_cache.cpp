/*
 * Challenge 4: LRU Cache
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * PROBLEM: Implement LRU cache with get and put in O(1).
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <list>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

// operations: {op, key, value} where op is "get" or "put"
vector<int> solve(int capacity, vector<vector<string>> operations) {
    // TODO: Replace this with your solution
    return {};
}

int main() {
    int capacity = 2;
    vector<vector<string>> ops = {
        {"put","1","1"},{"put","2","2"},{"get","1"},
        {"put","3","3"},{"get","2"},
        {"put","4","4"},{"get","1"},{"get","3"},{"get","4"}
    };
    vector<int> result = solve(capacity, ops);
    for (int r : result) cout << r << " ";
    cout << endl;
    return 0;
}
