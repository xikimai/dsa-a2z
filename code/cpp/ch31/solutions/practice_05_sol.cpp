/*
 * Solution for Practice 5: Count Numbers with Unique Digits
 * Chapter 31: Advanced DP — Bitmask, Interval, Trees
 */
#include <algorithm>
#include <climits>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

int digits_arr[10];
int digits_len;
map<long long, int> memo;

int dp(int pos, bool tight, int mask, bool started) {
    if (pos == digits_len) return started ? 1 : 0;

    long long key = ((long long)pos << 13) | ((tight ? 1LL : 0LL) << 12) |
                    ((long long)mask << 1) | (started ? 1LL : 0LL);
    auto it = memo.find(key);
    if (it != memo.end()) return it->second;

    int limit = tight ? digits_arr[pos] : 9;
    int count = 0;

    for (int d = 0; d <= limit; d++) {
        if (started && (mask & (1 << d))) continue;
        bool newTight = tight && (d == limit);
        bool newStarted = started || (d != 0);
        int newMask = newStarted ? (mask | (1 << d)) : mask;
        count += dp(pos + 1, newTight, newMask, newStarted);
    }

    memo[key] = count;
    return count;
}

int solve(int n) {
    string s = to_string(n);
    digits_len = s.size();
    for (int i = 0; i < digits_len; i++) digits_arr[i] = s[i] - '0';
    memo.clear();
    return dp(0, true, 0, false);
}

int main() { return 0; }
