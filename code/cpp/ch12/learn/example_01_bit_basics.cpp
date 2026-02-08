/*
 * Example 1: Bit Manipulation Basics
 * ====================================
 * Chapter 12: Bit Manipulation — The Language of Computers
 *
 * Demonstrates:
 *   Part 1: Binary conversion (manual + bitset)
 *   Part 2: Bitwise operators (AND, OR, XOR, NOT, shifts)
 *   Part 3: Bit checks (i-th bit, power of 2, count set bits)
 *   Part 4: Brian Kernighan's algorithm trace
 */

#include <algorithm>
#include <bitset>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

string toBinary(int n) {
    if (n == 0) return "0";
    string bits;
    while (n > 0) {
        bits += char('0' + n % 2);
        n /= 2;
    }
    reverse(bits.begin(), bits.end());
    return bits;
}

int main() {
    // Part 1: Binary Conversion
    cout << "=== Part 1: Binary Conversion ===" << endl;
    for (int n : {0, 1, 5, 10, 42, 255, 1024}) {
        cout << "  " << n << " = " << toBinary(n)
             << "  (bitset<8>: " << bitset<8>(n) << ")" << endl;
    }

    // Part 2: Bitwise Operators
    cout << "\n=== Part 2: Bitwise Operators ===" << endl;
    int a = 42, b = 15;
    cout << "  a     = " << bitset<8>(a) << "  (" << a << ")" << endl;
    cout << "  b     = " << bitset<8>(b) << "  (" << b << ")" << endl;
    cout << "  a & b = " << bitset<8>(a & b) << "  (" << (a & b) << ")" << endl;
    cout << "  a | b = " << bitset<8>(a | b) << "  (" << (a | b) << ")" << endl;
    cout << "  a ^ b = " << bitset<8>(a ^ b) << "  (" << (a ^ b) << ")" << endl;
    cout << "  ~a    = " << ~a << endl;
    cout << "  a<<2  = " << bitset<8>(a << 2) << "  (" << (a << 2) << ")" << endl;
    cout << "  a>>2  = " << bitset<8>(a >> 2) << "  (" << (a >> 2) << ")" << endl;

    // Part 3: Bit Checks
    cout << "\n=== Part 3: Bit Checks ===" << endl;
    int n = 42;
    cout << "  n = " << n << " = " << bitset<8>(n) << endl;
    for (int i = 0; i < 8; i++) {
        int bit = (n >> i) & 1;
        cout << "    bit " << i << ": " << bit << (bit ? "  SET" : "") << endl;
    }

    cout << "\n  Power of 2 checks:" << endl;
    for (int x : {0, 1, 2, 3, 4, 6, 8, 16, 24, 32, 64, 100, 128}) {
        bool isPow2 = x > 0 && (x & (x - 1)) == 0;
        cout << "    " << x << " -> " << (isPow2 ? "YES" : "no") << endl;
    }

    // Part 4: Brian Kernighan's
    cout << "\n=== Part 4: Brian Kernighan's Algorithm ===" << endl;
    for (int x : {42, 255, 0}) {
        int orig = x;
        int count = 0;
        while (x) {
            x &= (x - 1);
            count++;
        }
        cout << "  " << orig << " = " << bitset<16>(orig) << " -> " << count
             << " set bits (popcount = " << __builtin_popcount(orig) << ")" << endl;
    }

    return 0;
}
