/*
 * Example 01: Binary Search on Answers Basics
 * =============================================
 * Chapter 16: Binary Search Beyond Arrays — Searching on Answers
 *
 * Demonstrates BS on answers for integer square root and Koko's bananas.
 */

#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Part 1: Integer Square Root
    cout << "=== Part 1: BS on Answers — Integer Square Root ===" << endl;
    int n = 49;
    cout << "Finding floor(sqrt(" << n << "))" << endl;

    int lo = 0, hi = n;
    int step = 0;
    while (lo < hi) {
        int mid = lo + (hi - lo + 1) / 2;
        step++;
        long long sq = (long long)mid * mid;
        cout << "  Step " << step << ": mid=" << mid << ", mid*mid=" << sq;
        if (sq <= n) {
            cout << " <= " << n << " -> lo = " << mid << endl;
            lo = mid;
        } else {
            cout << " > " << n << " -> hi = " << (mid - 1) << endl;
            hi = mid - 1;
        }
    }
    cout << "Answer: floor(sqrt(" << n << ")) = " << lo << endl;

    // Part 2: Koko's Bananas
    cout << "\n=== Part 2: BS on Answers — Koko Eating Bananas ===" << endl;
    vector<int> piles = {3, 6, 7, 11};
    int h = 8;
    cout << "Piles: [3, 6, 7, 11], Hours: " << h << endl;

    int maxPile = *max_element(piles.begin(), piles.end());
    lo = 1;
    hi = maxPile;
    step = 0;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        step++;
        int hours = 0;
        for (int p : piles) hours += (p + mid - 1) / mid;
        cout << "  Step " << step << ": speed=" << mid << ", hours=" << hours;
        if (hours <= h) {
            cout << " <= " << h << " -> hi = " << mid << endl;
            hi = mid;
        } else {
            cout << " > " << h << " -> lo = " << (mid + 1) << endl;
            lo = mid + 1;
        }
    }
    cout << "Minimum eating speed: " << lo << endl;

    return 0;
}
