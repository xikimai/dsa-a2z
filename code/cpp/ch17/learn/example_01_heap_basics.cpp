/*
 * Example 01: Heap Basics
 * ==========================
 * Chapter 17: Heaps & Priority Queues — The VIP Line
 *
 * Demonstrates:
 *   Part 1: priority_queue basics (max-heap default, min-heap with greater<>)
 *   Part 2: Array representation of a heap
 *   Part 3: Manual bubble-up implementation
 *   Part 4: Heapify from a vector
 */

#include <algorithm>
#include <functional>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

// ── Part 1: Max-Heap and Min-Heap ───────────────────────────────────

void part1_max_min_heap() {
    cout << "=== Part 1: Max-Heap (default) and Min-Heap ===" << endl;

    // Max-heap (default)
    priority_queue<int> maxPQ;
    vector<int> data = {9, 5, 6, 2, 3, 8, 1, 7, 4};
    for (int x : data) maxPQ.push(x);

    cout << "  Max-heap top: " << maxPQ.top() << endl;
    cout << "  Polling all: ";
    while (!maxPQ.empty()) {
        cout << maxPQ.top() << " ";
        maxPQ.pop();
    }
    cout << endl;

    // Min-heap
    priority_queue<int, vector<int>, greater<int>> minPQ;
    for (int x : data) minPQ.push(x);

    cout << "  Min-heap top: " << minPQ.top() << endl;
    cout << "  Polling all: ";
    while (!minPQ.empty()) {
        cout << minPQ.top() << " ";
        minPQ.pop();
    }
    cout << endl;
}

// ── Part 2: Array Representation ────────────────────────────────────

void part2_array_representation() {
    cout << "\n=== Part 2: Heap as Array ===" << endl;

    vector<int> heap = {1, 3, 2, 7, 6, 5, 4, 8};
    cout << "  Array: [";
    for (int i = 0; i < (int)heap.size(); i++) {
        if (i) cout << ", ";
        cout << heap[i];
    }
    cout << "]" << endl;

    cout << "  Parent-child relationships:" << endl;
    for (int i = 0; i < (int)heap.size(); i++) {
        int parent = (i > 0) ? (i - 1) / 2 : -1;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        cout << "    node " << heap[i] << " (idx " << i << "): ";
        if (parent >= 0) cout << "parent=" << heap[parent];
        else cout << "ROOT";
        if (left < (int)heap.size()) cout << ", left=" << heap[left];
        else cout << ", left=none";
        if (right < (int)heap.size()) cout << ", right=" << heap[right];
        else cout << ", right=none";
        cout << endl;
    }
}

// ── Part 3: Manual Bubble-Up ────────────────────────────────────────

void part3_manual_bubble_up() {
    cout << "\n=== Part 3: Manual Bubble-Up (Min-Heap) ===" << endl;

    vector<int> heap;
    vector<int> values = {5, 3, 8, 1, 2};

    for (int val : values) {
        heap.push_back(val);
        int i = heap.size() - 1;
        string steps;
        while (i > 0) {
            int parent = (i - 1) / 2;
            if (heap[i] < heap[parent]) {
                if (!steps.empty()) steps += "; ";
                steps += "swap " + to_string(heap[i]) + " with " + to_string(heap[parent]);
                swap(heap[i], heap[parent]);
                i = parent;
            } else {
                break;
            }
        }
        if (steps.empty()) steps = "no swaps";
        cout << "  Push " << val << ": " << steps << " -> [";
        for (int j = 0; j < (int)heap.size(); j++) {
            if (j) cout << ",";
            cout << heap[j];
        }
        cout << "]" << endl;
    }
}

// ── Part 4: Build Heap from Vector ──────────────────────────────────

void part4_build_from_vector() {
    cout << "\n=== Part 4: Build Heap from Vector ===" << endl;

    vector<int> data = {5, 3, 8, 1, 2, 9, 4};
    cout << "  Input: [";
    for (int i = 0; i < (int)data.size(); i++) {
        if (i) cout << ",";
        cout << data[i];
    }
    cout << "]" << endl;

    // Build min-heap using range constructor
    priority_queue<int, vector<int>, greater<int>> pq(data.begin(), data.end());

    cout << "  Min-heap order: ";
    while (!pq.empty()) {
        cout << pq.top() << " ";
        pq.pop();
    }
    cout << endl;

    // Using make_heap from <algorithm>
    vector<int> v = {5, 3, 8, 1, 2, 9, 4};
    make_heap(v.begin(), v.end());  // Max-heap by default
    cout << "  make_heap (max): [";
    for (int i = 0; i < (int)v.size(); i++) {
        if (i) cout << ",";
        cout << v[i];
    }
    cout << "]  top=" << v.front() << endl;
}

// ── Main ────────────────────────────────────────────────────────────

int main() {
    part1_max_min_heap();
    part2_array_representation();
    part3_manual_bubble_up();
    part4_build_from_vector();
    return 0;
}
