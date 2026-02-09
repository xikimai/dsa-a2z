/*
 * Solution for Practice 3: Count Distinct Substrings
 * Chapter 32: String Algorithms — Beyond Brute Force
 */
#include <set>
#include <string>
#include <vector>
using namespace std;

int solve(string s) {
    set<string> subs;
    int n = s.size();
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j <= n; j++)
            subs.insert(s.substr(i, j - i));
    return subs.size() + 1; // +1 for empty string
}

int main() { return 0; }
