/*
 * Solution for Warmup 2: Implement Stack Using Array
 * Chapter 22: Stacks & Queues — Order Matters
 * APPROACH: Use vector as backing store.
 * TIME: O(1) per op, SPACE: O(n)
 */
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int> solve(vector<pair<string,int>> operations) {
    vector<int> data;
    vector<int> results;
    for (auto& [op, val] : operations) {
        if (op == "push") {
            data.push_back(val);
        } else if (op == "pop") {
            if (data.empty()) { results.push_back(-1); }
            else { results.push_back(data.back()); data.pop_back(); }
        } else if (op == "top") {
            results.push_back(data.empty() ? -1 : data.back());
        } else if (op == "is_empty") {
            results.push_back(data.empty() ? 1 : 0);
        }
    }
    return results;
}

int main() {
    vector<pair<string,int>> ops = {{"push",1},{"push",2},{"top",0},{"pop",0},{"is_empty",0}};
    for (int r : solve(ops)) cout << r << " ";
    cout << endl;
    return 0;
}
