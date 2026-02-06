/*
 * Example 02: Advanced Collections
 * =================================
 * Chapter 5: Collections
 *
 * This file covers more powerful collection types:
 *   1. unordered_set and set operations
 *   2. unordered_map and frequency counting (m[k]++ pattern)
 *   3. pair<> and structured bindings
 *   4. Sorting with lambdas and greater<>
 *
 * Build & run:
 *   g++ -std=c++17 -o example_02 code/cpp/ch05/learn/example_02_advanced_collections.cpp && ./example_02
 */

#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;

// =====================================================================
// 1. unordered_set and set operations
// =====================================================================
// unordered_set<T> — a collection of UNIQUE values, with O(1) lookup.
// Like Python's set or Java's HashSet.

void demo_sets() {
    cout << "=== 1. unordered_set and set operations ===" << endl;

    // --- Creating a set ---
    unordered_set<int> nums = {3, 1, 4, 1, 5, 9, 2, 6, 5};
    // Duplicates are automatically removed!
    cout << "  Set from {3,1,4,1,5,9,2,6,5}: ";
    for (int x : nums) cout << x << " ";
    cout << "(size=" << nums.size() << ")" << endl;

    // --- Lookup: O(1) average ---
    cout << "  Contains 4? " << (nums.count(4) ? "yes" : "no") << endl;
    cout << "  Contains 7? " << (nums.count(7) ? "yes" : "no") << endl;

    // --- Insert and erase ---
    nums.insert(7);
    cout << "  After insert(7), contains 7? " << (nums.count(7) ? "yes" : "no") << endl;
    nums.erase(3);
    cout << "  After erase(3), contains 3? " << (nums.count(3) ? "yes" : "no") << endl;

    // --- Set from a vector (remove duplicates) ---
    vector<int> v = {5, 3, 5, 1, 3, 2, 1};
    unordered_set<int> unique_vals(v.begin(), v.end());
    cout << "  Unique values from {5,3,5,1,3,2,1}: ";
    for (int x : unique_vals) cout << x << " ";
    cout << endl;

    // --- Ordered set (std::set) — keeps elements sorted ---
    set<int> ordered = {5, 3, 1, 4, 2};
    cout << "  Ordered set: ";
    for (int x : ordered) cout << x << " ";
    cout << "(always sorted!)" << endl;

    // --- Set intersection (manual, since C++ doesn't have built-in & like Python) ---
    unordered_set<int> a = {1, 2, 3, 4};
    unordered_set<int> b = {3, 4, 5, 6};
    vector<int> intersection;
    for (int x : a) {
        if (b.count(x)) intersection.push_back(x);
    }
    cout << "  Intersection of {1,2,3,4} and {3,4,5,6}: ";
    for (int x : intersection) cout << x << " ";
    cout << endl;
    cout << endl;
}

// =====================================================================
// 2. unordered_map and frequency counting
// =====================================================================
// unordered_map<K, V> — key-value pairs with O(1) lookup.
// Like Python's dict or Java's HashMap.

void demo_maps() {
    cout << "=== 2. unordered_map and frequency counting ===" << endl;

    // --- Creating a map ---
    unordered_map<string, int> ages;
    ages["Alice"] = 14;
    ages["Bob"] = 15;
    ages["Charlie"] = 14;

    cout << "  Alice's age: " << ages["Alice"] << endl;
    cout << "  Map size: " << ages.size() << endl;

    // --- Check if key exists ---
    cout << "  Has 'Bob'? " << (ages.count("Bob") ? "yes" : "no") << endl;
    cout << "  Has 'Dave'? " << (ages.count("Dave") ? "yes" : "no") << endl;

    // WARNING: accessing a missing key with [] CREATES it with value 0!
    // Use .count() or .find() to check first.

    // --- Iterating over a map ---
    cout << "  All entries: ";
    for (const auto& [name, age] : ages) {  // structured binding (C++17)
        cout << name << "=" << age << " ";
    }
    cout << endl;

    // --- THE FREQUENCY COUNTING PATTERN: m[k]++ ---
    // This is one of the most useful patterns in competitive programming!
    string word = "mississippi";
    unordered_map<char, int> freq;
    for (char c : word) {
        freq[c]++;  // If key doesn't exist, it's auto-created with 0, then incremented
    }
    cout << "  Frequencies in \"mississippi\": ";
    for (const auto& [ch, count] : freq) {
        cout << ch << ":" << count << " ";
    }
    cout << endl;

    // --- Another example: word frequency ---
    vector<string> words = {"apple", "banana", "apple", "cherry", "banana", "apple"};
    unordered_map<string, int> word_freq;
    for (const string& w : words) {
        word_freq[w]++;
    }
    cout << "  Word frequencies: ";
    for (const auto& [w, count] : word_freq) {
        cout << w << ":" << count << " ";
    }
    cout << endl;

    // --- Ordered map (std::map) — keeps keys sorted ---
    map<string, int> ordered_ages;
    ordered_ages["Charlie"] = 14;
    ordered_ages["Alice"] = 14;
    ordered_ages["Bob"] = 15;
    cout << "  Ordered map: ";
    for (const auto& [name, age] : ordered_ages) {
        cout << name << "=" << age << " ";
    }
    cout << "(keys always sorted!)" << endl;
    cout << endl;
}

