/*
 * Practice 4: Queue Using Two Stacks
 * Chapter 22: Stacks & Queues — Order Matters
 *
 * PROBLEM: Implement a queue using only two stacks.
 * INSTRUCTIONS: Replace the body of solve() with your solution.
 */
#include <iostream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

vector<int> solve(vector<pair<string,int>> operations) {
    // TODO: Replace this with your solution
    return {};
}

int main() {
    vector<pair<string,int>> ops = {{"enqueue",1},{"enqueue",2},{"peek",0},{"dequeue",0},{"empty",0}};
    vector<int> result = solve(ops);
    for (int r : result) cout << r << " ";
    cout << endl;
    return 0;
}
