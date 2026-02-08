/*
 * Example 1: Complete Search Basics
 * ==================================
 * Chapter 13: Bronze Battle Plan — Complete Search & Simulation
 *
 * Demonstrates the fundamental complete search patterns in C++:
 *   Part 1: Generating all subsets (recursion)
 *   Part 2: Generating all subsets (bitmask)
 *   Part 3: Generating all permutations
 *   Part 4: Robot simulation
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// ---------- Part 1: Subsets via recursion ----------
void part1_subsets_recursive() {
    cout << "=== Part 1: Subsets (Recursion) ===" << endl;

    vector<int> nums = {1, 2, 3};
    vector<vector<int>> result;

    // Recursive helper: for each element, include or exclude
    // We capture 'result' and 'nums' by reference
    function<void(int, vector<int>&)> generate =
        [&](int index, vector<int>& current) {
            if (index == (int)nums.size()) {
                result.push_back(current);
                return;
            }
            // Exclude nums[index]
            generate(index + 1, current);
            // Include nums[index]
            current.push_back(nums[index]);
            generate(index + 1, current);
            current.pop_back();
        };

    vector<int> current;
    generate(0, current);

    // Sort by size then lexicographically
    sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b) {
        if (a.size() != b.size()) return a.size() < b.size();
        return a < b;
    });

    cout << "Subsets of {1, 2, 3}:" << endl;
    for (auto& s : result) {
        cout << "  {";
        for (int i = 0; i < (int)s.size(); i++) {
            if (i > 0) cout << ", ";
            cout << s[i];
        }
        cout << "}" << endl;
    }
    cout << "Total: " << result.size() << " subsets" << endl;
    cout << endl;
}

// ---------- Part 2: Subsets via bitmask ----------
void part2_subsets_bitmask() {
    cout << "=== Part 2: Subsets (Bitmask) ===" << endl;

    vector<int> nums = {1, 2, 3};
    int n = nums.size();
    vector<vector<int>> result;

    // Iterate from 0 to 2^n - 1
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<int> subset;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) {
                subset.push_back(nums[i]);
            }
        }
        result.push_back(subset);
    }

    sort(result.begin(), result.end(), [](const vector<int>& a, const vector<int>& b) {
        if (a.size() != b.size()) return a.size() < b.size();
        return a < b;
    });

    cout << "Subsets of {1, 2, 3} using bitmasks:" << endl;
    for (auto& s : result) {
        cout << "  mask -> {";
        for (int i = 0; i < (int)s.size(); i++) {
            if (i > 0) cout << ", ";
            cout << s[i];
        }
        cout << "}" << endl;
    }
    cout << "Total: " << result.size() << " subsets" << endl;
    cout << endl;
}

// ---------- Part 3: Permutations ----------
void part3_permutations() {
    cout << "=== Part 3: Permutations ===" << endl;

    vector<int> nums = {1, 2, 3};
    sort(nums.begin(), nums.end());

    cout << "Permutations of {1, 2, 3}:" << endl;
    int count = 0;
    do {
        cout << "  [";
        for (int i = 0; i < (int)nums.size(); i++) {
            if (i > 0) cout << ", ";
            cout << nums[i];
        }
        cout << "]" << endl;
        count++;
    } while (next_permutation(nums.begin(), nums.end()));

    cout << "Total: " << count << " permutations" << endl;

    // C++ bonus: next_permutation gives you all permutations
    // in lexicographic order automatically!
    cout << endl;
}

// ---------- Part 4: Robot simulation ----------
void part4_robot_simulation() {
    cout << "=== Part 4: Robot Simulation ===" << endl;

    string commands = "UURRDL";
    int x = 0, y = 0;

    cout << "Commands: " << commands << endl;
    cout << "Start: (" << x << ", " << y << ")" << endl;

    for (char cmd : commands) {
        if (cmd == 'U') y++;
        else if (cmd == 'D') y--;
        else if (cmd == 'L') x--;
        else if (cmd == 'R') x++;
        cout << "  " << cmd << " -> (" << x << ", " << y << ")" << endl;
    }

    cout << "Final position: (" << x << ", " << y << ")" << endl;
    cout << endl;
}

int main() {
    part1_subsets_recursive();
    part2_subsets_bitmask();
    part3_permutations();
    part4_robot_simulation();
    return 0;
}
