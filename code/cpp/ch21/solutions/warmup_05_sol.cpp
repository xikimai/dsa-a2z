/* Solution: Warmup 5 — Reverse. TIME: O(n) SPACE: O(n) build + O(1) reverse */
#include <iostream>
#include <vector>
using namespace std;
struct ListNode { int val; ListNode* next; ListNode(int v) : val(v), next(nullptr) {} };

vector<int> solve(vector<int> arr) {
    ListNode dummy(0); ListNode* cur = &dummy;
    for (int v : arr) { cur->next = new ListNode(v); cur = cur->next; }
    ListNode* prev = nullptr; cur = dummy.next;
    while (cur) { ListNode* nx = cur->next; cur->next = prev; prev = cur; cur = nx; }
    vector<int> res; cur = prev;
    while (cur) { res.push_back(cur->val); cur = cur->next; }
    return res;
}

int main() { int n; cin>>n; vector<int> a(n); for(int i=0;i<n;i++) cin>>a[i];
    auto r=solve(a); for(int i=0;i<(int)r.size();i++) cout<<(i?" ":"")<<r[i]; cout<<endl; }
