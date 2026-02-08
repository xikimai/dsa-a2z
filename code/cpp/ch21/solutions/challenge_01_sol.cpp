/* Solution: Challenge 1 — Cycle Start. TIME: O(n) SPACE: O(n) */
#include <iostream>
#include <vector>
using namespace std;
struct ListNode { int val; ListNode* next; ListNode(int v) : val(v), next(nullptr) {} };

int solve(vector<int> arr, int cyclePos) {
    if (arr.empty()) return -1;
    vector<ListNode*> nodes;
    for (int v : arr) nodes.push_back(new ListNode(v));
    for (int i = 0; i < (int)nodes.size()-1; i++) nodes[i]->next = nodes[i+1];
    if (cyclePos >= 0) nodes.back()->next = nodes[cyclePos];

    ListNode* slow = nodes[0]; ListNode* fast = nodes[0];
    bool hasCycle = false;
    while (fast && fast->next) {
        slow = slow->next; fast = fast->next->next;
        if (slow == fast) { hasCycle = true; break; }
    }
    if (!hasCycle) return -1;
    slow = nodes[0];
    while (slow != fast) { slow = slow->next; fast = fast->next; }
    ListNode* cur = nodes[0]; int idx = 0;
    while (cur != slow) { cur = cur->next; idx++; }
    return idx;
}

int main() { int n; cin>>n; vector<int> a(n); for(int i=0;i<n;i++) cin>>a[i];
    int cp; cin>>cp; cout<<solve(a,cp)<<endl; }
