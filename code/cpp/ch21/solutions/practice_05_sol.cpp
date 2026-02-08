/* Solution: Practice 5 — Palindrome. TIME: O(n) SPACE: O(n) */
#include <iostream>
#include <vector>
using namespace std;
struct ListNode { int val; ListNode* next; ListNode(int v) : val(v), next(nullptr) {} };

bool solve(vector<int> arr) {
    if (arr.size() <= 1) return true;
    ListNode dummy(0); ListNode* cur = &dummy;
    for (int v : arr) { cur->next = new ListNode(v); cur = cur->next; }
    ListNode* head = dummy.next;
    ListNode* slow = head; ListNode* fast = head;
    while (fast && fast->next) { slow = slow->next; fast = fast->next->next; }
    ListNode* prev = nullptr; cur = slow;
    while (cur) { ListNode* nx = cur->next; cur->next = prev; prev = cur; cur = nx; }
    ListNode* left = head; ListNode* right = prev;
    while (right) { if (left->val != right->val) return false; left = left->next; right = right->next; }
    return true;
}

int main() { int n; cin>>n; vector<int> a(n); for(int i=0;i<n;i++) cin>>a[i];
    cout<<(solve(a)?"true":"false")<<endl; }
