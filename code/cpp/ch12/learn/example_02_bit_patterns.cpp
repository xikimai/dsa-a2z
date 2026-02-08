/*
 * Example 2: Bit Manipulation Patterns
 * ======================================
 * Chapter 12: Bit Manipulation — The Language of Computers
 *
 * Demonstrates:
 *   Part 1: XOR tricks (swap, single number)
 *   Part 2: Bitmask as set operations
 *   Part 3: Power set generation
 *   Part 4: Two odd-occurring numbers
 */

#include <algorithm>
#include <bitset>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    // Part 1: XOR Tricks
    cout << "=== Part 1: XOR Tricks ===" << endl;
    int a = 42, b = 99;
    cout << "  Before: a=" << a << ", b=" << b << endl;
    a ^= b; b ^= a; a ^= b;
    cout << "  After:  a=" << a << ", b=" << b << endl;

    vector<int> nums = {4, 1, 2, 1, 2};
    int single = 0;
    for (int x : nums) single ^= x;
    cout << "  Single number: " << single << endl;

    // Part 2: Bitmask as Set
    cout << "\n=== Part 2: Bitmask as Set ===" << endl;
    string elements[] = {"A", "B", "C", "D"};
    int n = 4;
    auto maskToStr = [&](int mask) -> string {
        string s = "{";
        bool first = true;
        for (int i = 0; i < n; i++) {
            if ((mask >> i) & 1) {
                if (!first) s += ", ";
                s += elements[i];
                first = false;
            }
        }
        return s + "}";
    };

    int mask = 0;
    mask |= (1 << 0); cout << "  Add A:  " << maskToStr(mask) << endl;
    mask |= (1 << 2); cout << "  Add C:  " << maskToStr(mask) << endl;
    mask ^= (1 << 1); cout << "  Tog B:  " << maskToStr(mask) << endl;
    mask &= ~(1 << 0); cout << "  Rem A:  " << maskToStr(mask) << endl;

    // Part 3: Power Set
    cout << "\n=== Part 3: Power Set ===" << endl;
    vector<int> elems = {1, 2, 3};
    int en = elems.size();
    for (int m = 0; m < (1 << en); m++) {
        cout << "  " << bitset<3>(m) << " -> [";
        bool first = true;
        for (int i = 0; i < en; i++) {
            if ((m >> i) & 1) {
                if (!first) cout << ",";
                cout << elems[i];
                first = false;
            }
        }
        cout << "]" << endl;
    }

    // Part 4: Two Odd-Occurring Numbers
    cout << "\n=== Part 4: Two Odd-Occurring ===" << endl;
    vector<int> arr = {2, 4, 7, 9, 2, 4};
    int xorAll = 0;
    for (int x : arr) xorAll ^= x;
    int diffBit = xorAll & (-xorAll);
    int p = 0, q = 0;
    for (int x : arr) {
        if (x & diffBit) p ^= x;
        else q ^= x;
    }
    if (p > q) swap(p, q);
    cout << "  Input: [2,4,7,9,2,4]" << endl;
    cout << "  Two odd: [" << p << ", " << q << "]" << endl;

    return 0;
}
