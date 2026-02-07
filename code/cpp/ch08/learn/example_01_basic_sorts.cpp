/*
 * Example 01: Basic Sorts -- Selection, Bubble, Insertion
 * =======================================================
 * Chapter 8: The Art of Sorting -- Putting Things in Order
 *
 * This file demonstrates three O(n^2) sorting algorithms:
 *   Part 1: Selection Sort -- find the minimum, swap it into place
 *   Part 2: Bubble Sort -- bubble the largest to the end, repeat
 *   Part 3: Insertion Sort -- insert each element into its sorted spot
 *
 * Build & run:
 *   g++ -std=c++17 -o example_01 code/cpp/ch08/learn/example_01_basic_sorts.cpp && ./example_01
 */

#include <iostream>
#include <vector>
using namespace std;

// Helper: print a vector with an optional label
void print_vec(const string& label, const vector<int>& v) {
    cout << "  " << label << " [";
    for (int i = 0; i < (int)v.size(); i++) {
        if (i > 0) cout << ", ";
        cout << v[i];
    }
    cout << "]" << endl;
}

// =====================================================================
// 1. Selection Sort
// =====================================================================
// Idea: Find the smallest element, put it first.
//       Find the second-smallest, put it second. Repeat.
// Time:  O(n^2) always
// Space: O(1)

void demo_selection_sort() {
    cout << "=== PART 1: Selection Sort ===" << endl;

    vector<int> arr = {64, 25, 12, 22, 11};
    print_vec("Original:", arr);

    int n = (int)arr.size();
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) min_idx = j;
        }
        swap(arr[i], arr[min_idx]);
        cout << "  Pass " << i + 1 << ": swapped arr[" << i << "] with arr["
             << min_idx << "] -> ";
        for (int k = 0; k < n; k++) cout << arr[k] << " ";
        cout << endl;
    }

    print_vec("Sorted:  ", arr);
    cout << endl;
}

// =====================================================================
// 2. Bubble Sort
// =====================================================================
// Idea: Compare adjacent elements and swap if out of order.
//       After each pass, the largest unsorted element "bubbles up".
// Time:  O(n^2) worst, O(n) best (with early termination)
// Space: O(1)

void demo_bubble_sort() {
    cout << "=== PART 2: Bubble Sort ===" << endl;

    vector<int> arr = {64, 34, 25, 12, 22, 11, 90};
    print_vec("Original:", arr);

    int n = (int)arr.size();
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        cout << "  Pass " << i + 1 << ": ";
        for (int k = 0; k < n; k++) cout << arr[k] << " ";
        if (!swapped) cout << " (no swaps -- done early!)";
        cout << endl;
        if (!swapped) break;
    }

    print_vec("Sorted:  ", arr);
    cout << endl;
}

// =====================================================================
// 3. Insertion Sort
// =====================================================================
// Idea: Take each element and INSERT it into the correct position
//       among the already-sorted elements to its left.
// Time:  O(n^2) worst, O(n) best (already sorted)
// Space: O(1)

void demo_insertion_sort() {
    cout << "=== PART 3: Insertion Sort ===" << endl;

    vector<int> arr = {12, 11, 13, 5, 6};
    print_vec("Original:", arr);

    int n = (int)arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
        cout << "  Insert arr[" << i << "]=" << key << ": ";
        for (int k = 0; k < n; k++) cout << arr[k] << " ";
        cout << endl;
    }

    print_vec("Sorted:  ", arr);
    cout << endl;
}

// =====================================================================
// main -- run all demos
// =====================================================================
int main() {
    cout << "Chapter 8: Basic Sorts" << endl;
    cout << "======================" << endl << endl;

    demo_selection_sort();
    demo_bubble_sort();
    demo_insertion_sort();

    cout << "All three are O(n^2), but they behave differently:" << endl;
    cout << "  - Selection Sort: always ~n^2/2 comparisons, few swaps" << endl;
    cout << "  - Bubble Sort: can stop early if already sorted" << endl;
    cout << "  - Insertion Sort: great for nearly-sorted data, used inside TimSort" << endl;
    return 0;
}
