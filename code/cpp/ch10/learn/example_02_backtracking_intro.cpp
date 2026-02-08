/*
 * Example 02: Backtracking Introduction
 * =======================================
 * Chapter 10: The Magic of Recursion
 *
 * This file demonstrates:
 *   Part 1: Generate subsets of {1,2,3} with trace
 *   Part 2: Generate permutations of {1,2,3}
 *   Part 3: N-Queens 4x4 demo
 *   Part 4: Backtracking template summary
 *
 * Build & run:
 *   g++ -std=c++17 -o example_02 code/cpp/ch10/learn/example_02_backtracking_intro.cpp && ./example_02
 */

#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Helper: print a vector of ints
void print_vec(const vector<int>& v) {
    cout << "{";
    for (int i = 0; i < (int)v.size(); i++) {
        if (i > 0) cout << ", ";
        cout << v[i];
    }
    cout << "}";
}

// =====================================================================
// 1. Generate All Subsets with Trace
// =====================================================================
// Idea: At each element, choose to INCLUDE it or EXCLUDE it.
//       This builds a binary decision tree.

void subsets_traced(const vector<int>& nums, int idx, vector<int>& current,
                    vector<vector<int>>& result, int depth) {
    string indent(depth * 2, ' ');

    if (idx == (int)nums.size()) {
        cout << indent << "-> Reached end, add subset: ";
        print_vec(current);
        cout << endl;
        result.push_back(current);
        return;
    }

    // Branch 1: INCLUDE nums[idx]
    cout << indent << "Include " << nums[idx] << endl;
    current.push_back(nums[idx]);
    subsets_traced(nums, idx + 1, current, result, depth + 1);

    // Branch 2: EXCLUDE nums[idx] (backtrack!)
    cout << indent << "Exclude " << nums[idx] << " (backtrack)" << endl;
    current.pop_back();
    subsets_traced(nums, idx + 1, current, result, depth + 1);
}

void demo_subsets() {
    cout << "=== PART 1: Generate All Subsets of {1, 2, 3} ===" << endl;
    cout << endl;
    cout << "  At each element, we choose: INCLUDE or EXCLUDE." << endl;
    cout << "  Watch the decision tree unfold:" << endl;
    cout << endl;

    vector<int> nums = {1, 2, 3};
    vector<int> current;
    vector<vector<int>> result;
    subsets_traced(nums, 0, current, result, 1);

    cout << endl;
    cout << "  All " << result.size() << " subsets:" << endl;
    cout << "  ";
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << ", ";
        print_vec(result[i]);
    }
    cout << endl;
    cout << endl;
    cout << "  With 3 elements, we get 2^3 = 8 subsets." << endl;
    cout << endl;
}

// =====================================================================
// 2. Generate All Permutations
// =====================================================================
// Idea: At each position, try every remaining (unused) element.
//       Swap elements to build each permutation.

void permutations_traced(vector<int>& nums, int start,
                          vector<vector<int>>& result, int depth) {
    string indent(depth * 2, ' ');

    if (start == (int)nums.size()) {
        cout << indent << "-> Complete permutation: ";
        print_vec(nums);
        cout << endl;
        result.push_back(nums);
        return;
    }

    for (int i = start; i < (int)nums.size(); i++) {
        cout << indent << "Swap position " << start << " with " << i
             << " (place " << nums[i] << " at position " << start << ")" << endl;
        swap(nums[start], nums[i]);
        permutations_traced(nums, start + 1, result, depth + 1);
        swap(nums[start], nums[i]);  // backtrack
        if (i != start) {
            cout << indent << "Undo swap (backtrack)" << endl;
        }
    }
}

void demo_permutations() {
    cout << "=== PART 2: Generate All Permutations of {1, 2, 3} ===" << endl;
    cout << endl;
    cout << "  At each position, try every remaining element." << endl;
    cout << "  Swap, recurse, then swap back (backtrack)." << endl;
    cout << endl;

    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result;
    permutations_traced(nums, 0, result, 1);

    cout << endl;
    cout << "  All " << result.size() << " permutations:" << endl;
    cout << "  ";
    for (int i = 0; i < (int)result.size(); i++) {
        if (i > 0) cout << ", ";
        print_vec(result[i]);
    }
    cout << endl;
    cout << endl;
    cout << "  With 3 elements, we get 3! = 6 permutations." << endl;
    cout << endl;
}

