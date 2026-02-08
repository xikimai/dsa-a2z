/* Solution: Warmup 1 — Traverse. TIME: O(n) SPACE: O(n) */
#include <iostream>
#include <vector>
using namespace std;
struct ListNode { int val; ListNode* next; ListNode(int v) : val(v), next(nullptr) {} };

vector<int> solve(vector<int> arr) {
    ListNode dummy(0); ListNode* cur = &dummy;
    for (int v : arr) { cur->next = new ListNode(v); cur = cur->next; }
    vector<int> res; cur = dummy.next;
    while (cur) { res.push_back(cur->val); cur = cur->next; }
    return res;
}

int main() { int n; cin >> n; vector<int> a(n); for (int i=0;i<n;i++) cin>>a[i];
    auto r=solve(a); for (int i=0;i<(int)r.size();i++) cout<<(i?" ":"")<<r[i]; cout<<endl; }
