/* Solution: Practice 4 — Remove Nth From End. TIME: O(n) SPACE: O(n) */
#include <iostream>
#include <vector>
using namespace std;
struct ListNode { int val; ListNode* next; ListNode(int v) : val(v), next(nullptr) {} };

vector<int> solve(vector<int> arr, int n) {
    ListNode dummy(0); ListNode* cur = &dummy;
    for (int v : arr) { cur->next = new ListNode(v); cur = cur->next; }
    ListNode* front = &dummy; ListNode* back = &dummy;
    for (int i = 0; i <= n; i++) front = front->next;
    while (front) { front = front->next; back = back->next; }
    back->next = back->next->next;
    vector<int> res; cur = dummy.next;
    while (cur) { res.push_back(cur->val); cur = cur->next; }
    return res;
}

int main() { int sz; cin>>sz; vector<int> a(sz); for(int i=0;i<sz;i++) cin>>a[i];
    int n; cin>>n; auto r=solve(a,n);
    for(int i=0;i<(int)r.size();i++) cout<<(i?" ":"")<<r[i]; cout<<endl; }
