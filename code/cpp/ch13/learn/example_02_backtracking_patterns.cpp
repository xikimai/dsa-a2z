/*
 * Example 2: Backtracking Patterns
 * ==================================
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * Demonstrates backtracking patterns in C++:
 *   Part 1: N-Queens visual (4x4 board)
 *   Part 2: Subset sum with pruning
 *   Part 3: Timing: pruned vs unpruned search
 */

#include <algorithm>
#include <chrono>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;

// ---------- Part 1: N-Queens visual ----------
void part1_nqueens_visual() {
    cout << "=== Part 1: N-Queens (4x4 Visual) ===" << endl;

    int n = 4;
    vector<int> queens;  // queens[i] = column of queen in row i
    set<int> cols, d1, d2;
    vector<vector<string>> solutions;

    function<void(int)> backtrack = [&](int row) {
        if (row == n) {
            vector<string> board;
            for (int r = 0; r < n; r++) {
                string row_str(n, '.');
                row_str[queens[r]] = 'Q';
                board.push_back(row_str);
            }
            solutions.push_back(board);
            return;
        }
        for (int col = 0; col < n; col++) {
            if (cols.count(col) || d1.count(row - col) || d2.count(row + col))
                continue;
            cols.insert(col);
            d1.insert(row - col);
            d2.insert(row + col);
            queens.push_back(col);
            backtrack(row + 1);
            queens.pop_back();
            cols.erase(col);
            d1.erase(row - col);
            d2.erase(row + col);
        }
    };

    backtrack(0);

    cout << "Found " << solutions.size() << " solutions for " << n << "-Queens:" << endl;
    for (int s = 0; s < (int)solutions.size(); s++) {
        cout << "\nSolution " << (s + 1) << ":" << endl;
        for (auto& row : solutions[s]) {
            cout << "  " << row << endl;
        }
    }
    cout << endl;
}

// ---------- Part 2: Subset sum with pruning ----------
void part2_subset_sum_pruning() {
    cout << "=== Part 2: Subset Sum with Pruning ===" << endl;

    vector<int> nums = {3, 7, 1, 8, 4, 12, 5};
    int target = 15;
    int calls_without_pruning = 0;
    int calls_with_pruning = 0;

    // Without pruning
    function<void(int, int)> no_prune = [&](int idx, int sum) {
        calls_without_pruning++;
        if (idx == (int)nums.size()) return;
        // Include
        no_prune(idx + 1, sum + nums[idx]);
        // Exclude
        no_prune(idx + 1, sum);
    };

    // With pruning (sort first, skip if sum exceeds target)
    sort(nums.begin(), nums.end());
    function<void(int, int)> with_prune = [&](int idx, int sum) {
        calls_with_pruning++;
        if (sum == target) return;  // Found solution, stop this branch
        if (idx == (int)nums.size()) return;
        if (sum > target) return;   // PRUNE: over target already
        // Include
        with_prune(idx + 1, sum + nums[idx]);
        // Exclude
        with_prune(idx + 1, sum);
    };

    no_prune(0, 0);
    with_prune(0, 0);

    cout << "Array: {";
    for (int i = 0; i < (int)nums.size(); i++) {
        if (i > 0) cout << ", ";
        cout << nums[i];
    }
    cout << "}, target = " << target << endl;
    cout << "Recursive calls WITHOUT pruning: " << calls_without_pruning << endl;
    cout << "Recursive calls WITH pruning:    " << calls_with_pruning << endl;
    cout << "Pruning saved " << (calls_without_pruning - calls_with_pruning) << " calls!" << endl;
    cout << endl;
}

// ---------- Part 3: Timing comparison ----------
void part3_timing() {
    cout << "=== Part 3: Timing — N-Queens Count ===" << endl;

    for (int n = 1; n <= 10; n++) {
        int count = 0;
        set<int> cols, d1, d2;

        function<void(int)> solve = [&](int row) {
            if (row == n) { count++; return; }
            for (int col = 0; col < n; col++) {
                if (cols.count(col) || d1.count(row - col) || d2.count(row + col))
                    continue;
                cols.insert(col);
                d1.insert(row - col);
                d2.insert(row + col);
                solve(row + 1);
                cols.erase(col);
                d1.erase(row - col);
                d2.erase(row + col);
            }
        };

        auto t1 = chrono::high_resolution_clock::now();
        solve(0);
        auto t2 = chrono::high_resolution_clock::now();
        auto us = chrono::duration_cast<chrono::microseconds>(t2 - t1).count();

        cout << "  n=" << n << ": " << count << " solutions (" << us << " us)" << endl;
    }
    cout << endl;
}

int main() {
    part1_nqueens_visual();
    part2_subset_sum_pruning();
    part3_timing();
    return 0;
}
