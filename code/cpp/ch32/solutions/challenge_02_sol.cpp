/*
 * Solution for Challenge 2: Shortest Palindrome (KMP)
 * Chapter 32: String Algorithms — Beyond Brute Force
 */
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

string solve(string s) {
    if (s.size() <= 1) return s;

    string rev = s;
    reverse(rev.begin(), rev.end());
    string combined = s + "#" + rev;

    int n = combined.size();
    vector<int> fail(n, 0);
    int length = 0, i = 1;
    while (i < n) {
        if (combined[i] == combined[length]) fail[i++] = ++length;
        else if (length > 0) length = fail[length - 1];
        else fail[i++] = 0;
    }

    int longestPalPrefix = fail[n - 1];
    string suffixToAdd = rev.substr(0, s.size() - longestPalPrefix);
    return suffixToAdd + s;
}

int main() { return 0; }
