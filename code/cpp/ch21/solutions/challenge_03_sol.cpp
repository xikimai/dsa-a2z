/* Solution: Challenge 3 — Add Two Numbers. TIME: O(max(n,m)) SPACE: O(max(n,m)) */
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
    ListNode* l1 = build(arr1); ListNode* l2 = build(arr2);
    ListNode dummy(0); ListNode* cur = &dummy;
    int carry = 0;
    while (l1 || l2 || carry) {
        int v1 = l1 ? l1->val : 0;
        int v2 = l2 ? l2->val : 0;
        int total = v1 + v2 + carry;
        carry = total / 10;
        cur->next = new ListNode(total % 10);
        cur = cur->next;
        if (l1) l1 = l1->next;
        if (l2) l2 = l2->next;
    }
    vector<int> res; cur = dummy.next;
    while (cur) { res.push_back(cur->val); cur = cur->next; }
    return res;
}

int main() { int n1; cin>>n1; vector<int> a1(n1); for(int i=0;i<n1;i++) cin>>a1[i];
    int n2; cin>>n2; vector<int> a2(n2); for(int i=0;i<n2;i++) cin>>a2[i];
    auto r=solve(a1,a2); for(int i=0;i<(int)r.size();i++) cout<<(i?" ":"")<<r[i]; cout<<endl; }
