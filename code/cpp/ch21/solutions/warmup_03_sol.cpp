/* Solution: Warmup 3 — Delete at Position. TIME: O(n) SPACE: O(n) */
#include <iostream>
#include <vector>
using namespace std;
struct ListNode { int val; ListNode* next; ListNode(int v) : val(v), next(nullptr) {} };

vector<int> solve(vector<int> arr, int pos) {
    ListNode dummy(0); ListNode* cur = &dummy;
    for (int v : arr) { cur->next = new ListNode(v); cur = cur->next; }
    ListNode* head = dummy.next;
    if (!head) return {};
    if (pos == 0) { head = head->next; }
    else {
        cur = head;
        for (int i = 0; i < pos-1 && cur->next; i++) cur = cur->next;
        if (cur->next) cur->next = cur->next->next;
    }
    vector<int> res; cur = head;
    while (cur) { res.push_back(cur->val); cur = cur->next; }
    return res;
}

int main() { int n; cin>>n; vector<int> a(n); for(int i=0;i<n;i++) cin>>a[i];
    int p; cin>>p; auto r=solve(a,p);
    for(int i=0;i<(int)r.size();i++) cout<<(i?" ":"")<<r[i]; cout<<endl; }
