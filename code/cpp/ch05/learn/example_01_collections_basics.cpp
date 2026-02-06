/*
 * Example 01: Collections Basics
 * ==============================
 * Chapter 5: Collections
 *
 * This file walks through the fundamental collection types in C++:
 *   1. Creating vectors and C-arrays
 *   2. Accessing and modifying (push_back, insert, erase, at())
 *   3. String operations (mutability!, substr, find, size)
 *   4. Iterating (range-based for, index-based, auto&)
 *
 * Build & run:
 *   g++ -std=c++17 -o example_01 code/cpp/ch05/learn/example_01_collections_basics.cpp && ./example_01
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// =====================================================================
// 1. Creating vectors and C-arrays
// =====================================================================
// In C++, the two main ways to store a sequence of values are:
//   - vector<T>  (dynamic, resizable — this is what you'll use 99% of the time)
//   - T[]        (fixed-size C-array — older style, still useful to know)

void demo_creating() {
    cout << "=== 1. Creating vectors and C-arrays ===" << endl;

    // --- Vectors ---
    vector<int> empty_vec;                      // Empty vector
    vector<int> nums = {10, 20, 30, 40, 50};   // Initialize with values
    vector<string> words = {"hello", "world"};  // Works with any type
    vector<int> zeros(5, 0);                    // 5 zeros: {0, 0, 0, 0, 0}
    vector<int> ones(3, 1);                     // 3 ones:  {1, 1, 1}

    cout << "  nums has " << nums.size() << " elements" << endl;
    cout << "  empty_vec has " << empty_vec.size() << " elements" << endl;
    cout << "  zeros: ";
    for (int x : zeros) cout << x << " ";
    cout << endl;

    // --- C-arrays (fixed size, decided at compile time) ---
    int scores[5] = {95, 87, 91, 78, 100};
    int all_zeros[3] = {};  // All initialized to 0

    cout << "  scores[0] = " << scores[0] << endl;
    cout << "  all_zeros[2] = " << all_zeros[2] << endl;

    // KEY DIFFERENCE: vectors know their size, C-arrays do NOT.
    cout << "  nums.size() works: " << nums.size() << endl;
    // scores has no .size() — you'd have to track it yourself.
    // That's why we prefer vectors in modern C++!
    cout << endl;
}

// =====================================================================
// 2. Accessing and modifying (push_back, insert, erase, at())
// =====================================================================
// Vectors are mutable — you can add, remove, and change elements.

void demo_accessing() {
    cout << "=== 2. Accessing and modifying ===" << endl;

    vector<int> nums = {10, 20, 30};

    // --- Accessing elements ---
    cout << "  nums[0] = " << nums[0] << endl;       // Fast, no bounds check
    cout << "  nums.at(1) = " << nums.at(1) << endl;  // Safe, throws if out of range
    cout << "  nums.front() = " << nums.front() << endl;
    cout << "  nums.back() = " << nums.back() << endl;

    // --- push_back: add to the end ---
    nums.push_back(40);
    nums.push_back(50);
    cout << "  After push_back(40, 50): ";
    for (int x : nums) cout << x << " ";
    cout << endl;

    // --- insert: add at a specific position ---
    // insert takes an ITERATOR, not an index. begin() + i gives iterator at index i.
    nums.insert(nums.begin() + 2, 25);  // Insert 25 at index 2
    cout << "  After insert(25 at idx 2): ";
    for (int x : nums) cout << x << " ";
    cout << endl;

    // --- erase: remove at a specific position ---
    nums.erase(nums.begin() + 0);  // Remove first element
    cout << "  After erase(idx 0): ";
    for (int x : nums) cout << x << " ";
    cout << endl;

    // --- pop_back: remove last element ---
    nums.pop_back();
    cout << "  After pop_back(): ";
    for (int x : nums) cout << x << " ";
    cout << endl;

    // --- Modify in place ---
    nums[0] = 99;
    cout << "  After nums[0] = 99: ";
    for (int x : nums) cout << x << " ";
    cout << endl;

    // --- Check if empty ---
    cout << "  nums.empty()? " << (nums.empty() ? "yes" : "no") << endl;

    // --- Clear everything ---
    nums.clear();
    cout << "  After clear(), size = " << nums.size() << endl;
    cout << endl;
}

// =====================================================================
// 3. String operations (mutability!, substr, find, size)
// =====================================================================
// Unlike Python and Java, C++ strings are MUTABLE — you can change
// individual characters in place!

void demo_strings() {
    cout << "=== 3. String operations ===" << endl;

    string s = "Hello, World!";
    cout << "  s = \"" << s << "\"" << endl;
    cout << "  s.size() = " << s.size() << endl;
    cout << "  s.length() = " << s.length() << endl;  // same as size()

    // --- C++ strings are MUTABLE! (Unlike Python/Java) ---
    s[0] = 'h';
    cout << "  After s[0] = 'h': \"" << s << "\"" << endl;

    // --- substr(start, length) — note: LENGTH, not end index! ---
    string sub = s.substr(0, 5);  // "hello"
    cout << "  s.substr(0, 5) = \"" << sub << "\"" << endl;

    string sub2 = s.substr(7);  // "World!" — from index 7 to end
    cout << "  s.substr(7) = \"" << sub2 << "\"" << endl;

    // --- find: search for a substring ---
    size_t pos = s.find("World");
    cout << "  s.find(\"World\") = " << pos << endl;

    size_t not_found = s.find("xyz");
    if (not_found == string::npos) {
        cout << "  s.find(\"xyz\") = not found (string::npos)" << endl;
    }

    // --- Concatenation ---
    string a = "Hello";
    string b = " World";
    string c = a + b;
    cout << "  \"Hello\" + \" World\" = \"" << c << "\"" << endl;

    // --- append and += ---
    a += "!!!";
    cout << "  After += \"!!!\": \"" << a << "\"" << endl;

    // --- Comparing strings (works with ==, <, >, etc.) ---
    cout << "  \"abc\" == \"abc\"? " << ("abc" == string("abc") ? "yes" : "no") << endl;
    cout << "  \"abc\" < \"abd\"? " << (string("abc") < string("abd") ? "yes" : "no") << endl;

    // --- Useful string methods ---
    string text = "  spaces around  ";
    cout << "  Before erase: \"" << text << "\"" << endl;

    // There's no built-in trim in C++, but you can use erase + find:
    // (This is a common gotcha compared to Python's strip()!)

    // Convert to uppercase manually (no built-in like Python's .upper()):
    string upper = "hello";
    for (char& ch : upper) {
        ch = toupper(ch);
    }
    cout << "  \"hello\" uppercased: \"" << upper << "\"" << endl;
    cout << endl;
}

// =====================================================================
// 4. Iterating (range-based for, index-based, auto&)
// =====================================================================
// Three main ways to loop through a vector or string.

void demo_iterating() {
    cout << "=== 4. Iterating ===" << endl;

    vector<int> nums = {10, 20, 30, 40, 50};

    // --- Style 1: Range-based for (preferred for reading) ---
    cout << "  Range-based for: ";
    for (int x : nums) {
        cout << x << " ";
    }
    cout << endl;

    // --- Style 2: Range-based for with auto& (modify in place) ---
    // 'auto&' means: figure out the type AND give me a reference.
    // Without '&', you'd get a COPY and changes wouldn't stick.
    for (auto& x : nums) {
        x *= 2;  // This modifies the original vector!
    }
    cout << "  After doubling with auto&: ";
    for (int x : nums) cout << x << " ";
    cout << endl;

    // --- Style 3: Index-based (when you need the index) ---
    cout << "  Index-based: ";
    for (int i = 0; i < (int)nums.size(); i++) {
        cout << "[" << i << "]=" << nums[i] << " ";
    }
    cout << endl;

    // --- Iterating over strings ---
    string word = "Hello";
    cout << "  Chars in \"Hello\": ";
    for (char c : word) {
        cout << c << " ";
    }
    cout << endl;

    // --- Iterating with const auto& (read-only, avoids copies) ---
    vector<string> names = {"Alice", "Bob", "Charlie"};
    cout << "  Names: ";
    for (const auto& name : names) {
        cout << name << " ";
    }
    cout << endl;

    // --- Reverse iteration ---
    cout << "  Reverse: ";
    for (int i = (int)nums.size() - 1; i >= 0; i--) {
        cout << nums[i] << " ";
    }
    cout << endl;
    cout << endl;
}

// =====================================================================
// main — run all the demos
// =====================================================================
int main() {
    demo_creating();
    demo_accessing();
    demo_strings();
    demo_iterating();

    cout << "All examples done!" << endl;
    return 0;
}
