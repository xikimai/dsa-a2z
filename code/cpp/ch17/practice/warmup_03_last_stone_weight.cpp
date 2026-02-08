/*
 * Warmup 3: Last Stone Weight
 * =============================
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * PROBLEM:
 *   You have a collection of stones, each with a positive weight.
 *   Each turn, pick the 2 heaviest stones and smash them together.
 *   If they are equal, both are destroyed. Otherwise, the lighter
 *   stone is destroyed and the heavier stone loses weight equal to
 *   the lighter one. Return the weight of the last remaining stone,
 *   or 0 if none remain.
 *
 * EXAMPLES:
 *   solve({2,7,4,1,8,1})  -> 1
 *   solve({3,3})           -> 0
 *
 * CONSTRAINTS:
 *   - 1 <= stones.size() <= 30
 *   - 1 <= stones[i] <= 1000
 *
 * INSTRUCTIONS:
 *   Replace the body of solve() with your solution.
 */

#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int solve(vector<int> stones) {
    // TODO: Replace this with your solution
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    int n;
    cin >> n;
    vector<int> stones(n);
    for (int i = 0; i < n; i++) cin >> stones[i];
    cout << solve(stones) << endl;
    return 0;
}
