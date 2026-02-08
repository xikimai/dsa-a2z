/* Solution: Practice 1 — Find Middle. TIME: O(n) SPACE: O(n) */
#include <iostream>
#include <vector>
using namespace std;
struct ListNode { int val; ListNode* next; ListNode(int v) : val(v), next(nullptr) {} };

int solve(vector<int> arr) {
    ListNode dummy(0); ListNode* cur = &dummy;
    for (int v : arr) { cur->next = new ListNode(v); cur = cur->next; }
    ListNode* slow = dummy.next; ListNode* fast = dummy.next;
    while (fast && fast->next) { slow = slow->next; fast = fast->next->next; }
    return slow->val;
}

int main() { int n; cin>>n; vector<int> a(n); for(int i=0;i<n;i++) cin>>a[i]; cout<<solve(a)<<endl; }
