/*
 * Solution for Practice 1: Rabin-Karp Pattern Search
 * Chapter 32: String Algorithms — Beyond Brute Force
 */
#include <string>
#include <vector>
using namespace std;

vector<int> solve(string text, string pattern) {
    int n = text.size(), m = pattern.size();
    vector<int> matches;
    if (m == 0 || m > n) return matches;

    long long BASE = 131, MOD = 1e9 + 7;
    long long pHash = 0, tHash = 0, power = 1;
    for (int i = 0; i < m - 1; i++) power = power * BASE % MOD;

    for (int i = 0; i < m; i++) {
        pHash = (pHash * BASE + pattern[i]) % MOD;
        tHash = (tHash * BASE + text[i]) % MOD;
    }

    for (int i = 0; i <= n - m; i++) {
        if (pHash == tHash && text.substr(i, m) == pattern)
            matches.push_back(i);
        if (i < n - m)
            tHash = ((tHash - text[i] * power % MOD + MOD)
                     * BASE + text[i + m]) % MOD;
    }
    return matches;
}

int main() { return 0; }
