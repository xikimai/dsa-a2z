/*
 * Example 02: Stock DP — State Machine Thinking
 * ================================================
 * Chapter 23: Dynamic Programming I — The Foundation
 *
 * Demonstrates: Stock I, II, III, Cooldown, Fee
 */

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int stockOne(vector<int>& p) {
    int mn = p[0], profit = 0;
    for (int i = 1; i < (int)p.size(); i++) {
        profit = max(profit, p[i] - mn);
        mn = min(mn, p[i]);
    }
    return profit;
}

int stockUnlimited(vector<int>& p) {
    int profit = 0;
    for (int i = 1; i < (int)p.size(); i++)
        if (p[i] > p[i - 1]) profit += p[i] - p[i - 1];
    return profit;
}

int stockTwoTxn(vector<int>& p) {
    int b1 = -p[0], s1 = 0, b2 = -p[0], s2 = 0;
    for (int i = 1; i < (int)p.size(); i++) {
        b1 = max(b1, -p[i]);
        s1 = max(s1, b1 + p[i]);
        b2 = max(b2, s1 - p[i]);
        s2 = max(s2, b2 + p[i]);
    }
    return s2;
}

int stockCooldown(vector<int>& p) {
    int held = -p[0], sold = 0, rest = 0;
    for (int i = 1; i < (int)p.size(); i++) {
        int ph = held;
        held = max(held, rest - p[i]);
        rest = max(rest, sold);
        sold = ph + p[i];
    }
    return max(sold, rest);
}

int stockFee(vector<int>& p, int fee) {
    int cash = 0, hold = -p[0];
    for (int i = 1; i < (int)p.size(); i++) {
        cash = max(cash, hold + p[i] - fee);
        hold = max(hold, cash - p[i]);
    }
    return cash;
}

int main() {
    vector<int> p1 = {7, 1, 5, 3, 6, 4};
    cout << "Stock I:   " << stockOne(p1) << endl;
    cout << "Stock II:  " << stockUnlimited(p1) << endl;

    vector<int> p2 = {3, 3, 5, 0, 0, 3, 1, 4};
    cout << "Stock III: " << stockTwoTxn(p2) << endl;

    vector<int> p3 = {1, 2, 3, 0, 2};
    cout << "Cooldown:  " << stockCooldown(p3) << endl;

    vector<int> p4 = {1, 3, 2, 8, 4, 9};
    cout << "Fee=2:     " << stockFee(p4, 2) << endl;

    return 0;
}
