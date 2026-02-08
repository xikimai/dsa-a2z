/* Solution: Practice 3 — Merge Sorted. TIME: O(n+m) SPACE: O(n+m) */
#include <iostream>
#include <vector>
using namespace std;
struct ListNode { int val; ListNode* next; ListNode(int v) : val(v), next(nullptr) {} };

ListNode* build(vector<int>& arr) {
    ListNode dummy(0); ListNode* cur = &dummy;
    for (int v : arr) { cur->next = new ListNode(v); cur = cur->next; }
    return dummy.next;
}

vector<int> solve(vector<int> arr1, vector<int> arr2) {
    ListNode* h1 = build(arr1); ListNode* h2 = build(arr2);
    ListNode dummy(0); ListNode* cur = &dummy;
    while (h1 && h2) {
        if (h1->val <= h2->val) { cur->next = h1; h1 = h1->next; }
        else { cur->next = h2; h2 = h2->next; }
        cur = cur->next;
    }
    cur->next = h1 ? h1 : h2;
    vector<int> res; cur = dummy.next;
    while (cur) { res.push_back(cur->val); cur = cur->next; }
    return res;
}

int main() { int n1; cin>>n1; vector<int> a1(n1); for(int i=0;i<n1;i++) cin>>a1[i];
    int n2; cin>>n2; vector<int> a2(n2); for(int i=0;i<n2;i++) cin>>a2[i];
    auto r=solve(a1,a2); for(int i=0;i<(int)r.size();i++) cout<<(i?" ":"")<<r[i]; cout<<endl; }
