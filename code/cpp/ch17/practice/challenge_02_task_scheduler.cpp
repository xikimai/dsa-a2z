/*
 * Challenge 2: Task Scheduler
 * =============================
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * PROBLEM:
 *   Given a list of tasks (uppercase letters) and a cooldown interval n,
 *   return the minimum number of intervals needed to complete all tasks.
 *   Same tasks must have at least n intervals between them. Idle intervals
 *   can be inserted.
 *
 * EXAMPLES:
 *   solve({'A','A','A','B','B','B'}, 2)  -> 8
 *   solve({'A','A','A','B','B','B'}, 0)  -> 6
 *
 * CONSTRAINTS:
 *   - 1 <= tasks.size() <= 10^4
 *   - tasks[i] is uppercase English letter
 *   - 0 <= n <= 100
 *
 * INSTRUCTIONS:
 *   Replace the body of solve() with your solution.
 */

#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int solve(vector<char> tasks, int n) {
    // TODO: Replace this with your solution
    return 0;
}

// -- Do not change anything below this line --------------------------
int main() {
    int m, n;
    cin >> m;
    vector<char> tasks(m);
    for (int i = 0; i < m; i++) cin >> tasks[i];
    cin >> n;
    cout << solve(tasks, n) << endl;
    return 0;
}
