/*
 * Example 01: Linked List Basics
 * Chapter 21: Linked Lists — Pointers and Connections
 *
 * Demonstrates: Building, traversing, inserting, deleting, and searching.
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

void printList(ListNode* head) {
    ListNode* cur = head;
    while (cur) {
        cout << cur->val << " -> ";
        cur = cur->next;
    }
    cout << "null" << endl;
}

ListNode* insertAtHead(ListNode* head, int val) {
    ListNode* newNode = new ListNode(val);
    newNode->next = head;
    return newNode;
}

ListNode* insertAtPosition(ListNode* head, int val, int pos) {
    ListNode* newNode = new ListNode(val);
    if (pos == 0) {
        newNode->next = head;
        return newNode;
    }
    ListNode* cur = head;
    for (int i = 0; i < pos - 1 && cur != nullptr; i++) {
        cur = cur->next;
    }
    if (cur) {
        newNode->next = cur->next;
        cur->next = newNode;
    }
    return head;
}

ListNode* deleteAtPosition(ListNode* head, int pos) {
    if (!head) return nullptr;
    if (pos == 0) {
        ListNode* newHead = head->next;
        delete head;
        return newHead;
    }
    ListNode* cur = head;
    for (int i = 0; i < pos - 1 && cur->next; i++) {
        cur = cur->next;
    }
    if (cur->next) {
        ListNode* toDelete = cur->next;
        cur->next = toDelete->next;
        delete toDelete;
    }
    return head;
}

bool search(ListNode* head, int target) {
    ListNode* cur = head;
    while (cur) {
        if (cur->val == target) return true;
        cur = cur->next;
    }
    return false;
}

int main() {
    cout << "=== Building a linked list ===" << endl;
    vector<int> arr = {10, 20, 30, 40, 50};
    ListNode* head = buildList(arr);
    printList(head);

    cout << "\n=== Insert 5 at head ===" << endl;
    head = insertAtHead(head, 5);
    printList(head);

    cout << "\n=== Insert 25 at position 3 ===" << endl;
    head = insertAtPosition(head, 25, 3);
    printList(head);

    cout << "\n=== Delete at position 0 ===" << endl;
    head = deleteAtPosition(head, 0);
    printList(head);

    cout << "\n=== Search ===" << endl;
    cout << "Search for 30: " << (search(head, 30) ? "true" : "false") << endl;
    cout << "Search for 99: " << (search(head, 99) ? "true" : "false") << endl;

    return 0;
}