// =====================================================================
// 3. pair<> and structured bindings
// =====================================================================
// pair<A, B> holds two values. It's everywhere in C++ — map entries,
// returning two values from a function, etc.

pair<int, int> find_min_max(vector<int>& nums) {
    int mn = nums[0], mx = nums[0];
    for (int x : nums) {
        if (x < mn) mn = x;
        if (x > mx) mx = x;
    }
    return {mn, mx};  // Shorthand for make_pair(mn, mx)
}

void demo_pairs() {
    cout << "=== 3. pair<> and structured bindings ===" << endl;

    // --- Creating pairs ---
    pair<string, int> student = {"Maya", 14};
    cout << "  student: " << student.first << ", " << student.second << endl;

    pair<int, int> point = make_pair(3, 4);
    cout << "  point: (" << point.first << ", " << point.second << ")" << endl;

    // --- Structured bindings (C++17) — much cleaner! ---
    auto [name, age] = student;
    cout << "  Structured binding: name=" << name << ", age=" << age << endl;

    // --- Using pairs as return values ---
    vector<int> data = {5, 2, 8, 1, 9, 3};
    auto [mn, mx] = find_min_max(data);
    cout << "  Min=" << mn << ", Max=" << mx << " from {5,2,8,1,9,3}" << endl;

    // --- Vector of pairs ---
    vector<pair<string, int>> roster = {
        {"Alice", 95},
        {"Bob", 87},
        {"Charlie", 91}
    };
    cout << "  Roster: ";
    for (const auto& [n, score] : roster) {
        cout << n << "(" << score << ") ";
    }
    cout << endl;
    cout << endl;
}

// =====================================================================
// 4. Sorting with lambdas and greater<>
// =====================================================================
// std::sort is incredibly powerful. You can customize how it sorts
// using lambdas (anonymous functions).

void demo_sorting() {
    cout << "=== 4. Sorting with lambdas and greater<> ===" << endl;

    // --- Basic sort (ascending) ---
    vector<int> nums = {5, 2, 8, 1, 9, 3};
    sort(nums.begin(), nums.end());
    cout << "  Sorted ascending: ";
    for (int x : nums) cout << x << " ";
    cout << endl;

    // --- Sort descending with greater<> ---
    sort(nums.begin(), nums.end(), greater<int>());
    cout << "  Sorted descending: ";
    for (int x : nums) cout << x << " ";
    cout << endl;

    // --- Sort with a lambda (custom comparator) ---
    // A lambda is like a mini-function you write inline.
    // Syntax: [captures](params) { body }
    vector<int> vals = {-3, 1, -7, 4, 2, -5};

    // Sort by absolute value:
    sort(vals.begin(), vals.end(), [](int a, int b) {
        return abs(a) < abs(b);
    });
    cout << "  Sorted by |value|: ";
    for (int x : vals) cout << x << " ";
    cout << endl;

    // --- Sort strings by length ---
    vector<string> words = {"banana", "fig", "apple", "kiwi"};
    sort(words.begin(), words.end(), [](const string& a, const string& b) {
        return a.size() < b.size();
    });
    cout << "  Sorted by length: ";
    for (const string& w : words) cout << w << " ";
    cout << endl;

    // --- Sort pairs: by second element descending ---
    vector<pair<string, int>> scores = {
        {"Alice", 87},
        {"Bob", 95},
        {"Charlie", 91}
    };
    sort(scores.begin(), scores.end(), [](const auto& a, const auto& b) {
        return a.second > b.second;  // Higher score first
    });
    cout << "  By score (desc): ";
    for (const auto& [name, score] : scores) {
        cout << name << "(" << score << ") ";
    }
    cout << endl;

    // --- Stable sort (preserves order of equal elements) ---
    vector<pair<string, int>> data = {
        {"Alice", 90},
        {"Bob", 90},
        {"Charlie", 85}
    };
    stable_sort(data.begin(), data.end(), [](const auto& a, const auto& b) {
        return a.second > b.second;
    });
    cout << "  Stable sort by score: ";
    for (const auto& [name, score] : data) {
        cout << name << "(" << score << ") ";
    }
    cout << "(Alice before Bob since they tied)" << endl;
    cout << endl;
}

// =====================================================================
// main — run all the demos
// =====================================================================
int main() {
    demo_sets();
    demo_maps();
    demo_pairs();
    demo_sorting();

    cout << "All examples done!" << endl;
    return 0;
}
