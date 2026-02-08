/*
 * Solution for Warmup 3: Implement Queue Using Array
 * Chapter 22: Stacks & Queues — Order Matters
 * APPROACH: Use deque for O(1) front/back operations.
 * TIME: O(1) per op, SPACE: O(n)
 */
#include <deque>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int> solve(vector<pair<string,int>> operations) {
    deque<int> q;
    vector<int> results;
    for (auto& [op, val] : operations) {
        if (op == "enqueue") {
            q.push_back(val);
        } else if (op == "dequeue") {
            if (q.empty()) { results.push_back(-1); }
            else { results.push_back(q.front()); q.pop_front(); }
        } else if (op == "front") {
            results.push_back(q.empty() ? -1 : q.front());
        } else if (op == "is_empty") {
            results.push_back(q.empty() ? 1 : 0);
        }
    }
    return results;
}

int main() {
    vector<pair<string,int>> ops = {{"enqueue",1},{"enqueue",2},{"front",0},{"dequeue",0},{"is_empty",0}};
    for (int r : solve(ops)) cout << r << " ";
    cout << endl;
    return 0;
}
