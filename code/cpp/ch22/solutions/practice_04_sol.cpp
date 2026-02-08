/*
 * Solution for Practice 4: Queue Using Two Stacks
 * Chapter 22: Stacks & Queues — Order Matters
 * APPROACH: In-stack and out-stack. Transfer when out is empty.
 * TIME: O(1) amortized per op, SPACE: O(n)
 */
#include <iostream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

vector<int> solve(vector<pair<string,int>> operations) {
    stack<int> in, out;
    vector<int> results;

    auto transfer = [&]() {
        while (!in.empty()) { out.push(in.top()); in.pop(); }
    };

    for (auto& [op, val] : operations) {
        if (op == "enqueue") {
            in.push(val);
        } else if (op == "dequeue") {
            if (out.empty()) transfer();
            results.push_back(out.top()); out.pop();
        } else if (op == "peek") {
            if (out.empty()) transfer();
            results.push_back(out.top());
        } else if (op == "empty") {
            results.push_back(in.empty() && out.empty() ? 1 : 0);
        }
    }
    return results;
}

int main() {
    vector<pair<string,int>> ops = {{"enqueue",1},{"enqueue",2},{"peek",0},{"dequeue",0},{"empty",0}};
    for (int r : solve(ops)) cout << r << " ";
    cout << endl;
    return 0;
}
