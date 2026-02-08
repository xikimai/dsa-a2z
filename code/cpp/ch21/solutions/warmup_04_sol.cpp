/* Solution: Warmup 4 — Search. TIME: O(n) SPACE: O(n) */
#include <iostream>
#include <vector>
using namespace std;
struct ListNode { int val; ListNode* next; ListNode(int v) : val(v), next(nullptr) {} };

bool solve(vector<int> arr, int target) {
    ListNode dummy(0); ListNode* cur = &dummy;
    for (int v : arr) { cur->next = new ListNode(v); cur = cur->next; }
    cur = dummy.next;
    while (cur) { if (cur->val == target) return true; cur = cur->next; }
    return false;
}

int main() { int n; cin>>n; vector<int> a(n); for(int i=0;i<n;i++) cin>>a[i];
    int t; cin>>t; cout<<(solve(a,t)?"true":"false")<<endl; }
