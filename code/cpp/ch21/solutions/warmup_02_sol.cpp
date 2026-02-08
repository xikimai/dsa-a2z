/* Solution: Warmup 2 — Insert at Position. TIME: O(n) SPACE: O(n) */
#include <iostream>
#include <vector>
using namespace std;
struct ListNode { int val; ListNode* next; ListNode(int v) : val(v), next(nullptr) {} };

vector<int> solve(vector<int> arr, int val, int pos) {
    ListNode dummy(0); ListNode* cur = &dummy;
    for (int v : arr) { cur->next = new ListNode(v); cur = cur->next; }
    ListNode* head = dummy.next;
    ListNode* nn = new ListNode(val);
    if (pos == 0) { nn->next = head; head = nn; }
    else {
        cur = head;
        for (int i = 0; i < pos-1 && cur; i++) cur = cur->next;
        if (cur) { nn->next = cur->next; cur->next = nn; }
    }
    vector<int> res; cur = head;
    while (cur) { res.push_back(cur->val); cur = cur->next; }
    return res;
}

int main() { int n; cin>>n; vector<int> a(n); for(int i=0;i<n;i++) cin>>a[i];
    int v,p; cin>>v>>p; auto r=solve(a,v,p);
    for(int i=0;i<(int)r.size();i++) cout<<(i?" ":"")<<r[i]; cout<<endl; }
