/*
 * Tests for Chapter 21: Linked Lists — Pointers and Connections
 * Build: g++ -std=c++17 -o /tmp/test_ch21 code/cpp/ch21/tests/test_ch21.cpp && /tmp/test_ch21
 */

#include <algorithm>
#include <cassert>
#include <climits>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// =====================================================================
// ListNode definition used by all reference solutions
// =====================================================================
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

ListNode* buildLL(vector<int> arr) {
    ListNode dummy(0);
    ListNode* cur = &dummy;
    for (int v : arr) { cur->next = new ListNode(v); cur = cur->next; }
    return dummy.next;
}

vector<int> toVec(ListNode* head) {
    vector<int> res;
    while (head) { res.push_back(head->val); head = head->next; }
    return res;
}

// =====================================================================
// Reference solutions
// =====================================================================

// W1: Traverse
vector<int> ref_traverse(vector<int> arr) {
    return toVec(buildLL(arr));
}

// W2: Insert at Position
vector<int> ref_insert(vector<int> arr, int val, int pos) {
    ListNode* head = buildLL(arr);
    ListNode* nn = new ListNode(val);
    if (pos == 0) { nn->next = head; head = nn; }
    else {
        ListNode* cur = head;
        for (int i = 0; i < pos-1 && cur; i++) cur = cur->next;
        if (cur) { nn->next = cur->next; cur->next = nn; }
    }
    return toVec(head);
}

// W3: Delete at Position
vector<int> ref_delete(vector<int> arr, int pos) {
    ListNode* head = buildLL(arr);
    if (!head) return {};
    if (pos == 0) return toVec(head->next);
    ListNode* cur = head;
    for (int i = 0; i < pos-1 && cur->next; i++) cur = cur->next;
    if (cur->next) cur->next = cur->next->next;
    return toVec(head);
}

// W4: Search
bool ref_search(vector<int> arr, int target) {
    ListNode* cur = buildLL(arr);
    while (cur) { if (cur->val == target) return true; cur = cur->next; }
    return false;
}

// W5: Reverse
vector<int> ref_reverse(vector<int> arr) {
    ListNode* head = buildLL(arr);
    ListNode* prev = nullptr; ListNode* cur = head;
    while (cur) { ListNode* nx = cur->next; cur->next = prev; prev = cur; cur = nx; }
    return toVec(prev);
}

// P1: Find Middle
int ref_find_middle(vector<int> arr) {
    ListNode* head = buildLL(arr);
    ListNode* slow = head; ListNode* fast = head;
    while (fast && fast->next) { slow = slow->next; fast = fast->next->next; }
    return slow->val;
}

