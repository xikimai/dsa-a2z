/*
 * Example 02: Slow/Fast Pointer Techniques
 * Chapter 21: Linked Lists — Pointers and Connections
 *
 * Demonstrates: Floyd's cycle detection, finding the middle node.
 */

#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

ListNode* buildList(vector<int>& arr) {
    ListNode dummy(0);
    ListNode* cur = &dummy;
    for (int v : arr) {
        cur->next = new ListNode(v);
        cur = cur->next;
    }
    return dummy.next;
}

ListNode* buildListWithCycle(vector<int>& arr, int cyclePos) {
    if (arr.empty()) return nullptr;
    vector<ListNode*> nodes;
    for (int v : arr) nodes.push_back(new ListNode(v));
    for (int i = 0; i < (int)nodes.size() - 1; i++) nodes[i]->next = nodes[i + 1];
    if (cyclePos >= 0) nodes.back()->next = nodes[cyclePos];
    return nodes[0];
}

bool hasCycle(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}

int findMiddle(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow->val;
}

int main() {
    cout << "=== Finding the Middle Node ===" << endl;
    vector<int> arr1 = {1, 2, 3, 4, 5};
    ListNode* head = buildList(arr1);
    cout << "List: [1,2,3,4,5] -> Middle: " << findMiddle(head) << endl;

    vector<int> arr2 = {1, 2, 3, 4};
    head = buildList(arr2);
    cout << "List: [1,2,3,4] -> Middle (second): " << findMiddle(head) << endl;

    cout << "\n=== Cycle Detection ===" << endl;
    vector<int> arr3 = {1, 2, 3, 4, 5};
    ListNode* noCycle = buildListWithCycle(arr3, -1);
    cout << "[1,2,3,4,5] no cycle: " << (hasCycle(noCycle) ? "true" : "false") << endl;

    ListNode* withCycle = buildListWithCycle(arr3, 2);
    cout << "[1,2,3,4,5] tail->node 2: " << (hasCycle(withCycle) ? "true" : "false") << endl;

    return 0;
}
