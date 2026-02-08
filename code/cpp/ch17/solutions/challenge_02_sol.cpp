/*
 * Solution for Challenge 2: Task Scheduler
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * APPROACH: Max-heap of frequencies. Each round, pick up to (n+1) tasks.
 *           Decrement counts, re-push non-zero. If more tasks remain,
 *           the round took a full cycle; otherwise only tasks done.
 * TIME:  O(total_tasks)
 * SPACE: O(1) auxiliary (at most 26 entries)
 */

#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int solve(vector<char> tasks, int n) {
    int freq[26] = {};
    for (char t : tasks) freq[t - 'A']++;

    priority_queue<int> pq;  // Max-heap of frequencies
    for (int f : freq) {
        if (f > 0) pq.push(f);
    }

    int time = 0;
    while (!pq.empty()) {
        int cycle = n + 1;
        vector<int> temp;
        int tasksDone = 0;

        for (int i = 0; i < cycle; i++) {
            if (!pq.empty()) {
                int cnt = pq.top(); pq.pop();
                if (cnt > 1) temp.push_back(cnt - 1);
                tasksDone++;
            }
        }

        for (int t : temp) pq.push(t);
        time += pq.empty() ? tasksDone : cycle;
    }
    return time;
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
