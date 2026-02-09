/*
 * Example 02: KMP and Z-Function Demo
 * Chapter 32: String Algorithms — Beyond Brute Force
 */

#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int> buildFailure(const string& pattern) {
    int m = pattern.size();
    vector<int> fail(m, 0);
    int length = 0, i = 1;
    while (i < m) {
        if (pattern[i] == pattern[length]) {
            fail[i++] = ++length;
        } else if (length > 0) {
            length = fail[length - 1];
        } else {
            fail[i++] = 0;
        }
    }
    return fail;
}

vector<int> kmpSearch(const string& text, const string& pattern) {
    vector<int> matches;
    int n = text.size(), m = pattern.size();
    if (m == 0) return matches;
    vector<int> fail = buildFailure(pattern);
    int j = 0;
    for (int i = 0; i < n; i++) {
        while (j > 0 && text[i] != pattern[j]) j = fail[j - 1];
        if (text[i] == pattern[j]) j++;
        if (j == m) { matches.push_back(i - m + 1); j = fail[j - 1]; }
    }
    return matches;
}

vector<int> zFunction(const string& s) {
    int n = s.size();
    vector<int> z(n, 0);
    int l = 0, r = 0;
    for (int i = 1; i < n; i++) {
        if (i < r) z[i] = min(r - i, z[i - l]);
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) z[i]++;
        if (i + z[i] > r) { l = i; r = i + z[i]; }
    }
    return z;
}

int main() {
    cout << "KMP AND Z-FUNCTION DEMO" << endl;

    string pattern = "AABAAAB";
    auto fail = buildFailure(pattern);
    cout << "  Pattern: " << pattern << endl << "  Failure: ";
    for (int f : fail) cout << f << " ";
    cout << endl;

    auto matches = kmpSearch("AABAACAADAABAABA", "AABA");
    cout << "  KMP matches: ";
    for (int m : matches) cout << m << " ";
    cout << endl;

    auto z = zFunction("aabxaa");
    cout << "  Z-array of 'aabxaa': ";
    for (int v : z) cout << v << " ";
    cout << endl;

    return 0;
}
