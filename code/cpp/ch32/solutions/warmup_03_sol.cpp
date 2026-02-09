/*
 * Solution for Warmup 3: KMP Pattern Search
 * Chapter 32: String Algorithms — Beyond Brute Force
 */
#include <string>
#include <vector>
using namespace std;

vector<int> solve(string text, string pattern) {
    int n = text.size(), m = pattern.size();
    vector<int> matches;
    if (m == 0) return matches;

    vector<int> fail(m, 0);
    int length = 0, i = 1;
    while (i < m) {
        if (pattern[i] == pattern[length]) fail[i++] = ++length;
        else if (length > 0) length = fail[length - 1];
        else fail[i++] = 0;
    }

    int j = 0;
    for (i = 0; i < n; i++) {
        while (j > 0 && text[i] != pattern[j]) j = fail[j - 1];
        if (text[i] == pattern[j]) j++;
        if (j == m) { matches.push_back(i - m + 1); j = fail[j - 1]; }
    }
    return matches;
}

int main() { return 0; }