// P2: Detect Cycle
bool ref_detect_cycle(vector<int> arr, int cyclePos) {
    if (arr.empty()) return false;
    vector<ListNode*> nodes;
    for (int v : arr) nodes.push_back(new ListNode(v));
    for (int i = 0; i < (int)nodes.size()-1; i++) nodes[i]->next = nodes[i+1];
    if (cyclePos >= 0) nodes.back()->next = nodes[cyclePos];
    ListNode* slow = nodes[0]; ListNode* fast = nodes[0];
    while (fast && fast->next) {
        slow = slow->next; fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}

// P3: Merge Sorted
vector<int> ref_merge_sorted(vector<int> a1, vector<int> a2) {
    ListNode* h1 = buildLL(a1); ListNode* h2 = buildLL(a2);
    ListNode dummy(0); ListNode* cur = &dummy;
    while (h1 && h2) {
        if (h1->val <= h2->val) { cur->next = h1; h1 = h1->next; }
        else { cur->next = h2; h2 = h2->next; }
        cur = cur->next;
    }
    cur->next = h1 ? h1 : h2;
    return toVec(dummy.next);
}

// P4: Remove Nth From End
vector<int> ref_remove_nth(vector<int> arr, int n) {
    ListNode dummy(0); ListNode* cur = &dummy;
    for (int v : arr) { cur->next = new ListNode(v); cur = cur->next; }
    ListNode* front = &dummy; ListNode* back = &dummy;
    for (int i = 0; i <= n; i++) front = front->next;
    while (front) { front = front->next; back = back->next; }
    back->next = back->next->next;
    return toVec(dummy.next);
}

// P5: Palindrome
bool ref_palindrome(vector<int> arr) {
    if (arr.size() <= 1) return true;
    ListNode* head = buildLL(arr);
    ListNode* slow = head; ListNode* fast = head;
    while (fast && fast->next) { slow = slow->next; fast = fast->next->next; }
    ListNode* prev = nullptr; ListNode* cur = slow;
    while (cur) { ListNode* nx = cur->next; cur->next = prev; prev = cur; cur = nx; }
    ListNode* left = head; ListNode* right = prev;
    while (right) { if (left->val != right->val) return false; left = left->next; right = right->next; }
    return true;
}

// C1: Cycle Start
int ref_cycle_start(vector<int> arr, int cyclePos) {
    if (arr.empty()) return -1;
    vector<ListNode*> nodes;
    for (int v : arr) nodes.push_back(new ListNode(v));
    for (int i = 0; i < (int)nodes.size()-1; i++) nodes[i]->next = nodes[i+1];
    if (cyclePos >= 0) nodes.back()->next = nodes[cyclePos];
    ListNode* slow = nodes[0]; ListNode* fast = nodes[0];
    bool hasCycle = false;
    while (fast && fast->next) {
        slow = slow->next; fast = fast->next->next;
        if (slow == fast) { hasCycle = true; break; }
    }
    if (!hasCycle) return -1;
    slow = nodes[0];
    while (slow != fast) { slow = slow->next; fast = fast->next; }
    ListNode* cur = nodes[0]; int idx = 0;
    while (cur != slow) { cur = cur->next; idx++; }
    return idx;
}

// C2: Intersection
int ref_intersection(vector<int> arrA, vector<int> arrB, int skipA, int skipB) {
    if (skipA >= (int)arrA.size() || skipB >= (int)arrB.size()) return -1;
    int lenSuffix = (int)arrA.size() - skipA;
    if ((int)arrB.size() - skipB != lenSuffix) return -1;
    for (int i = 0; i < lenSuffix; i++)
        if (arrA[skipA+i] != arrB[skipB+i]) return -1;
    if (lenSuffix == 0) return -1;
    vector<ListNode*> shared;
    for (int i = 0; i < lenSuffix; i++) shared.push_back(new ListNode(arrA[skipA+i]));
    for (int i = 0; i < lenSuffix-1; i++) shared[i]->next = shared[i+1];
    ListNode* headA = shared[0]; ListNode* headB = shared[0];
    if (skipA > 0) {
        vector<ListNode*> pA;
        for (int i = 0; i < skipA; i++) pA.push_back(new ListNode(arrA[i]));
        for (int i = 0; i < skipA-1; i++) pA[i]->next = pA[i+1];
        pA.back()->next = shared[0]; headA = pA[0];
    }
    if (skipB > 0) {
        vector<ListNode*> pB;
        for (int i = 0; i < skipB; i++) pB.push_back(new ListNode(arrB[i]));
        for (int i = 0; i < skipB-1; i++) pB[i]->next = pB[i+1];
        pB.back()->next = shared[0]; headB = pB[0];
    }
    ListNode* a = headA; ListNode* b = headB;
    while (a != b) { a = a ? a->next : headB; b = b ? b->next : headA; }
    return a ? a->val : -1;
}

// C3: Add Two Numbers
vector<int> ref_add_two(vector<int> a1, vector<int> a2) {
    ListNode* l1 = buildLL(a1); ListNode* l2 = buildLL(a2);
    ListNode dummy(0); ListNode* cur = &dummy;
    int carry = 0;
    while (l1 || l2 || carry) {
        int v1 = l1 ? l1->val : 0; int v2 = l2 ? l2->val : 0;
        int total = v1 + v2 + carry; carry = total / 10;
        cur->next = new ListNode(total % 10); cur = cur->next;
        if (l1) l1 = l1->next; if (l2) l2 = l2->next;
    }
    return toVec(dummy.next);
}

// C4: Flatten (encoded with BEGIN_LIST/END_LIST markers)
static const int BEGIN_LIST = -999999;
static const int END_LIST = -999998;

vector<int> ref_flatten(vector<int> encoded) {
    vector<int> result;
    for (int val : encoded) {
        if (val != BEGIN_LIST && val != END_LIST) result.push_back(val);
    }
    return result;
}

// =====================================================================
// Test framework
// =====================================================================

int tests_passed = 0;
int tests_total = 0;

void check(bool condition, const string& name) {
    tests_total++;
    if (condition) {
        tests_passed++;
    } else {
        cout << "  FAIL: " << name << endl;
    }
}

// =====================================================================
// Test functions
// =====================================================================

void test_w1() {
    cout << "Testing W1: Traverse..." << endl;
    check(ref_traverse({1,2,3}) == vector<int>{1,2,3}, "basic");
    check(ref_traverse({5}) == vector<int>{5}, "single");
    check(ref_traverse({}) == vector<int>{}, "empty");
    check(ref_traverse({10,20,30,40,50}) == vector<int>{10,20,30,40,50}, "five");
    check(ref_traverse({-1,-2,-3}) == vector<int>{-1,-2,-3}, "negative");
}

void test_w2() {
    cout << "Testing W2: Insert at Position..." << endl;
    check(ref_insert({1,2,3,4}, 10, 2) == vector<int>{1,2,10,3,4}, "middle");
    check(ref_insert({1,2,3}, 0, 0) == vector<int>{0,1,2,3}, "head");
    check(ref_insert({1,2,3}, 4, 3) == vector<int>{1,2,3,4}, "tail");
    check(ref_insert({}, 5, 0) == vector<int>{5}, "empty");
    check(ref_insert({1}, 2, 1) == vector<int>{1,2}, "single");
}

void test_w3() {
    cout << "Testing W3: Delete at Position..." << endl;
    check(ref_delete({1,2,3,4,5}, 2) == vector<int>{1,2,4,5}, "middle");
    check(ref_delete({1,2,3}, 0) == vector<int>{2,3}, "head");
    check(ref_delete({1,2,3}, 2) == vector<int>{1,2}, "tail");
    check(ref_delete({1}, 0) == vector<int>{}, "single");
    check(ref_delete({10,20,30,40}, 1) == vector<int>{10,30,40}, "second");
}

void test_w4() {
    cout << "Testing W4: Search..." << endl;
    check(ref_search({1,2,3,4,5}, 3) == true, "found");
    check(ref_search({1,2,3}, 7) == false, "not found");
    check(ref_search({}, 1) == false, "empty");
    check(ref_search({5}, 5) == true, "single found");
    check(ref_search({5}, 3) == false, "single not found");
    check(ref_search({10,20,30}, 10) == true, "first");
    check(ref_search({10,20,30}, 30) == true, "last");
}

void test_w5() {
    cout << "Testing W5: Reverse..." << endl;
    check(ref_reverse({1,2,3,4,5}) == vector<int>{5,4,3,2,1}, "basic");
    check(ref_reverse({1,2}) == vector<int>{2,1}, "two");
    check(ref_reverse({1}) == vector<int>{1}, "single");
    check(ref_reverse({}) == vector<int>{}, "empty");
    check(ref_reverse({5,4,3,2,1}) == vector<int>{1,2,3,4,5}, "already reversed");
}

void test_p1() {
    cout << "Testing P1: Find Middle..." << endl;
    check(ref_find_middle({1,2,3,4,5}) == 3, "odd");
    check(ref_find_middle({1,2,3,4}) == 3, "even");
    check(ref_find_middle({1}) == 1, "single");
    check(ref_find_middle({1,2}) == 2, "two");
    check(ref_find_middle({10,20,30}) == 20, "three");
    check(ref_find_middle({1,2,3,4,5,6}) == 4, "six");
}

void test_p2() {
    cout << "Testing P2: Detect Cycle..." << endl;
    check(ref_detect_cycle({3,2,0,-4}, 1) == true, "cycle mid");
    check(ref_detect_cycle({1,2}, -1) == false, "no cycle");
    check(ref_detect_cycle({1}, 0) == true, "self loop");
    check(ref_detect_cycle({1,2,3}, 0) == true, "cycle head");
    check(ref_detect_cycle({}, -1) == false, "empty");
    check(ref_detect_cycle({1,2,3,4,5,6,7}, -1) == false, "long no cycle");
    check(ref_detect_cycle({1,2,3,4}, 3) == true, "cycle tail");
}

void test_p3() {
    cout << "Testing P3: Merge Sorted..." << endl;
    check(ref_merge_sorted({1,3,5}, {2,4,6}) == vector<int>{1,2,3,4,5,6}, "basic");
    check(ref_merge_sorted({}, {1,2,3}) == vector<int>{1,2,3}, "first empty");
    check(ref_merge_sorted({1,2,3}, {}) == vector<int>{1,2,3}, "second empty");
    check(ref_merge_sorted({}, {}) == vector<int>{}, "both empty");
    check(ref_merge_sorted({1,2,3}, {1,2,3}) == vector<int>{1,1,2,2,3,3}, "duplicates");
    check(ref_merge_sorted({1}, {2}) == vector<int>{1,2}, "single");
}

void test_p4() {
    cout << "Testing P4: Remove Nth From End..." << endl;
    check(ref_remove_nth({1,2,3,4,5}, 2) == vector<int>{1,2,3,5}, "2nd from end");
    check(ref_remove_nth({1,2}, 1) == vector<int>{1}, "last");
    check(ref_remove_nth({1}, 1) == vector<int>{}, "only");
    check(ref_remove_nth({1,2,3}, 1) == vector<int>{1,2}, "1st from end");
    check(ref_remove_nth({1,2,3}, 3) == vector<int>{2,3}, "head");
    check(ref_remove_nth({1,2}, 2) == vector<int>{2}, "head of two");
}

void test_p5() {
    cout << "Testing P5: Palindrome..." << endl;
    check(ref_palindrome({1,2,3,2,1}) == true, "odd palindrome");
    check(ref_palindrome({1,2,3,4,5}) == false, "not palindrome");
    check(ref_palindrome({1}) == true, "single");
    check(ref_palindrome({}) == true, "empty");
    check(ref_palindrome({1,2,2,1}) == true, "even palindrome");
    check(ref_palindrome({1,1}) == true, "two same");
    check(ref_palindrome({1,2}) == false, "two different");
}

void test_c1() {
    cout << "Testing C1: Cycle Start..." << endl;
    check(ref_cycle_start({3,2,0,-4}, 1) == 1, "idx 1");
    check(ref_cycle_start({1,2}, 0) == 0, "idx 0");
    check(ref_cycle_start({1}, -1) == -1, "no cycle");
    check(ref_cycle_start({1}, 0) == 0, "self loop");
    check(ref_cycle_start({1,2,3,4,5}, 2) == 2, "idx 2");
    check(ref_cycle_start({}, -1) == -1, "empty");
}

void test_c2() {
    cout << "Testing C2: Intersection..." << endl;
    check(ref_intersection({4,1,8,4,5}, {5,6,1,8,4,5}, 2, 3) == 8, "basic");
    check(ref_intersection({1,2,3}, {4,5,6}, 3, 3) == -1, "none");
    check(ref_intersection({1,2,3}, {1,2,3}, 0, 0) == 1, "at head");
    check(ref_intersection({1,9,1,2,4}, {3,2,4}, 3, 1) == 2, "diff prefix");
    check(ref_intersection({1,2,7}, {3,4,5,7}, 2, 3) == 7, "single shared");
}

void test_c3() {
    cout << "Testing C3: Add Two Numbers..." << endl;
    check(ref_add_two({2,4,3}, {5,6,4}) == vector<int>{7,0,8}, "342+465");
    check(ref_add_two({9,9,9}, {1}) == vector<int>{0,0,0,1}, "999+1");
    check(ref_add_two({0}, {0}) == vector<int>{0}, "0+0");
    check(ref_add_two({9,9}, {1}) == vector<int>{0,0,1}, "99+1");
    check(ref_add_two({5}, {5}) == vector<int>{0,1}, "5+5");
    check(ref_add_two({1,2,3}, {4,5,6}) == vector<int>{5,7,9}, "321+654");
}

void test_c4() {
    cout << "Testing C4: Flatten..." << endl;
    // [1, 2, [3, 4, [5, 6]], 7] encoded
    check(ref_flatten({1, 2, BEGIN_LIST, 3, 4, BEGIN_LIST, 5, 6, END_LIST, END_LIST, 7})
          == vector<int>{1,2,3,4,5,6,7}, "nested");
    check(ref_flatten({1, BEGIN_LIST, 2, BEGIN_LIST, 3, END_LIST, END_LIST})
          == vector<int>{1,2,3}, "deep");
    check(ref_flatten({1, 2, 3}) == vector<int>{1,2,3}, "flat");
    check(ref_flatten({}) == vector<int>{}, "empty");
}

// =====================================================================
// Main
// =====================================================================

int main() {
    test_w1();
    test_w2();
    test_w3();
    test_w4();
    test_w5();
    test_p1();
    test_p2();
    test_p3();
    test_p4();
    test_p5();
    test_c1();
    test_c2();
    test_c3();
    test_c4();

    cout << endl;
    if (tests_passed == tests_total) {
        cout << "All " << tests_total << " tests passed!" << endl;
    } else {
        cout << tests_passed << " / " << tests_total << " tests passed." << endl;
    }
    return (tests_passed == tests_total) ? 0 : 1;
}