// =====================================================================
// 3. N-Queens 4x4 Demo
// =====================================================================
// Idea: Place queens one row at a time. Before placing, check all
//       constraints (column, diagonals). If stuck, backtrack.

bool is_safe(const vector<int>& queens, int row, int col) {
    for (int r = 0; r < row; r++) {
        int c = queens[r];
        if (c == col) return false;                    // same column
        if (r - c == row - col) return false;          // same diagonal
        if (r + c == row + col) return false;          // same anti-diagonal
    }
    return true;
}

void print_board(const vector<int>& queens, int n) {
    for (int r = 0; r < n; r++) {
        cout << "    ";
        for (int c = 0; c < n; c++) {
            cout << (queens[r] == c ? "Q " : ". ");
        }
        cout << endl;
    }
}

void nqueens(int n, int row, vector<int>& queens,
             vector<vector<int>>& solutions, int depth) {
    string indent(depth * 2, ' ');

    if (row == n) {
        cout << indent << "-> Found a solution!" << endl;
        solutions.push_back(queens);
        return;
    }

    for (int col = 0; col < n; col++) {
        if (is_safe(queens, row, col)) {
            cout << indent << "Place queen at row " << row << ", col " << col << endl;
            queens[row] = col;
            nqueens(n, row + 1, queens, solutions, depth + 1);
            queens[row] = -1;  // backtrack
        }
    }
}

void demo_nqueens() {
    cout << "=== PART 3: N-Queens on a 4x4 Board ===" << endl;
    cout << endl;
    cout << "  Place 4 queens so no two attack each other." << endl;
    cout << "  (No two queens share a row, column, or diagonal.)" << endl;
    cout << endl;

    int n = 4;
    vector<int> queens(n, -1);
    vector<vector<int>> solutions;
    nqueens(n, 0, queens, solutions, 1);

    cout << endl;
    cout << "  Found " << solutions.size() << " solutions:" << endl;
    cout << endl;
    for (int i = 0; i < (int)solutions.size(); i++) {
        cout << "  Solution " << (i + 1) << ":" << endl;
        print_board(solutions[i], n);
        cout << endl;
    }
}

// =====================================================================
// 4. Backtracking Template Summary
// =====================================================================

void demo_template() {
    cout << "=== PART 4: Backtracking Template ===" << endl;
    cout << endl;
    cout << "  Every backtracking problem follows this pattern:" << endl;
    cout << endl;
    cout << "    void backtrack(state, choices) {" << endl;
    cout << "        if (state is a solution) {" << endl;
    cout << "            record(state);" << endl;
    cout << "            return;" << endl;
    cout << "        }" << endl;
    cout << "        for (each choice in choices) {" << endl;
    cout << "            if (choice is valid) {" << endl;
    cout << "                make(choice);           // modify state" << endl;
    cout << "                backtrack(new_state, remaining_choices);" << endl;
    cout << "                undo(choice);           // BACKTRACK" << endl;
    cout << "            }" << endl;
    cout << "        }" << endl;
    cout << "    }" << endl;
    cout << endl;
    cout << "  The three key ingredients:" << endl;
    cout << "    1. BASE CASE:  When do we have a complete solution?" << endl;
    cout << "    2. CHOICES:    What can we try at each step?" << endl;
    cout << "    3. UNDO:       Undo each choice so we can try the next one." << endl;
    cout << endl;
    cout << "  Subsets:       include/exclude each element" << endl;
    cout << "  Permutations:  try each unused element at current position" << endl;
    cout << "  N-Queens:      try each column in the current row" << endl;
    cout << endl;
}

// =====================================================================
// main -- run all demos
// =====================================================================
int main() {
    cout << "Chapter 10: Backtracking Introduction" << endl;
    cout << "======================================" << endl << endl;

    demo_subsets();
    demo_permutations();
    demo_nqueens();
    demo_template();

    cout << "Key takeaways:" << endl;
    cout << "  - Backtracking = recursion + undo (try, recurse, undo)" << endl;
    cout << "  - Subsets: 2^n possibilities (include/exclude)" << endl;
    cout << "  - Permutations: n! possibilities (swap approach)" << endl;
    cout << "  - N-Queens: classic constraint-satisfaction problem" << endl;
    cout << "  - The template works for MANY problems -- learn it well!" << endl;
    return 0;
}
