/* Solution: Challenge 2 — Intersection. TIME: O(n+m) SPACE: O(n+m) */
#include <iostream>
#include <vector>
using namespace std;
struct ListNode { int val; ListNode* next; ListNode(int v) : val(v), next(nullptr) {} };

int solve(vector<int> arrA, vector<int> arrB, int skipA, int skipB) {
    if (skipA >= (int)arrA.size() || skipB >= (int)arrB.size()) return -1;
    int lenSuffix = (int)arrA.size() - skipA;
    if ((int)arrB.size() - skipB != lenSuffix) return -1;
    for (int i = 0; i < lenSuffix; i++)
        if (arrA[skipA+i] != arrB[skipB+i]) return -1;
    if (lenSuffix == 0) return -1;

    // Build shared suffix
    vector<ListNode*> shared;
    for (int i = 0; i < lenSuffix; i++) shared.push_back(new ListNode(arrA[skipA+i]));
    for (int i = 0; i < lenSuffix-1; i++) shared[i]->next = shared[i+1];

    // Build list A
    ListNode* headA;
    if (skipA > 0) {
        vector<ListNode*> prefA;
        for (int i = 0; i < skipA; i++) prefA.push_back(new ListNode(arrA[i]));
        for (int i = 0; i < skipA-1; i++) prefA[i]->next = prefA[i+1];
        prefA.back()->next = shared[0]; headA = prefA[0];
    } else { headA = shared[0]; }

    // Build list B
    ListNode* headB;
    if (skipB > 0) {
        vector<ListNode*> prefB;
        for (int i = 0; i < skipB; i++) prefB.push_back(new ListNode(arrB[i]));
        for (int i = 0; i < skipB-1; i++) prefB[i]->next = prefB[i+1];
        prefB.back()->next = shared[0]; headB = prefB[0];
    } else { headB = shared[0]; }

    ListNode* a = headA; ListNode* b = headB;
    while (a != b) {
        a = a ? a->next : headB;
        b = b ? b->next : headA;
    }
    return a ? a->val : -1;
}

int main() { int na; cin>>na; vector<int> aa(na); for(int i=0;i<na;i++) cin>>aa[i];
    int nb; cin>>nb; vector<int> ab(nb); for(int i=0;i<nb;i++) cin>>ab[i];
    int sa,sb; cin>>sa>>sb; cout<<solve(aa,ab,sa,sb)<<endl; }
